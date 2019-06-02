import scrapy

from tutorial.items import DmozlItem

class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ['dmoz.org']
    start_urls = [
        'http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/',
        'http://www.dmoz.org/Computers/Programming/Languages/Python/Books/'
        ]

    def parse(self, response):
        sel = scrapy.selector.Selector(response)
        sites = sel.xpath('//div/div/div[@class="title-and-desc"]')
        items = []
        for site in sites:
            item = DmozlItem()
            item['title'] = site.xpath('a/div/text()').extract()
            item['link'] = site.xpath('a/@href').extract()
            item['desc'] = site.xpath('div/text()').extract()
            items.append(item)

        return items
            

        
