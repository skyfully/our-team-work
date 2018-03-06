# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 19:35:09 2018
功能：获取笑话、内涵段子，可以根据pagesize的大小来调整一次获得的次数
实现：阿里云开放平台

@author: mynumber
"""

from urllib import request
from urllib.error import HTTPError,URLError
import json

class Joke(object):
    def __init__(self):
        """
        初始化数据key
        """
        self.AppKey='24773428'
        self.AppSecret='428a98ecaf930c7a0fd28d6d1e62e2fb'
        self.AppCode='1548b52c7a7e402ca82b6ff978996cd2'
        self.url='http://jisuxhdq.market.alicloudapi.com/xiaohua/text?'
    def get_joke(self,pagenum=1,pagesize=1,sort='rand'):
        querys='pagenum='+str(pagenum)+'&pagesize='+str(pagesize)+'&sort='+sort
        url=self.url+querys
        req=request.Request(url)
        req.add_header('Authorization', 'APPCODE ' + self.AppCode)
        try:
            response=request.urlopen(req)
            joke=response.read().decode('utf-8')
            joke=json.loads(joke)
            return  joke['result']['list']
        except HTTPError as e:
            print("HTTPError")
            print(e.code)
        except URLError as e:
            print("URLError")
            print(e.reason)
#调用方式
joke=Joke()
jokes=joke.get_joke(pagesize=2)
print(jokes)
            
        