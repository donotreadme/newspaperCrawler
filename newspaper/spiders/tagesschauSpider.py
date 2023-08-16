import scrapy
from newspaper.items import NewspaperItem
import json
import sys
import os

parentdir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
sys.path.append(parentdir)
import main

class TagesschauSpider(scrapy.Spider):
    name = 'getTagesschauArticle'
    start_urls = ['https://www.tagesschau.de/infoservices/alle-meldungen-100~rss2.xml']
    
    def parse(self, response):
        articles = response.xpath("//item/link/text()").getall()
        for article in articles:
            if not main.is_in_database(article):
                yield response.follow(article, self.parseArticle)

    def parseArticle(self, response):
        news = NewspaperItem()
        news['url'] = response.url
        news['headline'] = response.xpath("//title/text()").get()
        news['headlineSocial'] = response.xpath("//meta[@name='twitter:title']/@content").get()
        news['articleSection'] = response.url.split("/")[3]
        news['author'] = response.xpath("//meta[@name='author']/@content").get()
        news['articleBody'] = response.xpath("//p[@class]/text()").getall()
        news['keywords'] = response.xpath("//ul[@class='taglist']/li/a/text()").getall()        
        text = response.xpath("//script[@type='application/ld+json']/text()").get()
        elements = json.loads(text)
        news['description'] = elements['description']
        news['dateModified'] = elements['dateModified']
        news['datePublished'] = elements['datePublished']
        return news
    
    
        
