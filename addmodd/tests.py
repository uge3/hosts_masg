from django.test import TestCase

# Create your tests here.
from addmodd import db_conn
from addmodd import models
id=11
hostnames='1'
ip='123'
dep='xxx'
position='444'
name='434'
mac='111'
location='kkk'
detailed='888'
db_conn.Session.query(models.Host).filter(models.Host.id==11).update({'hostname': 'jm-4', 'ip': '192.168.10.5', 'dep': '   前厅部', 'position': '经理', 'name': '周2', 'MAC': '00-11-22-33-44-60', 'location': '前台', 'detailed_id': '1'})
db_conn.Session.commit()#关闭事务