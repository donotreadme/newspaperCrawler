import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
import pandas as pd
import logging
from datetime import datetime
import time
import sys

outfilename = "articles.jl" #TODO: only temporary solution


def start_crawl():
    settings = get_project_settings()    
    # customization of the settings
    settings['FEEDS'] = {
            outfilename: {"format": "jsonlines"}        
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


def wait(list_of_hours: list):
    # find the closest hour above the current time
    list_of_hours = sorted(list_of_hours, reverse=True)
    closest_hour = list_of_hours[-1]
    now = datetime.now()
    for hour in list_of_hours:
        if now.hour <= hour:
            closest_hour = hour
    # calculate the time difference between closest_hour and now, then let the script sleep for this duration
    target_time = now.replace(hour=closest_hour, minute=0, second=0, microsecond=0)
    timediff = target_time - now
    print(datetime.now())
    time.sleep(timediff.total_seconds())
    print(datetime.now())


def crawl_legacy_content(scheduled_crawl_hours, timeframe):
    # TODO
    pass


if __name__ == "__main__":
    scheduled_crawl_hours = [6, 12, 18]
    while True:
        try:
            start_crawl()
            wait(scheduled_crawl_hours)
        except KeyboardInterrupt:
            logging.info("User terminated script")
            sys.exit(0) 
            pass