# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class PropertyItem(scrapy.Item):
    name = scrapy.Field()
    latitude = scrapy.Field()
    longitude = scrapy.Field()
    address = scrapy.Field()
    # city = scrapy.Field()
    # country = scrapy.Field()
    price = scrapy.Field()
    rating = scrapy.Field()
