# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class chapm25Item(Item):
    date = Field()
    time = Field()
    city = Field()
    staname=Field()
    pm25_rt=Field()
    pm25_24=Field()
    pm25_index_rt=Field()
    pm25_index_24=Field()
    pm10_rt=Field()
    pm10_24=Field()
    pm10_index_rt=Field()
    pm10_index_24=Field()
    # define the fields for your item here like:
    # name = Field()

