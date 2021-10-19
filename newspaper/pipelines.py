# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import os
from urllib.parse import urlparse
from scrapy.pipelines.images import ImagesPipeline
import re


class NewspaperPipeline(ImagesPipeline):
    def file_path(self, request, response=None, info=None, *, item=None):
    # there are several solutions how to assign names to the images
    # solution 1: use the headline as name
        fileName = item['headline']
        # removes all special character from the filename
        fileName = re.sub('[^A-Za-z0-9 ]+', '', fileName)
        return fileName + ".jpg"
        
    # solution 2: use the original image name (sometimes it's a bit cryptic)
        # return os.path.basename(urlparse(request.url).path)
        
    # solution 3: use the built-in solution from scrapy which gives all images
        # a sha-1 hash (the path is saved in the json file for later assignment)
        # just change the pipeline in the settings.py 
