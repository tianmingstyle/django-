#coding:utf-8
from django.db import models

# Create your models here.
class User(models.Model):
	username = models.CharField(max_length=64,verbose_name="用户名称")
	password = models.CharField(max_length=64,verbose_name="用户密码")
	email = models.EmailField(verbose_name="用户邮箱")
	phone = models.CharField(max_length=64,verbose_name="手机",blank=True,null=True)
	photo = models.ImageField(upload_to="images/userphoto",verbose_name="用户头像" ,blank=True,null=True)

class Group(models.Model):
	name = models.CharField(max_length=64,verbose_name="组名称")

class Method(models.Model):
	name = models.CharField(max_length=64,verbose_name="权限名称")		