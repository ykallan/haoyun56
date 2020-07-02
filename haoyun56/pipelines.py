# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
pymysql.install_as_MySQLdb()


class Haoyun56Pipeline(object):
    def __init__(self):
        self.conn = pymysql.Connect(
            host='localhost',
            port=3306,
            database='scrapy',
            user='root',
            passwd='root',
            charset='utf8',
        )

        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        self.conn.ping(reconnect=True)
        self.cursor.execute('''INSERT INTO haoyun56(title, gongxuleibie, gongxuzhuti, wuliutongdao, suoshufuwu, 
        suozaidiqu, xiangxidizhi, fabushijian, cont_name, mobile, telephone, fax, wechat, info, com_name) 
        VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)''',
                            (item['title'], item['gongxuleibie'], item['gongxuzhuti'], item['wuliutongdao'],
                             item['suoshufuwu'],item['suozaidiqu'], item['xiangxidizhi'], item['fabushijian'],
                             item['cont_name'],item['mobile'],
                             item['telephone'], item['fax'], item['wechat'], item['info'], item['com_name']
                             ))
        self.conn.commit()
        return item
        # item['title'] = title
        # item['gongxuleibie'] = gongxuleibie
        # item['gongxuzhuti'] = gongxuzhuti
        # item['wuliutongdao'] = wuliutongdao
        # item['suoshufuwu'] = suoshufuwu
        # item['suozaidiqu'] = suozaidiqu
        # item['xiangxidizhi'] = xiangxidizhi
        # item['fabushijian'] = fabushijian
        # item['cont_name'] = cont_name
        # item['mobile'] = mobile
        # item['telephone'] = telephone
        # item['fax'] = fax
        # item['wechat'] = wechat
        # item['info'] = info
        # item['com_name'] = com_name