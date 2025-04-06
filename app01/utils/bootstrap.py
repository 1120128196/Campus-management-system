'''
创建个子类 之后的modelform直接继承就行了  简化步掫
'''
from django import forms

# 使用多态 可以继承多个父类 注意子类引用时候 把BootStrap类放到首位
class BootStrap:
    # 设置一个排除字段  在这里面的字段将不进行样式变化 可以在创建form/modelform时候定义
    bootstrap_exclude_fields = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            if name in self.bootstrap_exclude_fields:
                continue
            if name == 'create_time':
                field.widget.input_type = 'date'
            #     设置小数点
            if name == 'account':
                field.widget.attrs = {'step': '0.01', 'class': 'form-control'}
            # 字段中有属性时候保留原来属性 没有属性才完全修改
            if field.widget.attrs:
                field.widget.attrs['class'] = 'form-control'
                field.widget.attrs['placeholder'] = field.label
            else:
                field.widget.attrs = {'class': 'form-control', 'placeholder': field.label}


class BootstrapModelForm(BootStrap,forms.ModelForm):
    # class Meta:
    #     # model为指定的数据库类  fields为要显示的属性 widgets为应用的样式
    #     model = UserInfo
    #     # 可以用下述替换为所有 fields = ['name','password','age','account','create_time','gender','depart']
    #     # 也可以exclude = ['name'] 排除一个
    #     fields = '__all__'
    #
    #     # 样式调整
    #     # widgets = {
    #     #     'name': forms.TextInput(attrs={'class':'form-control'}),
    #     #     'password': forms.TextInput(attrs={'class':'form-control'}),
    #     #     'age': forms.TextInput(attrs={'class':'form-control'})
    #     # }
    #     # widgets = {
    #     #     'create_time' : forms.DateInput(attrs={'type':'date'})
    #     # }
    # #可以通过类的初始化循环来添加样式 上面是单独把createtime的输入样式

    '''
    在该类中直接写初始化init内容就行了 别的属性调用使用在自定义  目的是把bootstrap样式提前封装好
    '''

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     for name, field in self.fields.items():
    #         if name == 'create_time':
    #             field.widget.input_type = 'date'
    #         #     设置小数点
    #         if name == 'account':
    #             field.widget.attrs = {'step': '0.01', 'class': 'form-control'}
    #         # 字段中有属性时候保留原来属性 没有属性才完全修改
    #         if field.widget.attrs:
    #             field.widget.attrs['class'] = 'form-control'
    #             field.widget.attrs['placeholder'] = field.label
    #         else:
    #             field.widget.attrs = {'class': 'form-control', 'placeholder': field.label}
    pass


# form也可以继承样式 但form不能继承modelform的
class BootStrapForm(BootStrap,forms.Form):
    pass