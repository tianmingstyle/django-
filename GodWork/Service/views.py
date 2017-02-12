#coding:utf-8
from django.shortcuts import render_to_response
from models import *
from GodWork.views import *
# Create your views here.

@login_valid
def list(request):
    statue = "server展示页"
    table_list=Service.objects.all()
    return render_to_response("list.html", locals())

@login_valid
def content(request,ids):
    host_data={}
    hostinfo = Service.objects.get(id=int(ids))
    user_list = ServiceUser.objects.filter(serviceid=int(ids))
    statue = "Details of %s"%hostinfo.host
    host_data["host_name"] = hostinfo.host
    host_data["ip"] = hostinfo.ip
    host_data["mac"] = hostinfo.mac
    host_data["mem"] = hostinfo.mem
    host_data["disk"] = hostinfo.disk
    host_data["system"] = hostinfo.system
    host_data["model"] = hostinfo.model
    host_data["cpu"] = hostinfo.cpu
    return render_to_response("server_content.html",locals())	