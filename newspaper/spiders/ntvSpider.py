import scrapy
from newspaper.items import NewspaperItem
import json
import sys
import os

parentdir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
sys.path.append(parentdir)
import main

class NtvSpider(scrapy.Spider):
    name = 'getNtvArticle'
    start_urls = ['https://www.n-tv.de/rss']
    
    def parse(self, response):
        articles = response.xpath("//item/link/text()").getall()
        for article in articles:
            if not main.is_in_database(article):
                yield response.follow(article, self.parseArticle)

    def parseArticle(self, response):
        news = NewspaperItem()
        news['url'] = response.url
        news['headlineSocial'] = response.xpath("//meta[@property='twitter:title']/@content").get()
        news['keywords'] = response.xpath("//meta[@name='keywords']/@content").get()
        news['articleBody'] = response.xpath("//div[@class='article__text']/p/text()").getall()
        news['articleSection'] = response.url.split("/")[3]
        text = response.xpath("//script[@type='application/ld+json']/text()").get()
        elements = json.loads(text)        
        news['headline'] = elements['headline']
        news['author'] = elements['author']
        news['description'] = elements['description']
        news['dateModified'] = response.xpath("//meta[@name='last-modified']/@content").get()
        news['datePublished'] = response.xpath("//meta[@name='date']/@content").get()
        return news
    
    
        
