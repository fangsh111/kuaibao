# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
import datetime


class Baidu_hot_Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    top_num = scrapy.Field()
    title = scrapy.Field()
    link = scrapy.Field()
    new_link = scrapy.Field()
    video_link = scrapy.Field()
    image_link = scrapy.Field()
    hot_value = scrapy.Field()
    create_timed = scrapy.Field()
    update_timed = scrapy.Field()
