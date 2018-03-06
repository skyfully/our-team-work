# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 10:42:29 2018
功能：实现对每个好友聊天，输出该好友的聊天内容

@author: mynumber
"""

import wxpy

#
bot=wxpy.Bot(cache_path=True)   
global my_friend

def set_friend(name='老关'):
    friend=bot.friends().search(name)
    if len(friend) == 0:
        print('未找到好友,请重新输入姓名或昵称...')
    else:
        return friend[0]
def send(friend,message=None):
    if friend is not None:
        friend.send(message)
        print('成功发送...')
    else:
        print('无此好友,请选择真正的好友...')

#调用如下        
my_friend=set_friend('老关')
send(my_friend,'hello')

#可以返回好友的聊天记录
@bot.register(my_friend)
def print_others(msg):
    print(msg)

    
