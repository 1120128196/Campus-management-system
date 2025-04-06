from django.shortcuts import render, redirect
from app01.models import *
from app01.utils.pagination import Pagination
from app01.utils.form import AdminModelForm,AdminEditModelForm,AdminResetModelForm


def admin_list(request):
    ''' 管理员列表'''
    # 检查用户是否登陆 未登录返回登陆页码
    # 只需要检查用户发来请求中的cookie字符串 然后检查session中是否有对应信息
    # 所有视图函数都需要加入（添加编辑删除重置页面）  可以通过django中间件实现
    # info = request.session.get('info')
    # if not info:
    #     return redirect('/projectlogin/')

    # # 获取到session携带的用户信息
    # info_dict = request.session['info']



    # 搜索 搜索框中的跳转后保留默认值 需要传入前端
    data_dict = {}
    search_data = request.GET.get('q','')
    if search_data:
        data_dict = {'username__contains':search_data}

    queryset = Admin.objects.filter(**data_dict)

    page_obj = Pagination(request,queryset)

    context = {
        'queryset':page_obj.page_queryset,
        'page_string':page_obj.html(),
        'search_data':search_data
    }
    return render(request,'admin_list.html',context)

def admin_add(request):
    ''' 添加管理员'''
    if request.method == 'GET':
        form = AdminModelForm()
        # 由于所有添加页码都一样 直接用change.html 替换了名字就行了
        return render(request,'change.html',{'title':'添加管理员','form':form})
    form = AdminModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/admin/list/')
    return render(request,'change.html',{'title':'添加管理员','form':form})

def admin_edit(request,nid):
    ''' 编辑管理员'''
    row_obj = Admin.objects.filter(id=nid).first()
    if not row_obj:
        return redirect('/admin/list/')
    # instance显示默认值  由于只修改username 则重新定义一个modelform
    title = '编辑管理员'
    if request.method =='GET':
        form = AdminEditModelForm(instance=row_obj)
        return render(request,'change.html',{'title':title,'form':form})
    form = AdminEditModelForm(data=request.POST,instance=row_obj)
    if form.is_valid():
        form.save()
        return redirect('/admin/list/')
    return render(request, 'change.html', {'title': title, 'form': form})

def admin_delete(requese,nid):
    """ 删除管理员"""
    row_obj = Admin.objects.filter(id=nid).delete()
    return redirect('/admin/list/')

def admin_reset(request,nid):
    ''' 重置密码'''
    row_obj = Admin.objects.filter(id=nid).first()
    if not row_obj:
        return redirect('/admin/list/')

    title = '重置密码-{}'.format(row_obj.username)
    if request.method =='GET':
        form = AdminResetModelForm()
        return render(request,'change.html',{'title':title,'form':form})
    # 注意保存修改的密码必须带上instance 此时instance不是默认值情况了 是定义到当前id的字段
    form = AdminResetModelForm(data=request.POST,instance=row_obj)
    if form.is_valid():
        form.save()
        return redirect('/admin/list')
    return render(request,'change.html',{'title':title,'form':form})