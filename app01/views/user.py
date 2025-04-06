from django.shortcuts import render, redirect
from app01.models import *
from app01.utils.pagination import Pagination
from app01.utils.form import UserModelForm

def user_list(request):
    """ 用户管理"""
    queryset = UserInfo.objects.all()
    page_obj = Pagination(request,queryset,page_size=4)

    context = {
        'queryset':page_obj.page_queryset,
        'page_string':page_obj.html()
    }

    # python语法获取数据
    # for obj in queryset:
        #django中的优势：根据约束获取choice的选择值 根据获取外键关联的name值
        # print(obj.gender,obj.get_gender_display())  后者可以直接获取选择值
        # print(obj.depart_id,obj.depart.title) 直接调用depart可以获取到关联表信息
    # 注意在模板语法{{}} 中不需要加（） 他会自动补齐
    return render(request,'user_list.html',context)

#  传统方式
def user_add(request):
    """ 添加用户
        传统方式 1.用户提交数据没有校验 2.页面上没有错误提示 3.页面上每个字段都要重写 这三点form组件可以实现
        4.关联的数据如 genderchoices 要手动获取比较复杂 modelform可以实现
    """
    if request.method =='GET':
        context = {
            'gender_choices':UserInfo.gender_choices,
            'depart_list':Department.objects.all(),
        }
        # 直接传入元组 可以格式好看些
        return render(request,'user_add.html',context)

#     获取数据
    user = request.POST.get('user')
    pwd = request.POST.get('pwd')
    age = request.POST.get('age')
    account = request.POST.get('ac')
    ctime = request.POST.get('ctime')
    gender = request.POST.get('gd')
    depart_id = request.POST.get('dp')
#    添加到数据库中
    UserInfo.objects.create(name=user,password=pwd,age=age,account=account,create_time=ctime,
                            gender=gender,depart_id=depart_id)
    return redirect('/user/list/')

def user_model_form_add(request):
    """" modelform版本添加用户"""
    if request.method == 'GET':
        form = UserModelForm()
        return render(request,'user_model_form_add.html',{'form':form})

    # 从前端通过POST获取数据并校验
    form = UserModelForm(data=request.POST)

    # 使用is_valid自动校验 通过save()可以直接保存到数据库
    if form.is_valid():
        # print(form.cleaned_data)
        form.save()
        return redirect('/user/list/')

    # 校验失败 提示信息 需要在前端中带上field.error 提示中文要在setting中修改LANGUAGE_CODE='zh-hans'
    return render(request,'user_model_form_add.html',{'form':form})

def user_edit(request,nid):
    """ 编辑用户"""
    # 根据id获取编辑那行的数据
    row_obj = UserInfo.objects.filter(id=nid).first()
    if request.method == 'GET':
        # 根据id获取编辑那行的数据
        # 在modelform中只要设置了instance值 默认就会显示其内容
        form = UserModelForm(instance=row_obj)
        return render(request,'user_edit.html',{'form':form})

    # 从前端通过post获取数据 注意更新时候要获取当前id的数据 这时候form.save()才会更新数据而不是新建数据
    form = UserModelForm(data=request.POST,instance=row_obj)
    if form.is_valid():
        # form.instance.字段名 = 值 来保存用户输入之外的内容
        form.save()
        return redirect('/user/list/')
    return render(request,'user_edit.html',{'form':form})

def user_delete(request,nid):
    """ 用户删除"""
    UserInfo.objects.filter(id=nid).delete()
    return redirect('/user/list/')
