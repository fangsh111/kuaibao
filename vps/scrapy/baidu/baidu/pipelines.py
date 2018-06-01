# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from baidu import settings
import pymongo


class BaiduPipeline(object):
    def open_spider(self, spider):
        ####链接mongodb数据库
        self.client = pymongo.MongoClient(host=settings.MONGO_HOST, port=settings.MONGO_PORT)
        self.db = self.client[settings.MONGO_DB_NAME]
        pass

    def process_item(self, item, spider):
        if item['top_num']:
            self.db['baidu_hot'].insert(dict(item))
        return item

    def close_spider(self, spider):
        self.client.close()
