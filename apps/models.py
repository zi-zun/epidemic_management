from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=20, primary_key=True, unique=True, null=False, verbose_name='用户名')
    password = models.CharField(max_length=32, null=False, verbose_name='登录密码')
    real_name = models.CharField(max_length=500, verbose_name='真实姓名')
    tel = models.CharField(max_length=11, unique=True, verbose_name='电话号码')
    random_code = models.IntegerField(max_length=20)
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()

    class Meta:
        db_table = 'user'           # 表名

class Administrator(models.Model):
    username = models.CharField(max_length=20, primary_key=True, unique=True, null=False, verbose_name='用户名')
    password = models.CharField(max_length=32, null=False, verbose_name='登录密码')
    real_name = models.CharField(max_length=500, verbose_name='真实姓名')
    tel = models.CharField(max_length=11, unique=True, verbose_name='电话号码')
    random_code = models.IntegerField(max_length=20)
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()

    class Meta:
        db_table = 'administrator'  # 表名
