#  视图函数 do_login
from django.shortcuts import render,redirect
from web.models import *
# Create your views here.
from django.shortcuts import HttpResponse

#  request 为包含用户请求相关所有数据 可以获取用户提交的数据等信息
# settings中的path 清空时网页优先查看当前目录 默认是优先根目录下的templates
# def login(request):
    # return HttpResponse('登陆页面')

    # return render(request,'login.html')
    # 跳转到默认的网页 settings配置位置 需要在settings中注册app位置才能找到当前目录下templates
    #  最外层放公用的模板网页 每个app里放单独的模板

    # 重定向
    # return redirect('https://www.baidu.com')

def user_list(request):
    #  1.获取数据库所有用户列表
    data = ['rex','john','bob']

    mapping = {'name':'rex','age':19,'size':18}
    # 2.打开文件并读取内容
    # 3.模板渲染---文本替换 将网页中的message对象替换 可替换对象为{{}} 中内容
    # 单独获取对象：Django中html不支持 data[0] 读取数据 换为data.0
    return render(request,'user_list.html',{'message':'标题来了','data_list':data,'map':mapping})

# 案列 实现一个电话号码访问页面
"""
1.urls设置函数与路径
2.views页面中定义函数 
3.当前app下创建html样式
"""
def phone_list(request):
    queryset = [
        {'id':1,'phone':'188881','city':'上海'},
        {'id':2,'phone':'188882','city':'北京'},
        {'id':3,'phone':'188883','city':'深圳'},
        {'id':4,'phone':'188884','city':'武汉'},
    ]
    return render(request,'phone_list.html',{'data':queryset})
#  static是静态文件 在html中需要提前声明加载static

def something(request):
    #     request是一个对象 封装了用户发过来的所有数据

    # 1. 获取请求方式
    print(request.method)

    # 2. 在URL上传递值
    print(request.GET)

    # 3.在请求体中传递数据
    print(request.POST)

    # return HttpResponse('返回内容')

    # 【响应】  读取html内容 渲染 返回给用户浏览器
    return render(request,'something.html',{'title':'来了'})


def login1(request):
    if request.method =='GET':
        return render(request,'login1.html')

    # post请求获取用户提交数据
    print(request.POST)
    username = request.POST.get('user')
    password = request.POST.get('password')
    if username =='zzd' and password == '123':
        return HttpResponse('登陆成功')
    return render(request,'login1.html', {'error_msg':'用户名或密码错误'})


# 表内数据管理
# insert into web_department(title) values('销售部‘) 等同于 Department.objects.create(title='销售部')
def orm(request):
    #     测试orm操作表中数据
    # Department.objects.create(title='销售部')
    # Department.objects.create(title='IT部')
    # Department.objects.create(title='运营部')
    # UserInfo.objects.create(name='猪憨莲',password='1234',age=18)
    # UserInfo.objects.create(name='大哥',password='444',age=28)

    # 删除
    # UserInfo.objects.filter(id=2).delete()
    # Department.objects.all().delete()

    # 获取数据 Queryset类型 尾部加上.first() 可以选择第一条
    # data_list = UserInfo.objects.all()
    # for obj in data_list:
    #     print(obj.id,obj.name,obj.password,obj.age)

    # 更新数据
    # UserInfo.objects.filter(id=3).update(age=20)
    return  HttpResponse('成功')

# 案例用户管理
def info_list(request):
    #     1.获取数据库中所有用户信息
    data_list = UserInfo.objects.all()


    return render(request,'info_list.html',{'data_list':data_list})

def info_add(request):
    if request.method =='GET':
        return render(request,'info_add.html')
    user = request.POST.get('user')
    pwd = request.POST.get('pwd')
    age = request.POST.get('age')

    UserInfo.objects.create(name=user,password=pwd,age=age)
    # 跳转到自己网址可以省了域名
    return redirect('/info/list/')

def info_delete(request):
    nid = request.GET.get('nid')
    UserInfo.objects.filter(id=nid).delete()
    return redirect('/info/list/')









