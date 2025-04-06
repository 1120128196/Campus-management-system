from django.shortcuts import render, redirect
from app01 import models
from utils.form import LoginForm




'''
使用到cookie--用户发送到浏览器的字符串 字符串可以通过网页检查查看
    session--浏览器备份用户字符串和对应信息 字符串默认放在数据库的django_session表中
'''

def projectlogin(request):
    ''' 登陆'''
    if request.method == 'GET':
        form = LoginForm()
        return render(request,'projectlogin.html',{'form':form})
    form = LoginForm(data = request.POST)
    if form.is_valid():
        exist = models.Admin.objects.filter(username=form.cleaned_data.get('un'),password=form.cleaned_data['pwd']).first()
        if not exist:
            form.add_error('pwd','用户名或密码错误') #主动写入错误信息
            return render(request, 'projectlogin.html', {'form': form})
        # 当用户名和密码正确 网站生成随机字符串 写到用户的浏览器cookie中 再写入到session中
        # 此时每一个通过验证登陆的用户 服务器都会存储其字符串对应的info字典信息
        request.session['info'] = {'id':exist.id,'name':exist.username}
        return redirect('/admin/list/')
    return render(request, 'projectlogin.html', {'form': form})

def logout(request):
    ''' 注销'''
    # 清除当前session
    request.session.clear()
    return redirect('/projectlogin/')


def projectlogin_add(request):
    ''' 注册'''
    if request.method == 'GET':
        form = LoginForm()
        return render(request,'project_add.html',{'form':form })
    form = LoginForm(data = request.POST)
    if form.is_valid():
        username = form.cleaned_data.get('un')
        password = form.cleaned_data.get('pwd')
        models.Admin.objects.create(username=username,password=password)
        return redirect('/projectlogin/')
    return render(request,'project_add.html',{'form':form })




