# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 19:11:07 2018
功能：获取头条新闻、体育资讯等资料
接口：聚合数据api接口，可以根据 type_参数来调整获取的新闻类型
@author: mynumber
"""

from urllib.request import urlopen
from urllib.error import HTTPError,URLError
import json

class News(object):
    """浏览信息，可以读取新闻的标题，文本等内容"""
    def __init__(self):
        self.url='http://v.juhe.cn/toutiao/index?'
        self.key='97639d9aaa3e5c400df2dc57cb661d35'
    def get_news(self,type_='top'):
        """获取新闻，对获取的数据进行处理,默认情况下直接获取头条
        	 类型如下：top(头条，默认),shehui(社会),guonei(国内),
           guoji(国际),yule(娱乐),tiyu(体育)junshi(军事),keji(科技),
           caijing(财经),shishang(时尚)
        """
        url=self.url+'type='+type_+'&key='+self.key
        print(type_)
        try:
            html=urlopen(url).read().decode('utf-8')
            response=json.loads(html)
            print('成功获取新闻...')
            return response['result']['data']
        except HTTPError as e:
            print("HTTPError")
            print(e.code)
        except URLError as e:
            print("URLError")
            print(e.reason)
"""
#实例化对象，调用对象的get_news函数即可获取新闻
news=News()
#获得新闻是一个含有三十条新闻，可以根据不同的属性进行查看
n=news.get_news(type_='top')
print(n[0]['title'])
"""      