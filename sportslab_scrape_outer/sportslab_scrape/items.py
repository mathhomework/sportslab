# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Item
from scrapy import Field

class SportslabScrapeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class PassingItem(Item):
    category = Field()
    jersey_number = Field()
    athlete_name = Field()
    school = Field()
    games_played = Field()
    passing_comp = Field()
    passing_att = Field()
    passing_yard = Field()
    completion_percentage = Field()
    yds_per_completion = Field()
    passing_yards_per_game = Field()
    completions_per_game = Field()
    passing_td = Field()
    passing_tds_per_game = Field()
    passing_int = Field()
    passing_long = Field()
    qb_rating = Field()


class RushingItem(Item):
    category = Field()
    jersey_number = Field()
    athlete_name = Field()
    school = Field()
    games_played = Field()
    rushing_num = Field()
    rushing_yards = Field()
    yards_per_carry = Field()
    rushing_yards_per_game = Field()
    rushing_long = Field()
    rushing_100plus = Field()
    rushing_tdnum = Field()


class ReceivingItem(Item):
    category = Field()
    jersey_number = Field()
    athlete_name = Field()
    school = Field()
    games_played = Field()
    receiving_num = Field()
    receiving_yards = Field()
    yards_per_catch = Field()
    receiving_yards_per_game = Field()
    receiving_long = Field()
    receiving_tdnum = Field()



