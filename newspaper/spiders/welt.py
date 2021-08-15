import scrapy
from newspaper.items import NewspaperItem
import json


class PosttestSpider(scrapy.Spider):
    name = 'getWeltArticle'
    f = open("WeltDE_Urls.txt", "r")
    start_urls = [url.strip() for url in f.readlines()]
    f.close()

    def parse(self, response):
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
        
        