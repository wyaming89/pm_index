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
    
    # def parse(self,response):
        # req=[]
        # hxs=HtmlXPathSelector(response)
        # #获取省级单位的链接
        # pro_url=hxs.select('//div/ul/li[@class="nav-header  "]/a/@href').extract()
        # for url in pro_url:
            # r=Request(url,callback=self.parse_city)
            # req.append(r)
        # return req

    # def parse_city(self, response):
        # hxs = HtmlXPathSelector(response)
        
        # req=[]
        # city_urls=[]
        # citys=['北京','上海','天津','重庆']
        # province=['福建','广东','河北','江苏','辽宁','山东','浙江']
        # hxs=HtmlXPathSelector(response)
        # #获取市级单位的链接
        # city=hxs.select('//div/ul[@class="nav nav-list"]/li[1]/a/text()').extract()
        # if city[0] in citys:
            # urls=hxs.select('//div/ul[@class"nav nav-list"]/li[1]/a/@href').extract()
            # city_urls.extend(urls)
        # elif city[0] in province:
            # urls=hxs.select('//ul[@class="nav nav-list"]/li[not(@class)]/a/@href').extract()
            # city_urls.extend(urls)
        # else:
            # urls=hxs.select('//ul[@class="nav nav-list"]/li[1]/a/@href').extract()
            # city_urls.extend(urls)
        # for url in city_urls:
            
            # r=Request(url,callback=self.parse_item)
            # req.append(r)
        # return req
        
    def parse_item(self, response):
        hxs = HtmlXPathSelector(response)
        chapm = chapm25Item()        
        chapm['staname']=hxs.select('//h2/div/div/a/text()').extract()
        
        chapm['pm25_rt'] = hxs.select('//table[@class="table table-hover"]/tbody/tr[1]/td[2]/text()').re('(\d+)')
        chapm['pm25_24'] = hxs.select('//table[@class="table table-hover"]/tbody/tr[1]/td[3]/text()').re('(\d+)')
        chapm['pm25_index_rt'] = hxs.select('//table[@class="table table-hover"]/tbody/tr[2]/td[2]/span/text()').re('(\d+)')
        chapm['pm25_index_24'] = hxs.select('//table[@class="table table-hover"]/tbody/tr[2]/td[3]/span/text()').re('(\d+)')
        chapm['pm10_rt']=hxs.select('//table[@class="table table-hover"]/tbody/tr[3]/td[2]/text()').re('(\d+)')
        chapm['pm10_24']=hxs.select('//table[@class="table table-hover"]/tbody/tr[3]/td[3]/text()').re('(\d+)')
        chapm['pm10_index_rt'] = hxs.select('//table[@class="table table-hover"]/tbody/tr[4]/td[2]/span/text()').re('(\d+)')
        chapm['pm10_index_24'] = hxs.select('//table[@class="table table-hover"]/tbody/tr[4]/td[3]/span/text()').re('(\d+)')
        #chapm['city']=hxs.select('//ul/li[@class="active"]/a/text()').extract()
        chapm['time'] = hxs.select('//footer').re('(\d+:\d+:\d+)')
        chapm['date'] = hxs.select('//footer').re('(\d+-\d+-\d+)')
        chapm['city']=hxs.select('//title').re('(\w+)PM2.5')
        
        return chapm
