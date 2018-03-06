# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 15:41:49 2018

@author: mynumber
功能：实现语音到文本，使用者说出一句话，讲说出的话识别成对应的文字
接口：speech_recognition ,百度语音识别api
实现过程：1、利用speech_recognition进行录音（可以检测录音开始和结束位置），并将录音转化为采样频率为16000，wav的格式
         2、利用百度ResApi sdk 对 .wav格式的录音进行识别
         
接下来的工作：1、持续的输入输出
             2、不将录音写到本地，直接进行识别
"""
import speech_recognition as sr
import time
import sys
# 引入Speech SDK
from aip import AipSpeech   
import requests
import Netease
import get_news
KEY = '8edce3ce905a4c1dbb965e6b35c3834d' #这个key可以直接拿来用
KEY1='56e5e786796241e7a7c97d0a55414f27'
 
# 向api发送请求
def get_response(msg):
  apiUrl = 'http://www.tuling123.com/openapi/api'
  data = {
    'key'  : KEY1,
    'info'  : msg,
    'userid' : 'pth-robot',
  }
  try: 
    r = requests.post(apiUrl, data=data).json()
    print(r)
    return r.get('text')
  except:
    return
class speechRecognize(object):
    def __init__(self,):
        self._APP_ID = '10686210'
        self._API_KEY = 'dVPvuaXf7Zgr7iNVrXRBz390'
        self._SECRET_KEY = '764e77ae416d3510cb87cf4c8d7082ee'
        self.aipSpeech = AipSpeech(self._APP_ID, self._API_KEY, self._SECRET_KEY)
        self.r=sr.Recognizer()
    def record_voice(self):
        #从麦克风中获取音频
        with sr.Microphone() as source: 
            self.r.adjust_for_ambient_noise(source)
            print('请开始讲话...')
            audio=self.r.listen(source)
    
        #将音频写入WAV文件
        with open('speech1.wav','wb') as f:
            f.write(audio.get_wav_data(convert_rate=16000))
        self.start=time.time()
        print('ending say')
    def recognize_record(self):
        #识别转录之后的语音
        # 读取文件
        def get_file_content(filePath):
            with open(filePath, 'rb') as fp:
                return fp.read()
    # 识别本地文件 ，识别中文，可以通过修改’lan'属性进行调整识别的语言种类
        response=self.aipSpeech.asr(get_file_content('speech1.wav'), 'wav', 16000, {'lan': 'zh',}) 
        self.end=time.time()
        try:
            if response['result'] is not None:
                print(response['result'])
                print('运行时间：%s'%(self.end-self.start))
                return response['result']
        except:
            #print('ERROR 请检查错误格式')
            #print('说话内容为空或无法识别')
            return 
    
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
A=speechRecognize()
netmusic=Netease.NetEaseMusic()
news=get_news.News()
while True: 
   A.record_voice()
   msg=A.recognize_record()
   if msg is not None:
       if '播放' in msg[0]:
           speak('正在搜索中')
           print('音乐信息：%s'%msg[0])
           song=msg[0].split('播放')[1]
           netmusic.play_song(song)
       elif '退出系统' in msg[0]:
           print('即将退出系统')
           sys.exit(0)
       elif '新闻' in msg[0]:
           n=news.get_news(type_='top')
           speak(n[0]['title'])
           print(n[0]['title'])
       elif '暂停' in msg[0]:
           netmusic.pause_music()
       elif '继续' in msg[0]:
           netmusic.unpause_music()
       else :
           response=get_response(msg)
           netmusic.pause_music()
           speak(response)
           netmusic.unpause_music()
           
   time.sleep(0.1)
   
        