import random
from django.shortcuts import render
from django.http import JsonResponse


from app01.utils.pagination import Pagination
from app01.utils.form import OrderModelForm
from app01.models import Order
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
def order_list(request):
    ''' 订单列表'''
    queryset = Order.objects.all().order_by('-id')

    form = OrderModelForm()
    page_obj = Pagination(request, queryset)
    context = {
        'form':form,
        'queryset': page_obj.page_queryset,  # 分完页的数据
        'page_string': page_obj.html()  # 生成页码信息

    }
    return render(request,'order_list.html',context)

@csrf_exempt
def order_add(request):
    ''' 新建订单'''
    form = OrderModelForm(data = request.POST)
    if form.is_valid():
        # 保存的时候 由于oid属性没有传入值 需要手动传值  当存在某一属性不需要前台输入时候 可以这样
        form.instance.oid = datetime.now().strftime('%Y%m%d%H%M%S') + str(random.randint(1000,9999))
        form.instance.admin_id = request.session['info']['id']
        form.save()
        return JsonResponse({'status':True})
    return JsonResponse({'status':False,'error':form.errors})

def order_delete(request):
    ''' 删除订单 get请求不需要csrf'''
    uid = request.GET.get('uid')
    if Order.objects.filter(id = uid).exists():
        Order.objects.filter(id = uid).delete()
        return JsonResponse({'status': True})
    return JsonResponse({'status':False,'error':'删除失败：数据不存在'})

def order_detail(request):
    ''' 根据ID获取订单'''
#     方法1 常规
#     uid = request.GET.get('uid')
#     row_obj = Order.objects.filter(id=uid).first()
#     if not row_obj:
#         return JsonResponse({'status':False,'error':'数据不存在'})
# #     从数据库中获取到对象row_obj 可以通过手动构造返回前端
#     result = {
#         'status':True,
#         "data":{
#             'title':row_obj.title,
#             'price':row_obj.price,
#             'status':row_obj.status,
#         }
#     }
#     return JsonResponse(result)
#   方法2 直接获取字典 此时在filter后加入字典
    uid = request.GET.get('uid')
    row_dict = Order.objects.filter(id=uid).values('title','price','status').first()
    if not row_dict:
        return JsonResponse({'status': False, 'error': '数据不存在'})
    #     从数据库中获取到对象row_obj 可以通过手动构造返回前端
    result = {
        'status': True,
        "data": row_dict
    }
    return JsonResponse(result)

@csrf_exempt
def order_edit(request):
    ''' 编辑订单'''
    uid = request.GET.get('uid')
    row_obj = Order.objects.filter(id=uid).first()
    if not row_obj:
        return JsonResponse({'status': False, 'tips': ' 编辑失败：数据不存在'})
    form = OrderModelForm(data=request.POST,instance=row_obj)
    if form.is_valid():
        form.save()
        return JsonResponse({'status':True})
    return JsonResponse({'status':False,'error':form.errors})