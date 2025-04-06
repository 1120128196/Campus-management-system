from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from utils.form import TaskModelForm
from app01.models import Task
from app01.utils.pagination import Pagination
import json
def task_list(request):
    ''' 任务管理'''
    queryset = Task.objects.all().order_by('-id')

    page_obj = Pagination(request, queryset)

    form = TaskModelForm()
    context = {
        'form':form,
        'queryset': page_obj.page_queryset,  # 分完页的数据
        'page_string': page_obj.html()  # 生成页码信息
    }
    return render(request,'task_list.html',context)
'''
ajax:与常规表单形式 get post相比 它不需要刷新网页就可以向后端传递参数
需要用csrf_exempt跳过csrf校验
'''
@csrf_exempt
def task_ajax(request):
    print(request.POST)
    # 一般ajax返回都是json格式 json格式前端需要记得处理为datatype
    data_dict = {'status':True,'data':[11,22,33,44]}
    # json_string = json.dump(data_dict)
    # return HttpResponse(json_string)
    # 上两步掫可以简化为
    return JsonResponse(data_dict)

@csrf_exempt
def task_add(request):
    print(request.POST)

    # ajax 的校验同样能用modelform校验
    form = TaskModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        data_dict = {'status':True}
        return JsonResponse(data_dict)
    #  使用ajax校验完后 错误信息通过errors.as_json()可以返回到前端
    data_dict = {'status':False,'error':form.errors}
    return JsonResponse(data_dict)
    # data_dict = {'status':False,'error':form.errors}
    # return HttpResponse(json.dumps(data_dict,ensure_ascii=False))