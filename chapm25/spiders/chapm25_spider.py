#coding=gbk
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from chapm25.items import chapm25Item

class chapm25Spider(BaseSpider):
    name = "chapm25"
    allowed_domains = ["chapm25.com"]
    start_urls = [
        "http://www.chapm25.com/"
        
]    
  
    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        
        chapm=chapm25Item()
        chapm['staname']=hxs.select('//h2/div/div/a/text()').extract()
        chapm['pm25']=hxs.select('//table[@class="table table-hover"]/tbody/tr[1]/td/text()').extract()
        chapm['pm10']=hxs.select('//table[@class="table table-hover"]/tbody/tr[3]/td/text()').extract()
        chapm['city']=hxs.select('//ul/li[@class="active"]/a/text()').extract()
        chapm['pm25_index']=hxs.select('//table[@class="table table-hover"]/tbody/tr[2]/td/span/text()').extract()
        chapm['pm10_index']=hxs.select('//table[@class="table table-hover"]/tbody/tr[4]/td/span/text()').extract()
        return chapm
