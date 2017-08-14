from django.db import models

# Create your models here.

# 创建表
import os ,sys
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))#获取相对路径转为绝对路径赋于变量
sys.path.append(BASE_DIR)#增加环境变量
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint, Index,Table,DATE,DateTime
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine
from sqlalchemy import func #统计
#from sqlalchemy_utils import ChoiceType,PasswordType #

from addmodd import db_conn
Base = declarative_base()#生成orm 基类

# #创建用户－－分组,自动维护
User_m2m_Group = Table('user_m2m_group', Base.metadata,
        Column('user_id',Integer,ForeignKey('user.id', ondelete='CASCADE', onupdate='CASCADE')),#关联,用户id
        Column('group_id',Integer,ForeignKey('groups.id', ondelete='CASCADE', onupdate='CASCADE')),#关联,分组id
        )

# #创建主机－－分组,自动维护
Host_m2m_Group = Table('host_m2m_group', Base.metadata,
        Column('host_id',Integer,ForeignKey('host.id', ondelete='CASCADE', onupdate='CASCADE')),#关联,主机表id
        Column('group_id',Integer,ForeignKey('groups.id', ondelete='CASCADE', onupdate='CASCADE')),#关联,分组id
        )
##分组表
class Groups(Base):
    __tablename__='groups'
    id=Column(Integer,primary_key=True)#自增
    groupname=Column(String(64),nullable=False,)#组名不能为空
    user=relationship('User',secondary=User_m2m_Group,backref='groups')#分组表 远程联合表 查询与反查

#主机表
class Host(Base):#主机表
    __tablename__='host'
    id=Column(Integer,primary_key=True)#自增
    hostname=Column(String(64),nullable=False,unique=True)#主机名不能为空  唯一
    ip=Column(String(64),unique=True)#ip  唯一
    dep=Column(String(64),)#部门
    position=Column(String(64),)#使用职位
    name=Column(String(32),)#使用人姓名
    MAC=Column(String(64),)#MAC地址
    location=Column(String(64),)#位置
    group=relationship('Groups',secondary=Host_m2m_Group,backref='host')#分组表 查询与反查
    detailed_id=Column(Integer,ForeignKey('detailed_list.id'))#详细配置 外键
    detailed_lists=relationship("DetailedList",foreign_keys=[detailed_id],backref="host")#自定义关联反查 详细配置类Detailed_List通过host 查host

    def __repr__(self):
        return self.hostname#输出主机名

##详细配置
class DetailedList(Base):
    __tablename__='detailed_list'
    id=Column(Integer,primary_key=True)#自增
    CPU=Column(String(64),)#CPU
    memory=Column(String(64),)#内存条
    def __repr__(self):
        return self.id#输出 id

#普通用户表
class User(Base):
    __tablename__='user'
    id=Column(Integer,primary_key=True)
    username=Column(String(64),nullable=False,unique=True)#用户名 唯一
    password=Column(String(64))
    def __repr__(self):
        return self.username#用户名

#后台管理员用户名密码
class Admin_User(Base):
    __tablename__='admin_user'
    id=Column(Integer,primary_key=True)
    username=Column(String(64),nullable=False,unique=True)#用户名 唯一
    password=Column(String(64))

    def __repr__(self):
        return self.username#用户名


#                      用户 密码  主机             库
#Base.metadata.create_all(db_conn.engine)#创建表结构