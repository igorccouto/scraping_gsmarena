# -*- coding: utf-8 -*-
from scrapy import Spider
from scrapy.http import Request


class PhonesSpider(Spider):
    name = 'phones'
    allowed_domains = ['gsmarena.com']
    start_urls = ['https://gsmarena.com/makers.php3']

    def parse(self, response):
        brands = response.xpath('//div[@class="st-text"]//td')
        for brand in brands:
            url = brand.xpath('.//a/@href').extract_first()
            url_brand = response.urljoin(url)
            yield Request(url_brand,
                          callback=self.parse_brand)

    def parse_brand(self, response):
        url_phones_sel = './/div[@class="makers"]//li/a/@href'
        url_phones = response.xpath(url_phones_sel).extract()
        for url in url_phones:
            url_phone = response.urljoin(url)
            yield Request(url_phone,
                          callback=self.parse_phone)
        next_page = response.xpath('//div[@class="nav-pages"]')
        if next_page:
            next_page_sel = './/strong/following::a[1]/@href'
            next_page = next_page.xpath(next_page_sel).extract_first()
            url_next_page = response.urljoin(next_page)
            yield Request(url_next_page,
                          callback=self.parse_brand)

    def parse_phone(self, response):
        modelname_sel = '//*[@data-spec="modelname"]/text()'
        modelname = response.xpath(modelname_sel).extract_first()
        released_sel = '//*[@data-spec="released-hl"]/text()'
        released = response.xpath(released_sel).extract_first()
        body_sel = '//*[@data-spec="body-hl"]/text()'
        body = response.xpath(body_sel).extract_first()
        os_sel = '//*[@data-spec="os-hl"]/text()'
        os = response.xpath(os_sel).extract_first()
        storage_sel = '//*[@data-spec="storage-hl"]/text()'
        storage = response.xpath(storage_sel).extract_first()
        yield {'Model Name': modelname,
               'Released In': released,
               'Body': body,
               'OS': os,
               'Storage': storage}
