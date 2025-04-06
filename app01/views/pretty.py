from django.shortcuts import render, redirect
from app01.models import *
from app01.utils.pagination import Pagination
from app01.utils.form import PrettyModelForm,PrettyEditModelForm

def pretty_list(request):
    """ 账号列表"""

    # greater than equal less
    # PrettyNum.objects.filter(id_gt=12)
    # PrettyNum.objects.filter(id_gte=12)
    # PrettyNum.objects.filter(id_lt=12)
    # PrettyNum.objects.filter(id_lte=12)
    # 以xxx开头 或结尾 或包含  这些都可以收入dict中
    # PrettyNum.objects.filter(mobile__startswith=)
    # PrettyNum.objects.filter(mobile__endswith=)
    # PrettyNum.objects.filter(mobile__contains=)
    # 通过get方法获取到搜索按钮返回的信息 默认没有内容返回则为''
    data_dict = {}
    search_data = request.GET.get('q','')
    if search_data:
        data_dict = {'mobile__contains':search_data}

    # 通过自定义组件实现分页 把下面注释内容封装了
    queryset = PrettyNum.objects.filter(**data_dict).order_by('-level')

    page_obj = Pagination(request,queryset)

    # # 显示的起始页和最终页 由于每次只显示 当前页的前2页和后2页
    # start_page = page - 2 if page - 2 > 0 else 1
    # end_page = page + 2 if page + 2 <= total_page_count else total_page_count
    #
    # # 拼接成html返回前端
    # page_str_list = [] # 页码
    # # 首页
    # page_str_list.append('<li><a href="?page={}">首页</a></li>'.format(1))
    # # 上一页
    # pre_page = '<li><a href="?page={}">上一页</a></li>'.format(page-1) if page>1 else ''
    # page_str_list.append(pre_page)
    # # 页码
    # for i in range(start_page,end_page + 1):
    #     if i ==page: #当前页高亮
    #         ele = '<li class="active"><a href="?page={}">{}</a></li>'.format(i, i)
    #     else:
    #         ele = '<li><a href="?page={}">{}</a></li>'.format(i,i)
    #     page_str_list.append(ele)
    # # 下一页实现
    # pre_page = '<li><a href="?page={}">下一页</a></li>'.format(page+1) if page < total_page_count else ''
    # page_str_list.append(pre_page)
    # # 尾页
    # page_str_list.append('<li><a href="?page={}">尾页</a></li>'.format(total_page_count))
    # page_string = mark_safe(''.join(page_str_list)) #组成字符串注意要加mark_safe前端才能通过

    # 可以通过order by 排序 filter中为空时候就等于all
    # query_set = PrettyNum.objects.filter(**data_dict).order_by('-level')[start:end]
    # 使用类来传参 和上述步掫一页 简化了

    set = {
        'query_set': page_obj.page_queryset, #分完页的数据
        'search_data': search_data, #搜索的数据
        'page': page_obj.html() #分页的html代码
    }

    return render(request,'pretty_list.html',set)

def pretty_add(request):
    """ 添加账号"""
    if request.method == 'GET':
        form = PrettyModelForm()
        return render(request,'change.html',{'form':form,'title':'添加账号'})

    form = PrettyModelForm(data = request.POST)
    if form.is_valid():
        form.save()
        return redirect('/pretty/list/')
    return render(request,'change.html',{'form':form,'title':'添加账号'})

def pretty_edit(request,nid):
    """ 编辑账号 """
    row_obj = PrettyNum.objects.filter(id=nid).first()
    if request.method == 'GET':
        #  如果表中的字段有不可修改的 则要重新定义个modelform类
        form = PrettyEditModelForm(instance=row_obj)
        return render(request,'change.html',{'form':form,'title':'修改账号'})
    form = PrettyEditModelForm(data=request.POST,instance=row_obj)
    if form.is_valid():
        form.save()
        return redirect('/pretty/list/')
    return render(request,'change.html',{'form':form,'title':'修改账号'})

def pretty_delete(request,nid):
    """ 账号删除"""
    PrettyNum.objects.filter(id=nid).delete()
    return redirect('/pretty/list/')

