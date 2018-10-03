# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html
from scrapy import Item, Field


class PhoneItem(Item):
    modelname = Field()
    released = Field()
    body = Field()
    os = Field()
    storage = Field()
