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


from pymongo import Connection

from scrapy.exceptions import DropItem
from scrapy.conf import settings
from scrapy import log


class MongoDBPipeline(object):
    def __init__(self):
        connection = Connection(settings['MONGODB_HOST'], settings['MONGODB_PORT'])
        db = connection[settings['MONGODB_DATABASE']]
        self.collection = db[settings['MONGODB_COLLECTION']]
    def process_item(self, item, spider):
        self.collection.insert(dict(item))
        # log.msg("Item wrote to MongoDB database {}, collection {}, at host {}, port {}".format(
        #     settings['MONGODB_DATABASE'],
        #     settings['MONGODB_COLLECTION'],
        #     settings['MONGODB_HOST'],
        #     settings['MONGODB_PORT']))
        return item