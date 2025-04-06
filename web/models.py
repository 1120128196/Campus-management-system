#  数据库  自动把类转换为 SQL语句（ORM） migrations为自动生成的数据库迁移记录
from django.db import models

# Create your models here.

class UserInfo(models.Model):
    name = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    age = models.IntegerField(default=18)
"""
注意 连接数据库要先在settings中修改database信息 django中需要安装mysqlclient模块 注意版本问题

相当于自动执行sql语句 
create table web_userinfo(
id bigint auto_increment primary key， id是自动生成的
name varchar(32),
password varchar(64),
age int
)

通过控制行分别执行 python manage.py makemigrations 与python manage.py migrate 命令创建删除数据库
删除就直接注释了在执行一趟命令  修改表时候注意新增列需要默认赋值（指定空值也行） 删除列直接注释
"""

class Department(models.Model):
    title = models.CharField(max_length=16)
#
# class Role(models.Model):
#     caption = models.CharField(max_length=16)



