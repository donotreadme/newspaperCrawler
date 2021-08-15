# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class NewspaperItem(scrapy.Item):
    url = scrapy.Field()
    headline = scrapy.Field()
    headlineSocial = scrapy.Field()
    articleSection = scrapy.Field()
    author = scrapy.Field()
    keywords = scrapy.Field()
    dateModified = scrapy.Field()
    datePublished = scrapy.Field()
    description = scrapy.Field()
    articleBody = scrapy.Field()    
