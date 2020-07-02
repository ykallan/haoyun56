# -*- coding: utf-8 -*-
import scrapy
import re
import pandas as pd
from ..items import Haoyun56Item


class HySpider(scrapy.Spider):
    name = 'hy'
    # allowed_domains = ['haoyun.com']
    start_urls = ['http://www.haoyun56.com/service/list_p1.html']
    base_url = 'http://www.haoyun56.com'

    def parse(self, response):
        lines = response.xpath('//div[@class="list_border"]//td/a[1]/@href').getall()
        for line in lines:
            # print(line)
            yield scrapy.Request(url=line, callback=self.parse_detail)

        next_page = response.xpath('//div[@align="right"]/a[last()-1]/@href').get()
        print(next_page)
        if next_page:
            yield scrapy.Request(url=self.base_url + next_page, callback=self.parse)

    def parse_detail(self, response):
        title = response.xpath('//h1/text()').get().strip()

        com_name = response.xpath('//div[@class="div_Head_right"]/div/div[2]/a[2]/text()').get()
        gongxuleibie = response.xpath('//div[@class="div_Head_left"]/div[1]/b/text()').get()
        gongxuzhuti = response.xpath('//div[@class="div_Head_left"]/div[2]').get()
        gongxuzhuti = re.findall(r'</span>(.*?)</div>', gongxuzhuti)[0]
        wuliutongdao = response.xpath('//div[@class="div_Head_left"]/div[3]').get()
        wuliutongdao = re.findall(r'</span>(.*?)</div>', wuliutongdao)[0]


        suoshufuwu = response.xpath('//div[@class="div_Head_left"]/div[4]').get()
        suoshufuwu = re.findall(r'</span>(.*?)</div>', suoshufuwu)[0]


        suozaidiqu = response.xpath('//div[@class="div_Head_left"]/div[5]').get()
        suozaidiqu = re.findall(r'</span>(.*?)</div>', suozaidiqu)[0]

        xiangxidizhi = response.xpath('//div[@class="div_Head_left"]/div[6]').get()
        xiangxidizhi = re.findall(r'</span>(.*?)</div>', xiangxidizhi)[0]

        fabushijian = response.xpath('//div[@class="div_Head_left"]/div[7]').get()
        fabushijian = re.findall(r'</span>(.*?)</div>', fabushijian)[0]
        table = pd.read_html(response.text)[2]
        cont_name = table[0][1][3:]
        print(cont_name)
        mobile = table[0][2][3:]
        telephone = table[0][3][3:]
        fax = table[0][4][3:]
        wechat = table[0][6][4:]
        infos = response.xpath('//div[@class="div_memo"]/text()').getall()
        info = ' '.join(infos)
        item = Haoyun56Item()
        item['title'] = title
        item['gongxuleibie'] = gongxuleibie
        item['gongxuzhuti'] = gongxuzhuti
        item['wuliutongdao'] = wuliutongdao
        item['suoshufuwu'] = suoshufuwu
        item['suozaidiqu'] = suozaidiqu
        item['xiangxidizhi'] = xiangxidizhi
        item['fabushijian'] = fabushijian
        item['cont_name'] = cont_name
        item['mobile'] = mobile
        item['telephone'] = telephone
        item['fax'] = fax
        item['wechat'] = wechat
        item['info'] = info
        item['com_name'] = com_name

        yield item
