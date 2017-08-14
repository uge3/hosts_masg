#!usr/bin/env python
#-*-coding:utf-8-*-
# Author calmyan 
#hosts_masg 
#2017/8/13    12:38
#__author__='Administrator'
from addmodd import db_conn
from addmodd import models
db_conn.Session.query(models.User_m2m_Group).filter_by(user_id=1).filter_by(group_id=1).delete()
db_conn.Session.commit()