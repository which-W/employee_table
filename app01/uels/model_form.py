from django import forms
from django.core.validators import RegexValidator  # 正则表达式的使用函数
from app01.uels.bootstrap import Father_modelform
from app01 import models
from app01.uels.pwd_md5 import md5_pwd


class Userinfo_form(Father_modelform):
    class Meta:
        model = models.Employee_Table
        fields = ['name', 'age', 'gender', 'salary', 'date', 'depart']


class Telephone_form(Father_modelform):
    mobile = forms.CharField(
        label='电话号',
        validators=[RegexValidator(r'^1[3-9]\d{9}$', '号码格式不对')]
    )

    class Meta:
        model = models.Telephone_User
        fields = ['mobile', 'price', 'level', 'status']


# 定义Admin_form类，继承自forms.ModelForm
class Admin_form(Father_modelform):
    # 定义confirm_password字段，用于确认密码
    confirm_password = forms.CharField(label='确认密码', widget=forms.PasswordInput(render_value=True))
    password = forms.CharField(label='输入密码', widget=forms.PasswordInput(render_value=True))

    # 定义Meta类，继承自Father_modelform
    class Meta:
        # 指定model为models.Admin
        model = models.Admin
        # 指定字段为username, password, confirm_password
        fields = ['username', 'password', 'confirm_password']

    def clean_password(self):
        pwd = self.cleaned_data['password']
        pwd = md5_pwd(pwd)
        return pwd

    def clean_confire_password(self):
        pwd = self.cleaned_data['password']
        t_pwd = md5_pwd(self.cleaned_data['confirm_password'])
        if pwd != t_pwd:
            raise forms.ValidationError('两次密码不一致')
        return t_pwd


class Admin_change(Father_modelform):
    confirm_password = forms.CharField(label='确认密码', widget=forms.PasswordInput(render_value=True))
    password = forms.CharField(label='输入密码', widget=forms.PasswordInput(render_value=True))

    class Meta:
        model = models.Admin
        fields = ['password', 'confirm_password']

    def clean_password(self):
        pwd = self.cleaned_data['password']
        pwd = md5_pwd(pwd)
        pwd_same = models.Admin.objects.filter(id=self.instance.pk, password=pwd).exists()
        if pwd_same:
            raise forms.ValidationError('不能输入一样的密码')
        return pwd

    def clean_confire_password(self):
        pwd = self.cleaned_data['password']
        t_pwd = md5_pwd(self.cleaned_data['confirm_password'])
        if pwd != t_pwd:
            raise forms.ValidationError('两次密码不一致')
        return t_pwd

class OrderModel(Father_modelform):
    class Meta:
        model = models.Order
        # fields = "__all__"
        exclude = ["user"]