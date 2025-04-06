'''
把所有的modelform封装到此
'''
from app01.models import *
from django.core.exceptions import ValidationError
from django import forms
from app01.utils.bootstrap import BootstrapModelForm,BootStrapForm
from app01.utils.encrypt import md5
from captcha.fields import CaptchaField
# # form方式
# class MyForm(forms.Form):
#     user = forms.CharField(widget=forms.Textarea)
#     pwd = forms.CharField(widget=forms.Textarea)
# def user_add(request):
#     form = MyForm()
#     return render(request,'user_add.html',{'form':form})
# 前端代码改为：
#     <form method='post'>
#         {% for filed in form %}
#             {{ field }}
#         {% endfor %}
#     </form>

# ModelForm 注意返回值问题具体去models中修改类的实例
class UserModelForm(BootstrapModelForm):
    '''
    使用了继承自定义的BootstrapModelForm类 在utilis中
    '''
    class Meta:
        # model为指定的数据库类  fields为要显示的属性 widgets为应用的样式
        model = UserInfo
        # 可以用下述替换为所有 fields = ['name','password','age','account','create_time','gender','depart']
        # 也可以exclude = ['name'] 排除一个
        fields = '__all__'

class PrettyModelForm(BootstrapModelForm):
    # # 验证方式1：使用正则表达式来就行校验
    # mobile = forms.CharField(
    #     label='手机号',
    #     validators=[RegexValidator(r'^1[3-9]\d{9}$','手机号格式错误')]
    # )
    class Meta:
        model = PrettyNum
        fields = '__all__'
#     验证方式2:modelform自带的功能 clean_字段名
    def clean_mobile(self):
        txt_mobile = self.cleaned_data['mobile']
        if len(txt_mobile) != 11:
            raise ValidationError('手机号格式错误')
        elif PrettyNum.objects.filter(mobile=txt_mobile).exists():
            # elif PrettyNum.objects.exclude(id=self.instance.pk).exists(): 为排除当前id的手机号存在 用于编辑中修改手机号情况
            raise ValidationError('手机号已存在')
        return txt_mobile


class PrettyEditModelForm(BootstrapModelForm):
    # 重写的prettymodelform类 使得mobile不能修改
    mobile = forms.CharField(disabled=True,label='手机号')
    class Meta:
        model = PrettyNum
        fields = '__all__'

class AdminModelForm(BootstrapModelForm):
    confirm_password = forms.CharField(label='请确认密码',
                                       widget=forms.PasswordInput)

    class Meta:
        model = Admin
        fields = ['username','password','confirm_password']
        widgets = {
            'password':forms.PasswordInput
        }
    def clean_password(self):
        '''
        自定义的md5加密 在encrypt中
        @return:
        '''
        pwd = self.cleaned_data.get('password')
        return md5(pwd)

    def clean_confirm_password(self):
        pwd = self.cleaned_data.get('password')
        confirm = md5(self.cleaned_data.get('confirm_password'))
        if confirm != pwd:
            raise ValidationError('密码不一致')
        return confirm

class AdminEditModelForm(BootstrapModelForm):
    class Meta:
        model = Admin
        fields = ['username']

class AdminResetModelForm(BootstrapModelForm):
    confirm_password = forms.CharField(label='请确认密码',
                                       widget=forms.PasswordInput)
    class Meta:
        model = Admin
        fields = ['password','confirm_password']
        widgets = {
            'password': forms.PasswordInput
        }
    def clean_password(self):
        '''
        自定义的md5加密 在encrypt中
        @return:
        '''
        pwd = self.cleaned_data.get('password')
        md5_pwd = md5(pwd)
        # 去数据库校验修改前后密码是否一致 pk为primarykey
        exist = Admin.objects.filter(id=self.instance.pk,password=md5_pwd).exists()
        if exist:
            raise ValidationError('密码不能与之前一致')
        return md5_pwd
    def clean_confirm_password(self):
        pwd = self.cleaned_data.get('password')
        confirm = md5(self.cleaned_data.get('confirm_password'))
        if confirm != pwd:
            raise ValidationError('密码不一致')
        return confirm

# form做法  由于登陆不需要增上改查 form实现简单 继承自定义的类组件
class LoginForm(BootStrapForm):
    un = forms.CharField(
        label='用户名',
        widget=forms.TextInput
    )
    pwd = forms.CharField(
        label='密码',
        widget=forms.PasswordInput(render_value=True) #rendervalue使提交失败返回后默认值保留
    )
    # 验证码注意需要去auth中调整下中间件 不然不显示图片 验证码直接通过form来判断是否正确就行了
    cap = CaptchaField(
        label='图片验证码',
        required=True,
        error_messages={
            'required': '验证码不能为空',
            'invalid':'验证码错误'
        }
    )
    def clean_pwd(self):
        pwd = self.cleaned_data.get('pwd')
        return md5(pwd)
# # modelform
# class LoginModelForm(forms.ModelForm):
#     class Meta:
#         model = models.Admin
#         fields = ['username','password']

class TaskModelForm(BootstrapModelForm):
    class Meta:
        model = Task
        fields = '__all__'

class OrderModelForm(BootstrapModelForm):
    class Meta:
        model = Order
        # fields = '__all__'
        exclude = ['oid','admin']

class UpForm(BootStrapForm):
    bootstrap_exclude_fields = ['img']
    name = forms.CharField(label='姓名')
    age = forms.IntegerField(label='年龄')
    img = forms.FileField(label='头像')

class UpModelForm(BootstrapModelForm):
    bootstrap_exclude_fields = ['img']
    class Meta:
        model = Manager
        fields = '__all__'


