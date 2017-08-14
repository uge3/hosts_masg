主机管理WEB页面

使用MySQL
   或SQLALchemy
    主机管理(8列)
        ip
    用户表:
        用户名
        密码
    功能:
        1  管理员登陆  用户登陆
        2  管理员后台页面
            -查看所有主机信息(4列)
            -查看详细信息
    
            -增加主机信息(8列)  模态对话框
            -删除主机
    
            -修改主机信息
    
            -添加用户
            -删除用户
    
            -添加分组
            -删除分组
    
            -主机分组操作
            -用户分组操作
    
        3  用户登陆后台页面
            --查看可管理的分组
    
            --查看详细信息
            --修改主机信息
            
        说明:    初始管理员   用户名: admin  密码: admin
        
        程序结构:
    
    hosts_masg/#主目录
    
    |- - -addmodd/# APP目录
    
    |       |- - -init.py
    
    |       |- - -admin.py#Django提供的后台管理
    
    |       |- - -apps.py#配置当前app
    
    |       |- - -db_conn.py#数据库接连设置
    
    |       |- - -mag_init.py#始初化表结构文件
    
    |       |
    
    |       |- - -migrations /#数据库操作记录目录
    
    |       |- - -models.py#创建数据库表
    
    |       |- - -tests.py#单元测试
    
    |       |- - -views.py#业务代码
    
    |
    
    |- - -db.sqlite3/Django自带数据库
    
    |
    
    |- - -hosts_masg/#WEB服务端程序目录
    
    |       |- - -init.py
    
    |       |- - -settings.py#配置文件
    
    |       |- - -urls.py#对应关系 (路由)
    
    |       |- - -wsgi.py#WSIG规范文件
    
    |       |
    
    |       |
    
    |       |- - -core/##主逻辑程序目录
    
    |       |     |- - -server_class.py#主逻辑 相关类
    
    |
    
    |- - -manage.py#管理Django程序
    
    |
    
    |- - -static/#静态文件目录
    
    |       |- - -init.py
    
    |       |- - -bootstrap-3.3.7-dist/# bootstrap文件目录
    
    |       |- - -css/# css文件目录
    
    |       |- - -img/# 图片文件目录
    
    |       |- - -jquery-easyui-1.5.2/#jquery ui文件目录
    
    |       |- - -js/#js文件目录
    
    |
    
    |
    
    |- - -templates/#HTML文件目录
    
    |       |- - -adddet.html#增加配置页面
    
    |       |- - -addgroup.html#增加分组页面
    
    |       |- - -adduser.html#增加用户页面
    
    |       |- - -deldet.html#删除配置页面
    
    |       |- - -delgroup.html#删除分组页面
    
    |       |- - -delhost.html#删除主机跳转页面
    
    |       |- - -deluser.html#删除用户页面
    
    |       |- - -detail.html#详细情况页面
    
    |       |- - -group_host.html#主机分组操作页面
    
    |       |- - -group_user.html#用户分组操作页面
    
    |       |- - -hosts.html#用户后台页面
    
    |       |- - -index.html#主页面
    
    |       |- - -login.html#管理员登陆页面
    
    |       |- - -modify.html#管理员修改页面
    
    |       |- - -user_login.html#用户登陆页面
    
    |       |- - -web_hosts.html#管理后台管理页面
    
    |       |
    
    |       |- - -master/#母板目录
    
    |               |- - -mod.html#后台页面模板
    
    |               |- - -mod_login.html#登陆页面模板
    
    |
    
    |- - -README
    
        
        
        
        

​	






