# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class IarcItem(scrapy.Item):
    code1 = scrapy.Field()
    code2 = scrapy.Field()
    code2_name = scrapy.Field()
    code3 = scrapy.Field()
    code3_name = scrapy.Field()
