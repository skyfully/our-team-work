# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 19:36:22 2018
功能：记录用户在某个时间点对系统的输入信息（用户的指令或着用户说的话）
接口：使用Mysql数据库记录数据   安装pymysql等驱动器
实现过程：安装好Mysql数据库 和相关python连接模块 
         先在数据库中建立数据库“record1” 在record1中建立表user_record1 
         用pymysql连接数据库  通过execute提交数据

@author: mynumber
"""
import pymysql
import time
class record(object):
    """用于向数据库提交、查询、修改信息"""
    def __init__(self,database_name,table_name):
        self.database_name=database_name
        self.table_name=table_name
        self.table=self.database_name+'.'+self.table_name
        self.connect()
    def connect(self):
        try:
            print('正在连接数据库...')
            self.db = pymysql.connect("localhost","root","ZHUYINlong121217",self.database_name,charset='utf8')
            self.cursor=self.db.cursor()
            print('数据库连接成功...')
        except:
            print('连接失败...')
        
    def insert(self,time,content):
        """插入信息"""
        sql="INSERT INTO '%s' (`time`, `content`)"%(self.table)
        sql=sql.replace('\'','')
        sql=sql+"VALUES ('%s', '%s');" % (time,content)
        print(sql)
         
        try:
            self.cursor.execute(sql)
            self.db.commit()
            print('数据添加成功...')
        except:
            self.db.rollback()
            print('数据未成功添加...')
    def qury(self):
        sql= " SELECT * FROM '%s' " %(self.table)
        sql=sql.replace('\'','')
        try:
            self.cursor.execute(sql)
            results=self.cursor.fetchall()
            self.db.commit()
            print('数据查找成功...')
            return results
        except:
            self.db.rollback()
            print('数据查找失败...')
    def update(self,text):
        """根据text内容进行匹配,找到内容之后或着找到相似内容之后""" 
        pass
        
R=record("record1","user_record")
T=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
print(T)
text='关儿 我爱你'
R.insert(T,text)
result=R.qury()