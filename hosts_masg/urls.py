"""hosts_masg URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from addmodd import views

urlpatterns = [
    url(r'^$',views.index),
    url(r'^index',views.index),
    url(r'^admin', admin.site.urls),
    url(r'^login', views.login),#登陆
    url(r'^web_hosts', views.web_hosts),#主机查看
    url(r'^hosts', views.hosts),#分组主机查看
    url(r'^delhost', views.delhosts),#删除页面
    url(r'^modify', views.modify),#修改页面
    url(r'^user_modify', views.user_modify),#用户修改页面
    url(r'^detail', views.detail),#详情页面
    url(r'^adduser', views.adduser),#增加用户
    url(r'^deluser', views.deluser),#删除用户
    url(r'^adddet', views.adddet),#增加配置
    url(r'^deldet', views.deldet),#删除配置
    url(r'^addgroup', views.addgroup),#增加分组
    url(r'^delgroup', views.delgroup),#增加分组
    url(r'^user_login', views.user_login),#用户登陆
    url(r'^group_host', views.group_host),#主机分组
    #url(r'^host_rem', views.host_rem),#主机移出分组
    url(r'^group_user', views.group_user),#用户分组
    #url(r'^user_rem', views.user_rem),#用户移出分组

]
