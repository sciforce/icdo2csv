# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import csv


class IarcPipeline(object):
    def open_spider(self, spider):
        self.file = open("items.csv", "w")
        self.csv = csv.DictWriter(self.file, ('code1', 'code2', 'code2_name', 'code3', 'code3_name'))

    def process_item(self, item, spider):
        self.csv.writerow(item)
        return item

    def close_spider(self, spider):
        self.file.close()
