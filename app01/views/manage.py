import os
from django.shortcuts import render,HttpResponse,redirect
from app01.utils.form import UpModelForm
from app01.models import Manager

def manage_list(request):
    ''' 导员列表'''
    queryset = Manager.objects.all()
    return  render(request,'manage_list.html',{'query_set':queryset})
def manage_add(request):
    title = '导员添加'
    if request.method == 'GET':
        form = UpModelForm()
        return render(request,'change.html',{'form':form,'title':title})
    form = UpModelForm(data=request.POST,files=request.FILES)
    if form.is_valid():
        form.save()
        return redirect('/manage/list/')
    return render(request, 'change.html', {'form': form, 'title': title})
