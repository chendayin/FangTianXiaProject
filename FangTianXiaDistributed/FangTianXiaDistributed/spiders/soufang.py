# -*- coding: utf-8 -*-
import scrapy
import re

from FangTianXiaDistributed.items import OldHouseItem, NewHouseItem
from scrapy_redis.spiders import RedisSpider

class SoufangSpider(RedisSpider):
    name = 'soufang'
    allowed_domains = ['fang.com']
    # start_urls = ['http://www.fang.com/SoufunFamily.htm']
    redis_key = 'soufang'
    def parse(self, response):
        trs = response.xpath("//div[@id='c02']//tr")
        province = None
        for tr in trs:
            tds = tr.xpath(".//td[not(@class)]")
            province_td = tds[0].xpath(".//text()").get().strip()
            if province_td:
                province = province_td
            city_links = tds[1].xpath(".//a")
            # 不需要爬取国外的
            if province == '其它':
                continue
            for city_link in city_links:
                city_name = city_link.xpath(".//text()").get()
                city_url = city_link.xpath(".//@href").get()
                scheme, domain = city_url.split("//")
                # 北京的新房和二手房链接需要特别处理
                if 'bj.' in domain:
                    newHouseLink = 'http://newhouse.fang.com/house/s'
                    oldHouseLink = 'http://esf.fang.com/'
                else:
                    newHouseLink = scheme + "//" + "newhouse." + domain + "house/s"
                    oldHouseLink = scheme + "//" + "esf." + domain

                yield scrapy.Request(url=newHouseLink, callback=self.parse_newhouse,
                                     meta={'info': (province, city_name)})

                yield scrapy.Request(url=oldHouseLink, callback=self.parse_oldhouse,
                                     meta={'info': (province, city_name)})

    def parse_newhouse(self, response):
        province, city = response.meta.get("info")
        lis = response.xpath(".//div[contains(@class,'nl_con')]/ul//li")
        for li in lis:
            # 房子的名称
            name = li.xpath(".//div[@class='nlcd_name']//text()").getall()
            if name:
                name = re.sub(r'[\s\n]', '', ''.join(name))
                # 价格
                price = li.xpath(".//div[@class='nhouse_price']//text()").getall()
                price = re.sub(r'[\s\n广告]', '', ''.join(price))
                # 居式
                rooms = li.xpath(".//div[contains(@class,'house_type')]//text()").getall()
                rooms = re.sub('－', '一共', re.sub(r'[\s\n]', '', ''.join(rooms)))
                # 地址
                address = li.xpath('.//div[@class="address"]/a/@title').get()
                address = re.sub(r'\[.+\]', '', address)
                # 地区
                district = li.xpath(".//div[@class='address']//text()").getall()
                try:
                    district = re.search(r'(\[.+\])', ''.join(district)).group(1)
                except:
                    district = ''
                # 是否在售
                is_sale = li.xpath(".//div[contains(@class,'fangyuan')]/span/text()").get()
                # 房源的链接
                orgin_url = response.urljoin(li.xpath(".//div[@class='nlcd_name']/a/@href").get())

                items = NewHouseItem(province=province, city=city, name=name, price=price, rooms=rooms, address=address,
                                     district=district,
                                     is_sale=is_sale, orgin_url=orgin_url)
                yield items

        next_url = response.xpath("//div[@class='page']//a[@class='next']/@href").get()
        if next_url:
            next_url = response.urljoin(next_url)
            yield scrapy.Request(next_url, callback=self.parse_newhouse, meta={'info': (province, city)})

    def parse_oldhouse(self, response):
        province, city = response.meta.get("info")
        lis = response.xpath("//div[contains(@class,'shop_list')]//dl[@dataflag='bg']")

        for li in lis:
            try:
                name = li.xpath(".//p[@class='add_shop']/a/@title").get()
                address = li.xpath(".//p[@class='add_shop']//span/text()").get()
                house_info = li.xpath(".//p[@class='tel_shop']//text()").getall()
                house_info = ''.join(house_info).split('|')
                house_info = list(map(lambda x: re.sub(r'[\r\n\s]', '', x), house_info))
                rooms, areas, floor, toward, year, *ags = house_info
                unit_price = li.xpath(".//dd[@class='price_right']/span[not(@class)]/text()").get()
                total_price = li.xpath(".//dd[@class='price_right']/span[@class='red']//text()").getall()
                total_price = ''.join(total_price)
                item = OldHouseItem(province=province, city=city, name=name, address=address, rooms=rooms, floor=floor,
                                    toward=toward, year=year, area=areas, unit_price=unit_price,
                                    total_price=total_price)
                yield item
            except:
                continue

        next_url = response.xpath("//div[@class='page_al']//span/following-sibling::p//a[text()='下一页']/@href").get()
        if next_url:
            yield scrapy.Request(response.urljoin(next_url), callback=self.parse_oldhouse,
                                 meta={'info': (province, city)})
