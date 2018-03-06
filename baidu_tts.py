# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 19:32:55 2018
功能：两种文字转语音的方法
接口：百度api；pyttsx3
实现：百度api：先将要读的文字信息传给接口，并将获得信息进行存储，使用os模块进行播放
      pyttsx3：直接对文字信息进行读写，速度较快
@author: mynumber
"""

from aip  import AipSpeech


APP_ID = ' 10686953'
API_KEY = '3k0YmK4VTXqSb6zPpPatUqlN'
SECRET_KEY = 'f9b7683ae0c3a39f341b0d08793a2da4'
FILE_NAME1="F:/python_file/个人助理接口/voice1.mp3" 
FILE_NAME2="F:/python_file/个人助理接口/voice2.mp3"
speaker_client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

#将文字转换成语音，并存储
def wordsTowav(words,filename):
    result = speaker_client.synthesis(words, 'zh', 1, {'vol': 6,})
    if not isinstance(result, dict):
        with open(filename, 'wb') as f:
            f.write(result)
            f.close()
        return True
    else:
        return False
def Speak(words,filename):
    """播放语音文件""" 
    import pygame
    pygame.mixer.init()
    flag=wordsTowav(words,filename)
    if flag is True:
        pygame.mixer.music.load(filename)
        pygame.mixer.music.play()
        del pygame
        print('成功')
    else:
        print('失败')
        
#wordsTowav('你好',FILE_NAME2)
#调用演示
Speak('你好,我来自大连海事大学',FILE_NAME2)
"""       
#调用演示
start=time.time()
Speak('What is your name?') 
end=time.time()

import pyttsx3
engine=pyttsx3.init()
engine.say('What is your name?')
engine.runAndWait()     
""" 

  

        
        
        