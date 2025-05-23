from django.db import models


# Create your models here.
class Admin(models.Model):
    username = models.CharField(verbose_name='姓名', max_length=32)
    password = models.CharField(verbose_name='密码', max_length=64)

    def __str__(self):
        return self.username


class Department(models.Model):
    title = models.CharField(verbose_name='部门', max_length=32)

    def __str__(self):
        return self.title


class Employee_Table(models.Model):
    name = models.CharField(verbose_name='姓名', max_length=16)
    age = models.IntegerField(verbose_name='年龄')
    gender = models.CharField(verbose_name='性别', max_length=8)
    salary = models.DecimalField(verbose_name='薪水', max_digits=10, decimal_places=2, default=0)
    date = models.DateField(verbose_name='入职日期')
    #                                                                                 on_delete = models.SET_NULL是没有部门的时候直接删除
    depart = models.ForeignKey(verbose_name='部门', to='Department', to_field='id', null=True, blank=True,
                               on_delete=models.SET_NULL)


class Telephone_User(models.Model):
    mobile = models.CharField(verbose_name='电话号', max_length=11)
    price = models.DecimalField(verbose_name='价格', max_digits=15, decimal_places=2, default=0)
    level_choices = (
        (1, '一级'),
        (2, '二级'),
        (3, '三级'),
        (4, '四级')
    )
    level = models.SmallIntegerField(verbose_name='级别', choices=level_choices, default=1)
    status_choices = (
        (1, '已出售'),
        (2, '未出售'),
    )
    status = models.SmallIntegerField(verbose_name='状态', choices=status_choices, default=1)


class Task(models.Model):
    level_choices = (
        (1, '一级'),
        (2, '二级'),
        (3, '三级'),
    )
    level = models.SmallIntegerField(verbose_name='级别', choices=level_choices, default=1)
    name = models.CharField(verbose_name='任务名称', max_length=100)
    description = models.TextField(verbose_name='任务描述')
    user = models.ForeignKey(verbose_name='接收人', to='Admin', on_delete=models.CASCADE)


class Order(models.Model):
    user = models.ForeignKey(verbose_name='任务处理者', to='Admin', on_delete=models.CASCADE)
    name = models.CharField(verbose_name='商品名称', max_length=64)
    price = models.DecimalField(verbose_name='价格', max_digits=15, decimal_places=2, default=0)
    content = (
        (1, '未出售'),
        (2, '已出售'),
    )
    sale_situation = models.SmallIntegerField(verbose_name='出售情况', choices=content, default=1)
