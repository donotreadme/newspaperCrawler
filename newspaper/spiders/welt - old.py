import scrapy
from newspaper.items import NewspaperItem


class PosttestSpider(scrapy.Spider):
    name = 'getOldWeltArticle'
    start_urls = ["https://www.welt.de/politik/deutschland/article232888433/Querdenker-in-Berlin-Polizei-ermittelt-nach-Angriff-auf-Gewerkschafter.html"]
    

    def parse(self, response):
        text = response.xpath("//script[contains(., 'articleBody')]/text()").get()
        lines = text.split("\n  ")
        elements = {}
        for x in lines: 
            if " : " in x:
                splited = x.split(" : ")
                elements[splited[0].replace('"', '')] = splited[1].replace('"', '')             
        news = NewspaperItem()
        news['headline'] = elements.get('headline')
        news['headlineSocial'] = elements.get('alternativeHeadline')
        news['articleSection'] = elements.get('category')
        #TODO news['author'] = elements.get('headline')
        news['keywords'] = elements.get('about')
        news['dateModified'] = elements.get('dateModified')
        news['datePublished'] = elements.get('datePublished')
        news['description'] = elements.get('description')
        news['articleBody'] = elements.get('articleBody')
        return news
        
        