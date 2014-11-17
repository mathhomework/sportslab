# -*- coding: utf-8 -*-

# Scrapy settings for sportslab_scrape_outer project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'sportslab_scrape_outer'

SPIDER_MODULES = ['sportslab_scrape.spiders']
NEWSPIDER_MODULE = 'sportslab_scrape.spiders'

ITEM_PIPELINES = {'sportslab_scrape.pipelines.MongoDBPipeline':300}

# local settings

# MONGODB_HOST = 'localhost' # Change in prod
# MONGODB_PORT = 27017 # Change in prod
# MONGODB_DATABASE = "training" # Change in prod
# MONGODB_COLLECTION = "sportslab"
# MONGODB_USERNAME = "" # Change in prod
# MONGODB_PASSWORD = "" # Change in prod


#mongo labs!!
MONGODB_HOST = 'mongodb://andrew:hotdog@ds053190.mongolab.com:53190/sportslab_mongodb' # Change in prod
MONGODB_PORT = 53190 # Change in prod
MONGODB_DATABASE = "sportslab_mongodb" # Change in prod
MONGODB_COLLECTION = "sportslab"




# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'sportslab_scrape_outer (+http://www.yourdomain.com)'
