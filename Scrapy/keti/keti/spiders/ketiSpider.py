# -*- coding: utf-8 -*-
import scrapy
import requests
from lxml import etree
from scrapy.http import Request
from scrapy.selector import Selector
from keti.items import InformationItem
import time

class KETI(scrapy.Spider):
    name = "keti"
    redis_key = 'keti:start_urls'
    start_urls = ['http://xa.58.com/chuzu/0/', 'http://xa.58.com/chuzu/1/']

    def parse(self, response):
        item = InformationItem()
        selector = Selector(response)
        sites = selector.xpath('//ul[@class="listUl"]')

        def clean_spaces(s):
            s = s.replace(' ', '')
            s = s.replace('\n', '')
            s = s.replace('\r', '')
            s = s.replace('\t', ' ')
            s = s.replace('\f', ' ')

            return s

        for site in sites:
            titles = [a.strip() for a in site.xpath('li/div[2]/h2/a/text()').extract() if len(clean_spaces(a)) > 0]     # 标题：此写法无需调用其它函数
            areas = site.xpath('li/div[2]/p[1]/text()').extract()                                                       # 面积
            address = site.xpath('li/div[2]/p[2]/a[1]/text()').extract()                                                # 地址
            moneys = site.xpath('li/div[3]/div[2]/b/text()').extract()                                                  # 价钱

            for (title, area, add, money) in zip(titles, areas, address, moneys):

                item['title'] = title
                item['area'] = clean_spaces(area)
                item['address'] = add
                item['money'] = money
                yield item

            next_page = selector.xpath('//a[@class="next"]/@href').extract()
            time.sleep(1)
            if next_page:
                next_page = next_page[0]
                yield Request(next_page, callback=self.parse)

        new_url = 'http://xa.58.com/pinpaigongyu/'
        yield Request(new_url, callback=self.pingpai)

    def pingpai(self, response):
        selector = Selector(response)
        sites = selector.xpath('//ul[@class="list"]')
        def clean_spaces(s):
            s = s.replace(' ', '')
            s = s.replace('\n', '')
            s = s.replace('\r', '')
            s = s.replace('\t', ' ')
            s = s.replace('\f', ' ')

            return s

        def open_url(url):
            headers = {
                'Server': 'Tengine',
                'Content-Type': 'text/html; charset=UTF-8',
                'Connection': 'keep-alive',
                'Vary': 'Accept-Encoding',
                'X-Powered-By': 'PHP/5.6.20',
                'Content-Encoding': 'gzip',
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
            }
            req = requests.get(url, headers=headers)
            req.encoding = 'utf-8'
            new_selector = etree.HTML(req.text)

            return new_selector

        def new_address(url):
            address = []
            for i in url:
                new_selector = open_url('http://xa.58.com' + i)
                address_1 = ''.join(new_selector.xpath('//ul[@class="house-info-list"]/li[4]/span/text()'))
                address_2 = ''.join(new_selector.xpath('//div[@class="detail detailAddress"]/span/text()'))
                if len(address_1) > 0:
                    address.append(address_1)
                elif len(address_2) > 0:
                    address.append(address_2)
                else:
                    address.append('http://xa.58.com' + i)

            return address

        def str_address(str_title):
            num = 0
            for i in str_title:
                if i == ' ':
                    ss = num
                    break
                num += 1
            return ss

        for site in sites:
            item = InformationItem()
            titles = site.xpath('li/a/div[2]/h2/text()').extract()  # 标题
            areas = [a.strip() for a in site.xpath('li/a//div[2]/p[1]/text()').extract() if len(clean_spaces(a)) > 0]  # 面积
            moneys = site.xpath('li/a/div[3]/span/b/text()').extract()  # 价格
            #address_url = site.xpath('li/a/@href').extract()  # 目标页面url
            #time.sleep(1)
            #address = new_address(address_url)
            #time.sleep(1)
            '''
            for (title, area, add, money) in zip(titles, areas, address, moneys):
                item['title'] = title
                item['area'] = clean_spaces(area)
                item['address'] = add
                item['money'] = money
                time.sleep(0.5)
                yield item
            '''

            for (title, area, money) in zip(titles, areas, moneys):
                item['title'] = title
                item['area'] = clean_spaces(area)
                item['address'] = title[4:str_address(title)]
                item['money'] = money
                yield item

            next_page = selector.xpath('//a[@class="next"]/@href').extract()
            next_page = 'http://xa.58.com' + next_page[0]
            next_pages = []
            next_pages.append(next_page)
            time.sleep(1)
            if next_pages:
                next_pages = next_pages[0]
                yield Request(next_pages, callback=self.pingpai)







