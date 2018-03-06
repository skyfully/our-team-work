# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 21:01:15 2018
功能：实现天气查询的功能
接口:阿里天气api
实现方式：GET方式
@author: mynumber
"""

from urllib import request,parse
from urllib.error import HTTPError,URLError
import json


class Weather(object):
    def __init__(self):
        self.Appcode='1548b52c7a7e402ca82b6ff978996cd2'
        self.url='http://jisutqybmf.market.alicloudapi.com/weather/query?'
    def get_weather(self,**kwds):
        querys=parse.urlencode(kwds)
        url=self.url+querys+'&citycode=citycode&cityid=cityid&ip=ip&location=location'
        req=request.Request(url)
        req.add_header('Authorization', 'APPCODE ' + self.Appcode)
        try:
            response=request.urlopen(req)
            weather=json.loads(response.read().decode('utf-8'))
            return  weather['result']
        except HTTPError as e:
            print("HTTPError")
            print(e.code)
        except URLError as e:
            print("URLError")
            print(e.reason)
            
#调用  
wea=Weather()
weather=wea.get_weather(city='大连')