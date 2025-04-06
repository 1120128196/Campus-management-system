"""djangoProject1 URL Configuration
专门存放 URL 路由根
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.template.defaulttags import url
from django.urls import path, include,re_path
from django.views.static import serve
from django.conf import settings
from web.views import *
from app01.views import depart,user,pretty,admin,account,task,order,chart,upload,manage
from captcha.views import captcha_refresh


urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('login/',login),
    path('phone/list/',phone_list),

#     请求和响应
    path('something/',something),

#     用户登录
    path('login1/',login1),

#     数据库操作
    path('orm/',orm),

#     案例 用户管理
    path('info/list/',info_list),
    path('info/add/',info_add),
    path('info/delete/',info_delete),

#     用户上传的文件一般放在media中  注意需要配置media
    re_path(r'^media/(?P<path>.*)$',serve,{'document_root':settings.MEDIA_ROOT},name='media'),
#     案例 部门管理 原始方式做法 后续使用简化方式 Django的Form和ModelForm组件
    path('depart/list/',depart.depart_list),
    path('depart/add/',depart.depart_add),
    path('depart/delete/',depart.depart_delete),
    # 正则表达式 中间必须得传整型参数 把用？的get方式传值省略了
    path('depart/<int:nid>/edit/',depart.depart_edit),
    # 文件上传
    path('depart/mutil/',depart.depart_mutil),

    path('user/list/',user.user_list),
    path('user/add/',user.user_add),
    path('user/model/form/add/',user.user_model_form_add),
    path('user/<int:nid>/edit/',user.user_edit),
    path('user/<int:nid>/delete/',user.user_delete),

    path('pretty/list/',pretty.pretty_list),
    path('pretty/add/',pretty.pretty_add),
    path('pretty/<int:nid>/edit/',pretty.pretty_edit),
    path('pretty/<int:nid>/delete/',pretty.pretty_delete),

#     管理员管理
    path('admin/list/',admin.admin_list),
    path('admin/add/',admin.admin_add),
    path('admin/<int:nid>/edit/',admin.admin_edit),
    path('admin/<int:nid>/delete/',admin.admin_delete),
    path('admin/<int:nid>/reset/',admin.admin_reset),
#     登陆
    path('projectlogin/',account.projectlogin),
    path('projectlogin/add/',account.projectlogin_add),
    path('logout/',account.logout),
    path('captcha/',include('captcha.urls')),
    path('captcha/refresh/',captcha_refresh), #验证码点击刷新 注意使用内置方法 导入此方法就行了  还需要在html中写入script脚本

#     任务管理
    path('task/list/',task.task_list),
    path('task/ajax/',task.task_ajax),
    path('task/add/',task.task_add),

#     订单管理
    path('order/list/',order.order_list),
    path('order/add/',order.order_add),
    path('order/delete/',order.order_delete),
    path('order/detail/',order.order_detail),
    path('order/edit/',order.order_edit),

#     数据统计
    path('chart/list/',chart.chart_list),
    path('chart/bar/',chart.chart_bar),
    path('chart/pie/',chart.chart_pie),
    path('chart/line/',chart.chart_line),

#     文件上传
    path('upload/list/',upload.upload_list),
    path('upload/form/',upload.upload_form),
    path('upload/model/form/',upload.upload_modelform),
    path('manage/list/',manage.manage_list),
    path('manage/add/',manage.manage_add),

]
