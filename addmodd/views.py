from django.shortcuts import render
from django.shortcuts import redirect#重定向
import random,string
# Create your views here.

from addmodd import db_conn
from addmodd import models

#登陆相关函数
def login(request):
     #包含用户提交的所有信息
    #获取用户提交方法    request
    error_msg=''#错误信息
    if request.method=="POST":
        #获取用户 通过POST提交过来的数据
        user=request.POST.get('user',None)#获取传过来的用户名
        pwd=request.POST.get('pwd',None)#获取传过来的密码
        yzm=request.POST.get('yzmr',None)#获取传过来的验证码
        rans=request.POST.get('yzma',None)
        #print(yzm,rans)
        names=db_conn.Session.query(models.Admin_User).filter_by(username=user).first()#获取用户帐户数据
        if  not yzm or yzm!=rans:#如果没有验证码或 验证码出错
            error_msg="验证码出错或不能为空!"
        elif names and pwd==names.password:#如果获取成功 说明 在 用户列表中 并且密码正确
            # request.COOKIES ['IS_LOGIN']=True#登陆成功
            # request.COOKIES['USERNAME']=names#记录用户名
            res=redirect('/web_hosts')#跳转的页面
            res.set_cookie('IS_LOGIN',True)##登陆成功
            res.set_cookie('USERNAME',names)#记录用户名
            return res
        else:#用户密码不正确
            error_msg='用户名密码不正确!'

    return render(request,'login.html',{'error_msg':error_msg})#返回 login 页面 发送error_msg 数据

def user_login(request):
    error_msg=''#错误信息
    if request.method=="POST":
        #获取用户 通过POST提交过来的数据
        user=request.POST.get('user',None)#获取传过来的用户名
        pwd=request.POST.get('pwd',None)#获取传过来的密码
        yzm=request.POST.get('yzmr',None)#获取传过来的验证码
        rans=request.POST.get('yzma',None)
        #print(yzm,rans)
        names=db_conn.Session.query(models.User).filter_by(username=user).first()#获取用户帐户数据
        if  not yzm or yzm!=rans:#如果没有验证码或 验证码出错
            error_msg="验证码出错或不能为空!"
        elif names and pwd==names.password:#如果获取成功 说明 在 用户列表中 并且密码正确
            res=redirect('/hosts')#跳转的页面
            res.set_cookie('IS_LOGIN',True)##登陆成功
            res.set_cookie('USERNAME',names)#记录用户名
            return res
        else:#用户密码不正确
            error_msg='用户名密码不正确!'

    return render(request,'user_login.html',{'error_msg':error_msg})

#####################数据库相关操作###################
#获取主机列表
def mysqlset():
    hosts_list=db_conn.Session.query(models.Host).all()#主机列表
    return hosts_list

#获取管理用户
def adminuser():
    names=db_conn.Session.query(models.Admin_User).all()#获取用户帐户数据
    return names

#获取用户列表
def userset():
    user_list=db_conn.Session.query(models.User).all()#用户列表
    return user_list
#获取分组列表
def groupset():
    group_list=db_conn.Session.query(models.Groups).all()#分组列表
    return group_list

#获取配置列表
def cfg_list():
    conf_list=db_conn.Session.query(models.DetailedList).all()#分组列表
    return conf_list

#删除主机
def delset(nid):
    db_conn.Session.query(models.Host).filter_by(id=nid).delete()#删除记录
    db_conn.Session.commit()#关闭事务
    return
#删除用户
def del_user(nid):
    db_conn.Session.query(models.User).filter_by(id=nid).delete()#删除记录
    db_conn.Session.commit()#关闭事务
    return

#删除分组
def del_group(nid):
    db_conn.Session.query(models.Groups).filter_by(id=nid).delete()#删除记录
    db_conn.Session.commit()#关闭事务
    return

#批量删除主机
def delsets(list):
    for i in list:
        db_conn.Session.query(models.Host).filter_by(id=i).delete()#删除记录
    db_conn.Session.commit()#关闭事务
    return

##添加数据
def addset(obj):
    db_conn.Session.add(obj)#增加记录
    db_conn.Session.commit()#关闭事务
    return

#详情查看
def hostdetail(nid):
    host=db_conn.Session.query(models.Host).filter_by(id=nid).first()
    return host


