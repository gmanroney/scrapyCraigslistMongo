# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field

class CraigslistItem(Item):
    # define the fields for your item here like:
    postUrl = Field()
    postDate = Field()
    postTitle = Field()
    postAddress = Field()
