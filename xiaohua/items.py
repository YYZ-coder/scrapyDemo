# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class XiaohuaItem(scrapy.Item):
    # define the fields for your item here like:
    pic = scrapy.Field()
    name = scrapy.Field()

    # 大众点评额外字段
    address = scrapy.Field()
    # 店铺类型
    shopType = scrapy.Field()
    # 类目标签
    category = scrapy.Field()
    # 评分
    stars = scrapy.Field()
    # 店铺url
    url = scrapy.Field()

    # 总分店
    fullScore = scrapy.Field()
    # 评论数
    commentCount = scrapy.Field()
    # 团购优惠信息
    discount = scrapy.Field()
    # 城区
    area = scrapy.Field()
    # 街道
    street = scrapy.Field()
    pass


class ClassifyItem(scrapy.Item):
    url = scrapy.Field()
    name = scrapy.Field()
    categoryId = scrapy.Field()
    pass
