#!usr/bin/env python
#-*-coding:utf-8-*-
# Author calmyan 
#hosts_masg 
#2017/8/10    11:46
#__author__='Administrator'

import os ,sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))#获取相对路径转为绝对路径赋于变量
sys.path.append(BASE_DIR)#增加环境变量
from addmodd import models
from addmodd import db_conn
from hosts_masg import settings
if __name__ == '__main__':
    #                      用户 密码  主机             库
    models.Base.metadata.create_all(db_conn.engine)#创建表结构

    A1 = models.Admin_User(username=settings.USERNAME,password=settings.USER_PWD)#初始化 登陆用户名
    db_conn.Session.add(A1)#添加初始用户名密码
    db_conn.Session.commit()#连接