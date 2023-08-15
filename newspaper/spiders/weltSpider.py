import scrapy
from newspaper.items import NewspaperItem
import json


class WeltSpider(scrapy.Spider):
    name = 'getWeltArticle'
    start_urls = ['https://www.welt.de/feeds/latest.rss']

    def parse(self, response):
        articles = response.xpath("//item/link/text()").getall()
        yield from response.follow_all(articles, self.parseArticle)

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
        
        