# -*- coding: utf-8 -*-
import datetime
import re
import time

from scrapy import Item, Field
from scrapy.loader.processors import Join, MapCompose, Compose, TakeFirst

def filter_website_url(value):
    url = re.compile(u'\/biz_redir\?url=(.+)&website_link_type').search(value)
    if url:
        return str(url.group(1))
    return None

class YelpItem(Item):
    item_id = Field()
    store_biz_url = Field(input_processor=MapCompose(str.strip),
                         output_processor=Compose(Join(), str.strip))
    store_name = Field(input_processor=MapCompose(str.strip),
                         output_processor=Compose(TakeFirst(), str.strip))
    store_website_original = Field(input_processor=MapCompose(str.strip),
                         output_processor=Compose(Join(), str.strip, filter_website_url))
    store_website = Field(input_processor=MapCompose(str.strip),
                         output_processor=Compose(Join(), str.strip))
    email = Field()
    crawled_at = Field()
