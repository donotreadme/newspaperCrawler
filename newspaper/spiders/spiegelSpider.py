import scrapy
from newspaper.items import NewspaperItem
import json
import sys
import os

parentdir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
sys.path.append(parentdir)
import main

class SpiegelSpider(scrapy.Spider):
    name = 'getSpiegelArticle'
    start_urls = ['https://www.spiegel.de/schlagzeilen/index.rss']

    def parse(self, response):
        articles = response.xpath("//item/link/text()").getall()
        for article in articles:
            if not main.is_in_database(article):
                yield response.follow(article, self.parseArticle)

    def parseArticle(self, response):
        text = response.css("article p::text").getall()
        #Daten liegen im Quelltext sowohl als Metadaten als auch als json vor
        news = NewspaperItem()
        news['articleBody'] = text
        news['headline'] = response.xpath("//title/text()").get()
        news['headlineSocial'] = response.xpath("//meta[@name='twitter:title']/@content").get()        
        news['author'] = response.xpath("//meta[@name='author']/@content").get()
        news['keywords'] = response.xpath("//meta[@name='news_keywords']/@content").extract()
        news['dateModified'] = response.xpath("//meta[@name='last-modified']/@content").get()
        news['datePublished'] = response.xpath("//meta[@name='date']/@content").get()
        news['description'] = response.xpath("//meta[@name='description']/@content").get()
        
        text = response.xpath("//script[@type='application/ld+json']/text()").get()
        elements = json.loads(text) 
        news['articleSection'] = elements[0].get('articleSection')
        
        return news
        
