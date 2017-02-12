#coding:utf-8
from django.db import models

# Create your models here.
class Service(models.Model):
	host = models.CharField(max_length=256,verbose_name="主机名称")
	ip = models.CharField(max_length=128,verbose_name="主机ip")
	mac = models.CharField(max_length=128,verbose_name="mac")
	cpu = models.CharField(max_length=256,verbose_name="cpu")
	mem = models.CharField(max_length=128,verbose_name="内存")
	disk = models.CharField(max_length=128,verbose_name="硬盘")
	system = models.CharField(max_length=128,verbose_name="系统")
	model = models.CharField(max_length=128,verbose_name="服务器型号")

class ServiceUser(models.Model):
	serviceid = models.IntegerField(verbose_name="服务器id")	
	serviceUsername = models.CharField(max_length=128,verbose_name="服务器用户名称")
	servecePasswd = models.CharField(max_length=128,verbose_name="服务器用户密码")
	def __unicode__(self):
		return self.serviceUsername
		
class CpuData(models.Model):
	serviceid = models.IntegerField(verbose_name="服务器id")
	cpuload = models.IntegerField(verbose_name="cpu使用率")
	time = models.DateTimeField(verbose_name="监控的时间")