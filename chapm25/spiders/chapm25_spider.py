# -*- coding: utf-8 -*-
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from chapm25.items import chapm25Item
from scrapy.http import Request
import codecs

class Chapm25Spider(CrawlSpider):
    name = 'chapm25'
    allowed_domains = ['chapm25.com']
    start_urls = ['http://www.chapm25.com/']
    
    rules = (
        Rule(SgmlLinkExtractor(
                allow="www.chapm25.com/city",
                #restrict_xpaths='//ul[@class="nav val-list"]'
                ), 
            callback='parse_item', 
            follow=True),
    )
       
    def parse_item(self, response):
        hxs = HtmlXPathSelector(response)
                
        staname = hxs.select('//h2/div/div/a/text()').extract()
        pm25_rt = hxs.select('//table[@class="table table-hover"]/tbody/tr[1]/td[2]/text()').re('(\d+)')
        pm25_24 = hxs.select('//table[@class="table table-hover"]/tbody/tr[1]/td[3]/text()').re('(\d+)')
        pm25_index_rt = hxs.select('//table[@class="table table-hover"]/tbody/tr[2]/td[2]/span/text()').re('(\d+)')
        pm25_index_24 = hxs.select('//table[@class="table table-hover"]/tbody/tr[2]/td[3]/span/text()').re('(\d+)')
        pm10_rt=hxs.select('//table[@class="table table-hover"]/tbody/tr[3]/td[2]/text()').re('(\d+)')
        pm10_24=hxs.select('//table[@class="table table-hover"]/tbody/tr[3]/td[3]/text()').re('(\d+)')
        pm10_index_rt = hxs.select('//table[@class="table table-hover"]/tbody/tr[4]/td[2]/span/text()').re('(\d+)')
        pm10_index_24 = hxs.select('//table[@class="table table-hover"]/tbody/tr[4]/td[3]/span/text()').re('(\d+)')  
        time = hxs.select('//footer').re('(\d+:\d+:\d+)')
        date = hxs.select('//footer').re('(\d+-\d+-\d+)')
        city=hxs.select('//title').re('(\w+)PM2.5')
        items = []
        for i  in range(len(staname)):
            
            chapm = chapm25Item()
            chapm['staname'] = staname[i]
            chapm['pm25_rt'] = pm25_rt[i]
            chapm['pm25_24'] = pm25_24[i]
            chapm['pm25_index_rt'] = pm25_index_rt[i]
            chapm['pm25_index_24'] = pm25_index_24[i]
            chapm['pm10_rt'] = pm10_rt[i]
            chapm['pm10_24'] = pm10_24[i]
            chapm['pm10_index_rt'] = pm10_index_rt[i]
            chapm['pm10_index_24'] = pm10_index_24[i]
            
            chapm['time'] = time
            chapm['date'] = date
            chapm['city']=city
            items.append(chapm)
        return items
