#!usr/bin/env python
#-*-coding:utf-8-*-
# Author calmyan 
#python 
#2017/7/15    19:40
#__author__='Administrator'

from sqlalchemy import create_engine,Table
from  sqlalchemy.orm import sessionmaker

from hosts_masg import settings


#engine = create_engine(settings.DB_CONN)
engine = create_engine(settings.DB_CONN,echo=True)#数据库连接通道

SessionCls = sessionmaker(bind=engine) #创建与数据库的会话session class ,返回session的是个class,不是实例
Session = SessionCls()