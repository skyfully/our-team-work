# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 18:21:58 2018
功能：实现语音到文本，使用者说出一句话，讲说出的话识别成对应的文字
接口：speech_recognition ,百度语音识别api
实现过程：1、利用speech_recognition进行录音（可以检测录音开始和结束位置），并将录音转化为采样频率为16000，wav的格式
         2、利用百度ResApi sdk 对 .wav格式的录音进行识别
         
接下来的工作：1、持续的输入输出
             2、不将录音写到本地，直接进行识别

@author: mynumber
"""
import speech_recognition as sr
import time
# 引入Speech SDK
from aip import AipSpeech   
r=sr.Recognizer()
#从麦克风中获取音频
with sr.Microphone() as source:
    # 
    r.adjust_for_ambient_noise(source)
    print('请开始讲话...')
    audio=r.listen(source)
    
#将音频写入WAV文件
with open('speech1.wav','wb') as f:
    f.write(audio.get_wav_data(convert_rate=16000))
start=time.time()    


# 百度语音识别 相关包信息
APP_ID = '10686210'
API_KEY = 'dVPvuaXf7Zgr7iNVrXRBz390'
SECRET_KEY = '764e77ae416d3510cb87cf4c8d7082ee'
# 初始化AipSpeech对象
aipSpeech = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
# 读取文件
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()
    
# 识别本地文件 ，识别中文，可以通过修改’lan'属性进行调整识别的语言种类
response=aipSpeech.asr(get_file_content('speech1.wav'), 'wav', 16000, {'lan': 'zh',}) 
end=time.time()
try:
    print(response['result'])
    print('运行时间：%s'%(end-start))
except:
    print('ERROR 请检查错误格式')

