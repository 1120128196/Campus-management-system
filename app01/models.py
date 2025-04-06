from django.db import models

# Create your models here.

class Admin(models.Model):
    '''
    管理员
    '''
    username = models.CharField(verbose_name='用户名',max_length=32)
    password = models.CharField(verbose_name='密码',max_length=64)

    def __str__(self):
        return self.username
class Department(models.Model):
    """" 部门表 verbose_name 是备注 """
    # id = models.BigAutoField(verbose_name='ID',primary_key=True) 默认有可不写
    title = models.CharField(verbose_name='部门标题',max_length=32)

#     由于ModelForm自动返回的对象而不是对象内的title 需要手动设置
    def __str__(self):
        return self.title

class UserInfo(models.Model):
    """ 员工表"""
    name = models.CharField(verbose_name='姓名',max_length=16)
    password = models.CharField(verbose_name='密码',max_length=64)
    age = models.IntegerField(verbose_name='年龄')
    account = models.DecimalField(verbose_name='账户余额',max_digits=10,decimal_places=2,default=0)
    # create_time = models.DateTimeField(verbose_name='入职时间')
    create_time = models.DateField(verbose_name='入职时间')
    # 约束
    gender_choices = (
        (1,'男'),
        (2,'女'),
    )
    gender = models.SmallIntegerField(verbose_name='性别',choices=gender_choices)

    # 外键 django内部会自动把列名变为depart_id cascade为级联删除
    depart = models.ForeignKey(verbose_name='学院',to='Department',to_field='id',on_delete=models.CASCADE)
    # 下面一种是外键id删除了 关联的置空
    # depart = models.ForeignKey(to='Department',to_field='id',on_delete=models.SET_NULL,null=True,blank=True)

class PrettyNum(models.Model):
    """ 账号管理"""
    # 手机号最好用字符串charfield 由于后续需要正则表达 默认情况不允许为空 可以通过null=True black=Truei
    mobile = models.CharField(verbose_name='手机号',max_length=12)
    price = models.IntegerField(verbose_name='价格',default=0)
    level_choice = (
        (1,'1级'),
        (2,'2级'),
        (3,'3级'),
        (4,'4级'),
    )
    level = models.SmallIntegerField(verbose_name='级别',choices=level_choice,default=1)
    status_choice = (
        (1,'已占用'),
        (2,'未占用'),
    )
    status = models.SmallIntegerField(verbose_name='状态',choices=status_choice,default=2)

class Task(models.Model):
    ''' 任务'''
    level_choice = (
        (1,'紧急'),
        (2,'重要'),
        (3,'临时'),

    )
    level = models.SmallIntegerField(verbose_name='级别',choices=level_choice,default=3)
    title = models.CharField(verbose_name='标题',max_length=64)
    detail = models.TextField(verbose_name='详细信息')
    user = models.ForeignKey(verbose_name='负责人', to='Admin',on_delete=models.CASCADE)

class Order(models.Model):
    ''' 订单'''
    oid = models.CharField(verbose_name='订单号',max_length=64)
    title = models.CharField(verbose_name='名称',max_length=32)
    price = models.IntegerField(verbose_name='价格')

    status_choices = (
        (1,'待支付'),
        (2,'已支付'),
    )
    status = models.SmallIntegerField(verbose_name='状态',choices=status_choices,default=1)
    admin = models.ForeignKey(verbose_name='管理员',to='Admin',on_delete=models.CASCADE)

class Teacher(models.Model):
    ''' 教师'''
    name  = models.CharField(verbose_name='姓名',max_length=32)
    age = models.IntegerField(verbose_name='年龄')
    img = models.CharField(verbose_name='头像',max_length=128)

class Manager(models.Model):
    ''' 教师'''
    name  = models.CharField(verbose_name='名称',max_length=32)
    count = models.IntegerField(verbose_name='年龄')
    # Filefield本质上也是Charfield  但区别是可以自己保存数据 upload指定文件上传位置 media下
    img = models.FileField(verbose_name='Logo',max_length=128,upload_to='city/')