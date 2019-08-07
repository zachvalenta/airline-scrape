# -*- coding: utf-8 -*-
from loguru import logger
import scrapy


class ExampleSpider(scrapy.Spider):
    name = 'example'
    selector = 'h1'


    def start_requests(self):
        urls = ['http://www.example.com']
        logger.debug('making request 🕷')
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)


    def parse(self, response):
        logger.debug('parsing request 🕷')
        els = response.css(self.selector)
        logger.debug(f'response {els}')
