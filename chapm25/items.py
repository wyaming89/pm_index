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
    pm25=Field()
    pm25_index=Field()
    pm10=Field()
    pm10_index=Field()
    # define the fields for your item here like:
    # name = Field()

