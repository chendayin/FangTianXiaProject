# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class NewHouseItem(scrapy.Item):
    # 省份
    province = scrapy.Field()
    # 城市
    city = scrapy.Field()
    # 小区名字
    name = scrapy.Field()
    # 价格
    price = scrapy.Field()
    # 几居
    rooms = scrapy.Field()
    # 地址
    address = scrapy.Field()
    # 行政区
    district = scrapy.Field()
    # 是否在售
    is_sale = scrapy.Field()
    # 详情页面 url
    orgin_url = scrapy.Field()


class OldHouseItem(scrapy.Item):
    # 省份
    province = scrapy.Field()
    # 城市
    city = scrapy.Field()
    # 小区名字
    name = scrapy.Field()
    # 几室几厅
    rooms = scrapy.Field()
    # 几层
    floor = scrapy.Field()
    # 朝向
    toward = scrapy.Field()
    # 年代
    year = scrapy.Field()
    # 地址
    address = scrapy.Field()
    # 建筑面积
    area = scrapy.Field()
    # 单价
    unit_price = scrapy.Field()
    # 总价
    total_price = scrapy.Field()
