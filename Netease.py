# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 09:45:45 2018
功能： 网易云音乐接口，可以获取某个音乐的评论，下载音乐，查询歌手的信息,批量下载某个歌手的音乐等等
      提供用户名，可以查看用户的歌单等信息
接口：MusicBoxApi、download_music、pygame
实现过程：下载歌曲：先使用get_songsID获得歌曲的ID号等信息，再使用函数download_music 进行下载
         获取歌曲评论：根据歌曲ID号 使用get_comments 获取hotcomment和一般comment
         播放音乐使用的是pygame模块
        
接下来的工作：实现登录网易云音乐，获取用户的云端信息
@author: mynumber
"""
from MusicBoxApi import api  as NetEaseApi
import download_music 
import pygame

class NetEaseMusic(object):
    def __init__(self):
        self.netease=NetEaseApi.NetEase() 
        pygame.mixer.init()
        self.volume=0.3
        pygame.mixer.music.set_volume(self.volume)
        self.download_path='music\\'
    def get_artist(self,artist_name):
        #获取歌手的详细信息
        artists_message=self.netease.search(artist_name,stype=100)
        try: 
            #对搜索结果进行查询，找到真正的歌手
            artists=artists_message['result']['artists']
            namelist=[artists[i]['name'] for i in range(len(artists))]
            if artist_name in namelist:
                ind=namelist.index(artist_name)
            return artists[ind]
        except :
            print('错误信息,请重新检查歌手信息...')
        
    def get_songsMessage(self,song_name):
        #获取歌曲的信息，如歌手信息，唱片信息，及获得唱过该歌的歌手信息
        try:
            songs_message=self.netease.search(song_name,stype=1)['result']['songs']
            #songs_ID=[songs_message[i]['id'] for i in range(len(songs_message))]
            return songs_message
        except:
            print('错误信息,请重新检查歌曲信息...')    
    def get_comments(self,songID,hotcomments=True):
        #提供歌曲ID号，获取该歌的评论
        comments=self.netease.song_comments(songID)
        if comments['total'] is 0:
            print('歌曲号错误,请重新输入....')
            return 
        else:
            try:
                if hotcomments == True:
                    hcomments=[comment['content']  for comment in comments['hotComments']]
                    return hcomments
                else:
                    Tcomments=[comment['content']  for comment in comments['comments']]
                    return Tcomments
            except :
                print('信息错误,请检查原因...')
            
    def get_artist_songs(self,artist_name):
        #获得某个歌手的所有歌曲ID号码,和对应的歌名
        artistID=self.get_artist(artist_name)['id']
        try:
            artists_songs=self.netease.artists(artistID)
            songsID,songname=[song['id'] for song in artists_songs],[song['name'] for song in artists_songs]
            print('查找歌曲成功,共找到%s首歌曲'%(len(songsID)))
            return songsID,songname
        except:
            print('获取歌手的歌曲单失败...')
            return 
    def get_userMessage(self,use_name='fxcgvc'):
        #查询用户的信息，获得用户的详情,免登陆
        user_list=self.netease.search(s=use_name,stype=1002)
        try:
            for user in user_list['result']['userprofiles']:
                if user['nickname'] ==use_name:
                    print('已找到用户信息...')
                    return user
        except:
            print('查找失败,请检查用户名...')
    def get_user_playlist(self,username='fxcgcv'):
        #获取用户的播放列表，歌单信息等等
        userID=self.get_userMessage(username)['userId']
        try:
             
            userplaylist=self.netease.user_playlist(userID)  
            print('歌单查找成功...')
            return userplaylist
        except:
            print('歌单查找失败')
    def get_detail_playlist(self,playlistID):
        #获取歌单的详情信息
        playlist=self.netease.playlist_detail(playlistID)
        if playlist is not None:
            print('查找歌单成功...')
            return playlist
        else:
            print('查找失败,请检查歌单id...')
    
    def find_song(self,songname='演员',artist_name='薛之谦',album_name=None):
        #精确匹配，提供歌手的姓名和歌的名字
        songs_message=self.get_songsMessage(songname)
        if album_name is None:
            for song in songs_message:
                if song['name']==songname and artist_name==song['artists'][0]['name'] :
                    print('已为您详细匹配到歌曲...')
                    return [song]
            
        else:   
            for song in songs_message:
                if song['name']==songname and artist_name==song['artists'][0]['name'] and song['album']['name']==album_name:
                    print('已为您详细匹配到歌曲...')
                    return [song]
        
        print('未找到您想要的歌...')
    def play_song(self,songname='演员'):
        #播放歌曲，先查看本地是否有这首歌，没有的话先找到歌的ID，然后下载到本地，最后进行播放
        download_path=self.download_path+songname+'.mp3'
        try:
            pygame.mixer.music.load(download_path)
            pygame.mixer.music.play()
            print('已在本地找到歌曲,即将为您播放...')
        except:
            print('未在本地找到歌曲,正在尝试从互联网寻找...')
            try:
                songs=self.get_songsMessage(songname)
                
                for song in songs:
                    Flag=download_music.download(song['id'],download_path)
                    if Flag is True:
                        print('歌曲下载成功...\n即将为您播放...')
                        break
                
                pygame.mixer.music.load(download_path)
                pygame.mixer.music.play()
            except:
                print('未找到想要的歌...')
            
    def stop_music(self):
        #停止音乐的播放
        pygame.mixer.music.stop()
    def pause_music(self):
        #暂停播放
        pygame.mixer.music.pause()
    def unpause_music(self):
        #取消暂停
        pygame.mixer.music.unpause() 
    def set_volume(self):
        self.volume+=0.1
        pygame.mixer.music.set_volume(self.volume)         
    def batch_download(self,songsID,songName,songartist=None):
        #批量下载歌曲
        if len(songartist) ==0:
            for ID,Name in zip(songsID,songName):
                print('music\\'+Name+'.mp3')
                download_music.download(ID,'music\\'+Name+'.mp3')  
        else:
            for ID,Name,artist in zip(songsID,songName,songartist):
                print('music\\'+Name+'.mp3')
                download_music.download(ID,'music\\'+Name+' '+artist+'.mp3')
#调用
"""        

netmusic=NetEaseMusic()
netmusic.play_song('我爱你')
songs_name='演员'  
artist_name='薛之谦'
message=netmusic.get_artist(artist_name)

songsMessage=netmusic.get_songsMessage(songs_name)
comment=netmusic.get_comments(songsMessage[0]['id'])
#lyric=netmusic.netease.song_lyric(songsMessage[0]['id'])
#detail=netmusic.find_song(songname='演员',artist_name='薛之谦')
#userplaylist=netmusic.get_user_playlist(username='Afullgoodtime')
#playlist_datail=netmusic.get_detail_playlist(userplaylist[0]['id'])
netmusic.play_song('薛之谦的歌')
#download_music.download(songsID[0],'F:\\python_file\个人助理接口\\music\\'+songs_name+'.mp3')

#ID,Name=netmusic.get_artist_songs('朴树')
#netmusic.batch_download(ID,Name,['朴树']*50)
""" 
