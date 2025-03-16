# Scrapy settings for tutorial project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

###################### PROPERTIES ######################

BOT_NAME = "booking"

SPIDER_MODULES = ["booking.spiders"]
NEWSPIDER_MODULE = "booking.spiders"

ROBOTSTXT_OBEY = True # Obey robots.txt rules

COOKIES_ENABLED = True # Ensure cookies are enabled for scraping purposes

# Set settings whose default value is deprecated to a future-proof value
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"

# Configure Playwright to use Chromium
PLAYWRIGHT_BROWSER_TYPE = 'chromium'

PLAYWRIGHT_LAUNCH_OPTIONS = {"headless": False}

##################### DOWNLOAD HANDLER SETTINGS ######################
DOWNLOAD_HANDLERS = {
    "http": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
    "https": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
}

####################### MIDDLEWARE SETTINGS ######################
DOWNLOADER_MIDDLEWARES = {
    'booking.middlewares.RotateUserAgentMiddleware': 543,  # Custom middleware with priority 543
}

##################### ITEM PIPELINE SETTINGS ######################
ITEM_PIPELINES = {
    #'booking.pipelines.HtmlWriterPipeline': 1,  # 1 ensures it runs first MIDDLEWARE FOR DEBUGGING PURPOSES
}

ROTATE_USER_AGENTS = [
        # Google Chrome (Windows)
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36',
        
        # Mozilla Firefox (Windows)
        'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0',
        'Mozilla/5.0 (Windows NT 6.1; rv:36.0) Gecko/20100101 Firefox/36.0',
        'Mozilla/5.0 (Windows NT 6.1; rv:35.0) Gecko/20100101 Firefox/35.0',
        
        # Apple Safari (Mac OS)
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
        
        # Opera (Windows)
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 OPR/45.0.2552.888',
        'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0 OPR/32.0.1948.25',
        
        # Microsoft Edge (Windows)
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36 Edge/17.17134',
        # Add more user agents here
]

URLLENGTH_LIMIT=5000 # Limit the length of URLs to avoid errors in Scrapy

