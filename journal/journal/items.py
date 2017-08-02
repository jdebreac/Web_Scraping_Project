# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JournalItem(scrapy.Item):
    type = scrapy.Field()	
    title = scrapy.Field()
    author = scrapy.Field()
    email = scrapy.Field()
    keyword = scrapy.Field()
    keyword2 = scrapy.Field()
    date = scrapy.Field()
#    number = scrapy.Field()
#    pass