#修改主机信息数据
def  info(request):
    id=request.POST.get('id',None)
    hostnames=request.POST.get('hostname',None)#主机名
    ip=request.POST.get('ip',None)#ip
    dep=request.POST.get('dep',None)#部门
    position=request.POST.get('position',None)#职位
    name=request.POST.get('name',None)#姓名
    mac=request.POST.get('mac',None)#
    location=request.POST.get('location',None)#位置
    detailed=request.POST.get('detaled_id',None)#配置
    print(detailed)
    db_conn.Session.query(models.Host).filter_by(id=id).update({'hostname':hostnames,'ip':ip,'dep':dep,'position':position, 'name':name,'MAC':mac,'location':location,'detailed_id':detailed})
    db_conn.Session.commit()#关闭事务



############################url#######################
#管理后台相关操作函数
def web_hosts(request):
    is_login=request.COOKIES.get('IS_LOGIN',False)#判断是否登陆
    hosts_list=mysqlset()#主机列表
    conf_list=cfg_list()#配置列表
    if is_login:
        username=request.COOKIES.get('USERNAME',False)#获取用户名
        names=db_conn.Session.query(models.Admin_User).filter_by(username=username).first()#获取用户帐户数据
        if names:#判断是否是管理员
            if request.method=="GET":
                is_user=request.GET.get('username',None)#获取注销用户信息
                if is_user:
                    res=redirect('/login')#跳转到登陆页面
                    res.set_cookie('IS_LOGIN',False)##注销登陆
                    res.set_cookie('USERNAME',False)#注销用户名
                    return res
            if request.method=="POST":
                hostnames=request.POST.get('hostname',None)#主机名
                ip=request.POST.get('ip',None)#ip
                dep=request.POST.get('dep',None)#部门
                position=request.POST.get('position',None)#职位
                name=request.POST.get('name',None)#姓名
                mac=request.POST.get('mac',None)#
                location=request.POST.get('location',None)#位置
                detailed=request.POST.get('detailed_id',None)#配置
                host_obj =models.Host(hostname=hostnames,ip=ip,dep=dep,position=position,
                                      name=name,MAC=mac,location=location,
                                      detailed_id=detailed)#生成你要创建的数据对象
                db_conn.Session.add(host_obj)#增加记录
                db_conn.Session.commit()#关闭事务
                #addset(host_obj)
            return render(request,'web_hosts.html',{'host_list':hosts_list,'username':username,'conf_list':conf_list})
        else:
            res=redirect('/login/')#跳转到登陆页面
            res.set_cookie('IS_LOGIN',False)##注销登陆
            res.set_cookie('USERNAME',False)#注销用户名
            return res
    else:
        return render(request,'login.html')
        #return redirect('/login')#跳转

#分组主机
def hosts(request):
    is_login=request.COOKIES.get('IS_LOGIN',False)#判断是否登陆

    if is_login:
        if request.method=="GET":
            is_user=request.GET.get('username',None)#获取注销用户信息
            if is_user:
                res=redirect('/user_login/')#跳转到登陆页面
                res.set_cookie('IS_LOGIN',False)##登陆成功
                res.set_cookie('USERNAME',False)#记录用户名
                return res
        #hosts_list=mysqlset()#主机列表
        print(is_login)

        username=request.COOKIES.get('USERNAME',False)#获取用户名
        user=db_conn.Session.query(models.User).filter_by(username=username).first()#用户对象
        print(user,'==============================')
        hosts_list=db_conn.Session.query(models.Host).all()#主机列表
        group_list=db_conn.Session.query(models.Groups).all()#主机列表


        if request.method=="POST":
            pass
            #addset(host_obj)
        return render(request,'hosts.html',{'host_list':hosts_list,'username':username,'group_list':group_list,'user':user})

    else:
        return render(request,'user_login.html')
    #return render(request,'hosts.html',{})

#查看详情
def detail(request):
    #hosts_list=mysqlset()#主机列表
    nid=request.GET.get('nid')
    print(request)
    host=hostdetail(nid)#获取详情
    #host=db_conn.Session.query(models.Host).filter_by(id=nid).first()
    return render(request, 'detail.html', {'host_list':host})

