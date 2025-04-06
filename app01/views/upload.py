import os
from django.shortcuts import render,HttpResponse
from app01.utils.form import UpForm,UpModelForm
from app01.models import Teacher

def upload_list(request):
    ''' 上传文件 手动方式'''
    if request.method == 'GET':
        return render(request,'upload_list.html')
    # print(request.FILES)  此时获得的是文件名字 需要在form中添加

    file_obj = request.FILES.get('avatar')

    f = open(file_obj.name,mode='wb')
    for chunk in file_obj.chunks():
        f.write(chunk)
    f.close()

    return HttpResponse('xxx')




def upload_form(request):
    ''' form 形式文件上传'''
    title = 'form上传'
    if request.method == 'GET':
        form = UpForm
        return render(request,'upload_form.html',{'form':form,'title':title})
    # 注意这里由于是表单加文件 文件数据单独读取
    form = UpForm(data = request.POST, files=request.FILES)
    if form.is_valid():
        # 1.读取文件内容 写入到文件夹中获取文件路径
        image_obj = form.cleaned_data.get('img')
        # 数据库存放的文件路径尽量别带app01 这样用户查看头像时候方便
        # 使用media存放用户上传内容
        # media_path = os.path.join(settings.MEDIA_ROOT,image_obj.name) 绝对路径
        media_path = os.path.join('media', image_obj.name) #相对路径
        # 本地存放文件位置

        f = open(media_path,mode='wb')
        for chunk in image_obj.chunks():
            f.write(chunk)
        f.close()
        # 2.将文件路径写入数据库
        Teacher.objects.create(
            name = form.cleaned_data['name'],
            age = form.cleaned_data['age'],
            img = media_path
        )


        return HttpResponse('xxx')
    return render(request,'upload_form.html',{'form':form,'title':title})

def upload_modelform(request):
    ''' 上传文件 modelform  比form更简便'''
    title = 'ModelForm文件上传'
    if request.method == 'GET':
        form = UpModelForm()
        return render(request,'upload_form.html',{'form':form,'title':title})
    form = UpModelForm(data = request.POST, files = request.FILES) #与之前的modelform相比这里的files别忘记
    if form.is_valid():
        # 与form的区别在此处 自动保存 字段+路径写入数据库
        form.save()
        return HttpResponse('success')
    return render(request, 'upload_form.html', {'form': form, 'title': title})