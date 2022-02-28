import scrapy
from newspaper.items import NewspaperItem
import json


class NtvSpider(scrapy.Spider):
    name = 'getNtvArticle'
    start_urls = ['https://www.n-tv.de/rss']
    
    def parse(self, response):
        articles = response.xpath("//item/link/text()").getall()
        yield from response.follow_all(articles, self.parseArticle)
        pass

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
        news['dateModified'] = elements['dateModified']
        news['datePublished'] = elements['datePublished']
        return news
    
    
        
