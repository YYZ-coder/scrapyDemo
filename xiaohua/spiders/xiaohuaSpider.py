
import scrapy
import os
# 导入item中结构化数据模板
from xiaohua.items import XiaohuaItem, ClassifyItem
import logging
import copy

config = {
    "filename": 'D:\\workSpace\\PyWorkspace\\xiaohua\\myapp.log',
    "filemode": 'w',
    "format": "%(message)s"
}

logging.basicConfig(**config)


def parse_all_shops(response):
    # 获取所有图片的a标签
    shops = response.xpath('//div[@class="shopsearch"]/div[@class"content"]ul/li')
    logging.debug(shops)
    for shop in shops:
        logging.debug("=============================")
        logging.debug(shop.decode("gbk").encode("utf-8"))
        # 分别处理每个图片，取出名称及地址
        item = XiaohuaItem()
        # 店铺名
        name = shop.xpath('./div[@class="pic"]/a/img/@alt').extract()[0]
        # 店铺图片url
        picUrl = shop.xpath('./div[@class="pic"]/a/img/@src').extract()[0]
        # 店铺url
        url = shop.xpath('./div[@class="pic"]/a/@href').extract()[0]
        # 店铺地址
        address = shop.xpath('./div[@class="txt"]/div[@class="tag-addr"]/span/text()').extract()[0]
        item['name'] = name
        item['pic'] = picUrl
        item['url'] = url
        item['address'] = address
        logging.debug(item)
        logging.debug("=============================")
        # 返回爬取到的数据
        yield item


class XhSpider(scrapy.Spider):
    # 爬虫名称，唯一
    name = "xh"
    # 允许访问的域
    allowed_domains = ["dianping.com"]
    # 初始URL
    start_urls = ['http://www.dianping.com/shenzhen/ch90']

    # 解析所有区域
    # def parse_all_area(self, response):
    #     areas = response.xpath('//div[@class="shopsearch"]/div[@class"type"][2]/div[@class"content"]/ul/li')
    #     for area in areas:
    #

    # 解析所有店铺

    def parse(self, response):
        classifies = response.xpath('//div[@class="shopsearch"]/div[@class="type"][2]/div[@class="content"]/ul/li')
        logging.debug(classifies)
        for classify in classifies:
            logging.debug(classify)
            item = ClassifyItem()
            name = classify.xpath('./a/text()').extract()[0]
            url = classify.xpath('./a/@href').extract()[0]
            categoryId = classify.xpath('./a/@data-extend').extract()[0]
            item['name'] = name
            item['url'] = url
            item['categoryId'] = categoryId
            logging.debug(item)

        # self.parse_all_area(response)

        # 解析店铺信息
        # self.pares_all_shops(shopsParse)

