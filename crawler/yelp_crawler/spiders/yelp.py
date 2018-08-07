# -*- coding: utf-8 -*-

from scrapy import Selector, Request
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from scrapy.spiders import Rule, CrawlSpider

from yelp_crawler.items import YelpItem
from urllib.parse import unquote


class YelpSpider(CrawlSpider):
    name = 'yelp'
    # start_urls = ['https://www.yelp.com/search?find_desc=hair+salons&find_loc=Toronto,+Ontario,+Canada&start=0']
    # start_urls = ['https://www.yelp.com/search?find_desc=salon&find_loc=New+York,+NY&start=0']
    start_urls = ['https://www.yelp.com/search?find_desc=salon&find_loc=San+Francisco,+CA&start=0']
    # start_urls = ['https://www.yelp.com/search?find_desc=salon&find_loc=Seattle,+WA&start=0']
    # start_urls = ['https://www.yelp.com/search?find_desc=Hair+Salons&find_loc=Oregon+City,+OR&start=0']

    rules = (
        Rule(LinkExtractor(allow=r'/search?.*$',
                            restrict_css=('div#super-container li.regular-search-result', 'div#super-container div.search-pagination')),
            follow=True),
        Rule(LinkExtractor(allow=r'/biz/.*$'), callback='parse_biz'),
    )

    def parse_biz(self, response):
        self.logger.debug('==============parse_biz response==============')
        selector = Selector(response=response)
        selector.css('div#wrap div.top-shelf')

        item_loader = ItemLoader(item=YelpItem(), selector=selector, response=response)
        item_loader.add_css(field_name='store_name', css='h1.biz-page-title::text')
        item_loader.add_css(field_name='store_website_original', css='li span.biz-website a::attr(href)')
        item_loader.add_value(field_name='store_biz_url', value=response.url)

        instanced_item = item_loader.load_item()
        
        website_link = instanced_item.get('store_website_original')
        store_name = instanced_item.get('store_name')
        store_biz_url = instanced_item.get('store_biz_url')
        self.logger.debug('==============store_website_original start==============')
        self.logger.debug(website_link)
        self.logger.debug(instanced_item.items())
        self.logger.debug('==============store_website_original end==============')
        if website_link is not None:
            yield Request(unquote(website_link, 'utf-8'),
                            callback=self.parse_website,
                            meta={'store_name': store_name, 'store_biz_url': store_biz_url})

    def parse_website(self, response):
        self.logger.debug('==============parse_website response==============')
        self.logger.debug('==============parse_website response meta start==============')
        self.logger.debug(response.meta)
        self.logger.debug('==============parse_website response meta end==============')
        selector = Selector(response=response)
        selector.xpath('.')

        item_loader = ItemLoader(item=YelpItem(), selector=selector, response=response)
        item_loader.add_value(field_name='store_name', value=response.meta.get('store_name', None))
        item_loader.add_value(field_name='store_biz_url', value=response.meta.get('store_biz_url', None))
        item_loader.add_value(field_name='store_website', value=response.url)
        item_loader.add_xpath('email', '//a[contains(@href, "mailto:")]/text()')

        instanced_item = item_loader.load_item()
        self.logger.debug('==============parse_website item_loader start==============')
        self.logger.debug(instanced_item)
        self.logger.debug('==============parse_website item_loader end==============')
        yield instanced_item
        # yield item_loader.load_item()