#修改主机信息
def modify(request):
    nid=request.GET.get('nid',None)
    host=hostdetail(nid)
    conf_list=cfg_list()#配置列表
    if request.method=='POST':
        info(request)
        return redirect('/web_hosts/')#跳转
    return render(request,'modify.html',{'host_list':host,"conf_list":conf_list})

#用户修改主机信息
def user_modify(request):
    nid=request.GET.get('nid',None)
    host=hostdetail(nid)
    conf_list=cfg_list()#配置列表
    if request.method=='POST':
        info(request)
        return redirect('/hosts/')#跳转
    return render(request,'user_modify.html',{'host_list':host,"conf_list":conf_list})

#删除主机
def delhosts(request):
    #nid=request.GET.get("nid")
    #obj=db_conn.Session.query(models.Host).filter_by(id=nid).first()
    if request.method=="GET":
        nid=request.GET.get("nid")#获取要删除的id
        delset(nid)#调用删除函数
        return redirect('/web_hosts')#跳转
    return render(request,'delhost.html')

#增加用户
def adduser(request):
    user_list=userset()#用户列表
    if request.method=='POST':
        user=request.POST.get('user',None)
        pwd=request.POST.get('pwd',None)
        name_obj=models.User(username=user,password=pwd)#生成用户数据对象
        addset(name_obj)
    return render(request,'adduser.html',{'user_list':user_list})

#删除用户
def deluser(request):
    user_list=userset()#用户列表
    if request.method=='POST':
        nid=request.POST.get("user_id",None)#获取要删除的id
        del_user(nid)#调用删除函数
        return redirect('/deluser')#跳转
    return render(request,'deluser.html',{'user_list':user_list})

#增加分组
def addgroup(request):
    group_list=groupset()#分组列表
    if request.method=='POST':
        groupname=request.POST.get('groupname',None)
        name_obj=models.Groups(groupname=groupname)#生成用户数据对象
        addset(name_obj)
    return render(request,'addgroup.html',{'group_list':group_list})

#删除分组
def delgroup(request):
    group_list=groupset()#分组列表
    if request.method=='POST':
        nid=request.POST.get('nid',None)
        del_group(nid)
        return redirect('/delgroup')#跳转
    return render(request,'delgroup.html',{'group_list':group_list})

#增加配置
def adddet(request):
    conf_list=cfg_list()#配置列表
    if request.method=='POST':
        cpu=request.POST.get('cpu',None)
        memory=request.POST.get('memory',None)
        name_obj=models.DetailedList(CPU=cpu,memory=memory)#生成配置数据对象
        addset(name_obj)
        return redirect('/adddet')#跳转
    return render(request,'adddet.html',{'conf_list':conf_list})

#删除配置
def deldet(request):
    conf_list=cfg_list()#配置列表
    if request.method=='POST':
        nid=request.POST.get('nid',None)
        del_group(nid)
        return redirect('/deldet')#跳转
    return render(request,'deldet.html',{'conf_list':conf_list})

#用户分组
def group_user(request):
    group_list=groupset()#分组列表
    user_list=userset()#用户列表
    if request.method=="POST":
        user_id=request.POST.get('user_id',None)
        groups_id=request.POST.get('groups_id',None)
        #主机对象
        u=db_conn.Session.query(models.User).filter(models.User.id==user_id).first()
        #分组对象
        g=db_conn.Session.query(models.Groups).filter(models.Groups.id==groups_id).first()

        u.groups.append(g)
        db_conn.Session.commit()

    return render(request,'group_user.html',{'group_list':group_list,'user_list':user_list})

#主机分组
def group_host(request):
    hosts_list=mysqlset()#主机列表
    group_list=groupset()#分组列表
    if request.method=="POST":
        host_id=request.POST.get('host_id',None)
        groups_id=request.POST.get('groups_id',None)
        #主机对象
        h=db_conn.Session.query(models.Host).filter(models.Host.id==host_id).first()
        #分组对象
        g=db_conn.Session.query(models.Groups).filter(models.Groups.id==groups_id).first()

        h.group.append(g)
        db_conn.Session.commit()



    return render(request,'group_host.html',{"host_list":hosts_list,"group_list":group_list})#主机分组


#默认主页面
def index(request):
    return render(request,'index.html',{})
