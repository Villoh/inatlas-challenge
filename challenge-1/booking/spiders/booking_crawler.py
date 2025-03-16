from datetime import datetime, timedelta
import logging
from urllib.parse import urlencode
import scrapy
from booking.items import PropertyItem

class BookingPropertiesCrawler(scrapy.Spider):
    """
    A Scrapy spider to crawl booking.com properties based on a given keyword and date range.
    """

    name = "booking_properties"
    custom_settings = {
        'LOG_ENABLED': True,
        'LOG_LEVEL': "INFO",  # Set the log level to INFO for better readability
        'LOG_FILE': 'booking_properties.log',
        'LOG_FILE_APPEND': True,
        
        'FEEDS': {
            'booking_properties_output.csv': {
                'format': 'csv',
                'fields': ['name', 'latitude', 'longitude', 'address', 'price', 'rating', 'url']
            }
        }
    }
    
    def __init__(self, search_keyword="Spain", checkin=datetime.now(), checkout=datetime.now() + timedelta(days=1),
                 group_adults=1, group_children=0, max_results=200, **kwargs):
        self.search_keyword = search_keyword
        self.checkin = checkin.strftime("%Y-%m-%d")
        self.checkout = checkout.strftime("%Y-%m-%d")
        self.group_adults = group_adults
        self.group_children = group_children
        self.max_results = max_results
        self.query_params = {
            'ss': self.search_keyword,
            'checkin': self.checkin,
            'checkout': self.checkout,
            'group_adults': self.group_adults,
            'group_children': self.group_children
        }
        self.start_urls = [f"https://www.booking.com/searchresults.es.html?{urlencode(self.query_params)}"]
        self.processed_items = set()
        self.processed_urls = set()

        super().__init__(**kwargs)

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(
                url=url,
                callback=self.parse_search_results,
                meta={
                    'playwright': True,
                    'playwright_include_page': True,
                },
            )

    async def parse_search_results(self, response):
        page = response.meta.get("playwright_page")
        if not page:
            self.log("Playwright page not found in response meta.", logging.ERROR)
            return

        try:
            while True: #Infinite loop 

                await page.wait_for_selector('[data-testid="property-card"]', timeout=10000)
                hotel_cards = await page.query_selector_all('[data-testid="property-card"]')
                
                for hotel in hotel_cards:
                    hotel_element = await hotel.query_selector('[data-testid="property-card-desktop-single-image"]')
                    if not hotel_element:
                        continue
                    
                    hotel_link = await hotel_element.get_attribute("href")
                    if not hotel_link:
                        continue

                    # Skip hotel if URL is already processed
                    if hotel_link in self.processed_urls:
                        continue

                    # Add URL to processed list
                    self.processed_urls.add(hotel_link)

                    self.log(f"Found hotel link: {hotel_link}", logging.INFO)
                    
                    price_element = await hotel.query_selector('span[data-testid="price-and-discounted-price"]')
                    price = (await price_element.inner_text()).replace('\xa0', '').strip() if price_element else 'N/A'
                    hotel_url = response.urljoin(hotel_link)
                    
                    if len(self.processed_items) >= self.max_results:
                        self.log(f"Reached max results ({self.max_results}), stopping further processing.", logging.INFO)
                        await page.context.close()
                        self.crawler.engine.close_spider(self, reason="max_results_reached")
                        return 
                    
                    yield scrapy.Request(
                        url=hotel_url,
                        callback=self.parse_hotel_page,
                        meta={
                            'playwright': True,
                            'playwright_include_page': True,
                            'price': price
                        },
                    )

                # Scroll to the bottom of the page to ensure the "Load more results" button is visible
                self.log("Scrolling to the bottom of the page", logging.INFO)
                await page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
                await page.wait_for_timeout(2000)  # Wait for scroll to complete

                # Look for the "Load More" button - try multiple possible selectors
                load_more_button = await page.query_selector('div.c82435a4b8 button.a83ed08757.c0e0affd09 span.e4adce92df')
                if not load_more_button:
                    # If not found by class name, try with the text content
                    load_more_button = await page.query_selector('button:has-text("Load more results")')
                    self.log("Found 'Load more results' button by text", logging.INFO)
                
                if load_more_button:
                    self.log("Clicking 'Show more results' button to load more hotels", logging.INFO)
                    # Scroll to the button to make sure it's visible
                    await load_more_button.scroll_into_view_if_needed()
                    await load_more_button.click()
                    # Wait for new content to load
                    await page.wait_for_timeout(3000)
                    await page.wait_for_load_state("domcontentloaded")
                else:
                    self.log("No more results to load - button not found", logging.INFO)
                    break  # No more results, exit loop
        except Exception as e:
            self.log(f"Error parsing search results: {e}. With url: {response.url}", logging.ERROR)

    async def parse_hotel_page(self, response):
        page = response.meta.get("playwright_page")
        await page.wait_for_load_state('domcontentloaded')
        price = response.meta.get("price", "N/A")
        url = response.url

        if len(self.processed_items) >= self.max_results:
            self.log(f"Reached max results ({self.max_results}), stopping further processing.", logging.INFO)
            await page.context.close()
            self.crawler.engine.close_spider(self, reason="max_results_reached")
            return 

        if not page:
            self.log("Playwright page not found in response meta for hotel page.", logging.ERROR)
            return
        
        try:
            self.log(f"Processing hotel page: {url}", logging.INFO)
            name = (await page.locator('h2.d2fee87262.pp-header__title').text_content() or "").strip()
            latlong = (await page.locator('a#map_trigger_header_pin').get_attribute('data-atlas-latlng') or "").strip()
            latitude, longitude = self.get_coordinates(latlong)
    
            address_element = page.locator('div.a53cbfa6de.f17adf7576').first
            address = (await address_element.evaluate('(el) => el.childNodes[0].textContent') or "").strip()
            
            rating = (await page.locator('div#js--hp-gallery-scorecard').get_attribute('data-review-score') or "").strip()
        except Exception as e:
            self.log(f"Error parsing hotel page: {e}. With url: {url}", logging.ERROR)
        
        item = PropertyItem(name=name, latitude=latitude, longitude=longitude, address=address, rating=rating, price=price, url=url)
        self.log(f'Property extracted: {item}', logging.INFO)
        self.processed_items.add(item)
        yield item
        
        # Close the page and context after processing each hotel page
        await page.close()


    def get_coordinates(self, latlong):
        if latlong:
            try:
                latitude, longitude = latlong.split(',')
                return float(latitude), float(longitude)
            except ValueError:
                self.log(f"Invalid coordinates format: {latlong}", logging.WARNING)
        return None, None
