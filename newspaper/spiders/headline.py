# -*- coding: utf-8 -*-
"""
Created on Fri Aug 13 01:29:32 2021

@author: Frank
"""

import scrapy


class PosttestSpider(scrapy.Spider):
    name = 'getHeadlines'
    start_urls = ['https://www.welt.de/newsticker/',
                  'https://www.spiegel.de/schlagzeilen/']
    
    def parse(self, response):
        if (response.url == "https://www.welt.de/newsticker/"):
            f = open("WeltDE_Urls.txt", "w")
            for lines in response.css("article"): #response.xpath("//article//a/@href")
                if lines.css("a::attr(href)").get() is not None: 
                    f.write(response.url[:-1] + lines.css("a::attr(href)").get() + '\n')
        
        if (response.url == "https://www.spiegel.de/schlagzeilen/"):
            f = open("SpiegelDE_Urls.txt", "w")
            for lines in response.css("article"):
                f.write(lines.css("a::attr(href)").get() + "\n")