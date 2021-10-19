import scrapy
from newspaper.items import NewspaperItem
import json


class ImageSpider(scrapy.Spider):
    name = "getImages"
    f = open("WeltDE_Urls.txt", "r")
    start_urls = [url.strip() for url in f.readlines()]
    f.close()
    f = open("SpiegelDE_Urls.txt", "r")
    for url in f.readlines():
        start_urls.append(url.strip())
    f.close()
    
    def parse(self, response):
        # initalize a NewsPaperItem which gets later returned to the scrapy pipeline 
        news = NewspaperItem()
        # the path to images is the same for Welt and Spiegel 
        image_path = response.xpath("//meta[@property='og:image']/@content").get()
        news['image_urls'] = [image_path]
        
        if 'www.welt.de' in response.url:
            text = response.xpath("//script[contains(., 'articleBody')]/text()").get()
            elements = json.loads(text)
            news['headline'] = elements.get('headline')
            news['headlineSocial'] = elements.get('alternativeHeadline')
            news['articleSection'] = elements.get('category')
            news['author'] = elements.get('author')
            news['keywords'] = elements.get('about')
            news['dateModified'] = elements.get('dateModified')
            news['datePublished'] = elements.get('datePublished')
            news['description'] = elements.get('description')
            news['articleBody'] = elements.get('articleBody')
            
        elif 'www.spiegel.de' in response.url:
            text = response.css("article p::text").getall()
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
            
    # outdated: can be used if only the images have to be saved 
        # path = response.xpath("//meta[@property='og:image']/@content").get()       
        # yield NewspaperItem(image_urls = [path])