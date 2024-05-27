# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class KnowckknowckCrawlingItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    id = scrapy.Field()
    title = scrapy.Field()
    content = scrapy.Field()
    created_at = scrapy.Field()
    original_url = scrapy.Field()
    category = scrapy.Field()
    

class Article(scrapy.Item):
    id = scrapy.Field()
    title = scrapy.Field()
    content = scrapy.Field()
    created_at = scrapy.Field()
    original_url = scrapy.Field()
    category = scrapy.Field()
