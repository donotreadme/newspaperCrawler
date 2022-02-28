import scrapy
from newspaper.items import NewspaperItem
import json


class TagesschauSpider(scrapy.Spider):
    name = 'getTagesschauArticle'
    start_urls = ['https://www.tagesschau.de']
    
    def parse(self, response):
        articles = response.xpath("//a[@class='teaser__link']/@href").getall()
        yield from response.follow_all(articles, self.parseArticle)
        articles = response.xpath("//a[@class='teaser-xs__link']/@href").getall()
        yield from response.follow_all(articles, self.parseArticle)
        pass

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
    
    
        
