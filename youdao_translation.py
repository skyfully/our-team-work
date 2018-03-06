# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 16:18:31 2018
功能：实现翻译功能（可以自动检测语言类型）可以给出翻译的词性，英式发音，美式发音
      默认情况下，给出英文翻译出中文，给出汉语翻译成英语
接口：有道api 地址为http://openapi.youdao.com/api
实现：使用get方式向服务器发送信息，将获得的信息进行'utf-8'解码

@author: mynumber
"""
from urllib.request import  urlopen
from urllib import parse
from urllib.error import HTTPError,URLError
import hashlib
import random
import json

class youdao(object):
    def __init__(self):
        self.ID='74eb7e9d03323124'   #应用 ID
        self.key='g08NSmVWf3oAMnyvueToyj79yzhK95ri'#应用michi
        self.url='http://openapi.youdao.com/api'
    def translation(self,q=None):
        
        """将请求参数中的 appKey，翻译文本 q (注意为UTF-8编码)，随机数 salt 和
        密钥按照 appKey+q+salt+密钥 的顺序拼接得到字符串 str。
         对字符串 str 做md5，得到32位大写的 sign
         """
        if q is None:
            print('警告！！！请输入要翻译的内容...')
            return 
        fromLang='auto'
        toLang='auto'
        salt=random.randint(1,65536)
        sign=self.ID+q+str(salt)+self.key
        m1=hashlib.md5()
        m1.update(sign.encode('utf-8'))
        sign=m1.hexdigest()
        self.url=self.url+'?appKey='+self.ID+'&q='+parse.quote(q)+'&from='+fromLang+'&to='+toLang+'&salt='+str(salt)+'&sign='+sign
        try:
            response=urlopen(self.url)
            response=json.loads(response.read().decode('utf-8'))
            return response
        except HTTPError as e:
            print("HTTPError")
            print(e.code)
        except URLError as e:
            print("URLError")
            print(e.reason)
        
trans=youdao()
answer=trans.translation('卖国狗')
print('翻译结果为:%s'% answer['translation'])