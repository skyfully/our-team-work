# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 20:37:49 2018
功能：将一段文字(可以是汉字也可以是英文)读出来，即文字转语音
接口：win32com模块
实现过程：用户传入一段文字，将文字读出来

接下来的工作：
@author: mynumber
"""


import win32com.client  

"""
from win32com.client import gencache
gencache.EnsureModule('{C866CA3A-32F7-11D2-9602-00C04F8EE628}', 0, 5, 0)
"""
#声明win32com 语音模块的引用，实例化发言人（speaker）
def speak(words=None):
    try:
        speaker = win32com.client.Dispatch("SAPI.SPVOICE") 
        speaker.Speak(words)
    except:
        print('Error: 实例化失败 请检查是否设置好--IID{269316D8-57BD-11D2-9EEE-00C04F797396}')
#调用如下
#words='我喜欢English,it is interesting!'
#speak(words)