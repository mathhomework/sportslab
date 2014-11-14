# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from pymongo import Connection

class SportslabScrapePipeline(object):
    def process_item(self, item, spider):
        return item


# db = Connection(
#     host=getattr(settings, "MONGODB_HOST", None),
#     port=getattr(settings, "MONGODB_PORT", None)
# )[settings.MONGODB_DATABASE]
#
# if getattr(settings, "MONGODB_USERNAME", None):
#     db.authenticate(getattr(settings, "MONGODB_USERNAME", None), getattr(settings, "MONGODB_PASSWORD", None))


import pymongo

from scrapy.exceptions import DropItem
from scrapy.conf import settings
from scrapy import log


class MongoDBPipeline(object):
    def __init__(self):
        connection = pymongo.Connection(settings['MONGODB_HOST'], settings['MONGODB_PORT'])
        db = connection[settings['MONGODB_DATABASE']]
        self.collection = db[settings['MONGODB_COLLECTION']]

    def process_item(self, item, spider):
        valid = True
        for data in item:
            if not data:
                valid = False
                raise DropItem("Missing %s of blogpost from %s" %(data, item['url']))
        if valid:
            self.collection.insert(dict(item))
            log.msg("Item wrote to MongoDB database %s/%s" %
                (settings['MONGODB_DB'], settings['MONGODB_COLLECTION']),
                level=log.DEBUG, spider=spider)
        return item