import scrapy
from newspaper.items import NewspaperItem
import json
import os
import sys

parentdir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
sys.path.append(parentdir)
import main

class WeltSpider(scrapy.Spider):
    name = 'getWeltArticle'
    start_urls = ['https://www.welt.de/feeds/latest.rss']

    def parse(self, response):
        articles = response.xpath("//item/link/text()").getall()
        for article in articles:
            if not main.is_in_database(article):
                yield response.follow(article, self.parseArticle)

    def parseArticle(self, response):
        text = response.xpath("//script[contains(., 'articleBody')]/text()").get()
        elements = json.loads(text)     
        news = NewspaperItem()
        news['headline'] = elements.get('headline')
        news['headlineSocial'] = elements.get('alternativeHeadline')
        news['articleSection'] = elements.get('category')
        news['author'] = elements.get('author')
        news['keywords'] = elements.get('about')
        news['dateModified'] = elements.get('dateModified')
        news['datePublished'] = elements.get('datePublished')
        news['description'] = elements.get('description')
        news['articleBody'] = elements.get('articleBody')
        return news
        
        