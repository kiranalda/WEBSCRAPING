# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class QuotesItem(scrapy.Item):
    text = scrapy.Field()
    author = scrapy.Field()
    tags = scrapy.Field()
    #last_upd_time = scrapy.Field()


class ScrapyprojectItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
