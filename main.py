import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
import pandas as pd
import logging

outfilename = "articles.jl" #TODO: only temporary solution

def start_crawl():
    settings = get_project_settings()    
    # customization of the settings
    settings['FEEDS'] = {
            outfilename: {"format": "jsonlines", 'encoding': "utf8"}        
        }
    settings['LOG_FILE'] = "crawler.log"
    settings['LOG_LEVEL'] = "INFO"
    
    process = CrawlerProcess(settings)
    process.crawl("getNtvArticle")
    process.crawl("getSpiegelArticle")
    process.crawl("getTagesschauArticle")
    process.crawl("getWeltArticle")    
    process.start()  # the script will block here until all crawling jobs are finished

def is_in_database(url):
    try:
        with open(outfilename, "r") as f: 
            dataframe = pd.read_json(f, lines=True)
        if len(dataframe[dataframe.url==url]) > 0:
            return True
        else:
            return False
    except FileNotFoundError:
        logging.info("File doesn't exist yet")
    return False

if __name__ == "__main__":
    start_crawl()
    pass
