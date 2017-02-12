from django.shortcuts import render_to_response
from django.http import JsonResponse
from Service.models import *
import paramiko
import re

# Create your views here.

def saveData(request):
	result={}
	if request.method == 'POST' and request.POST:
		req_data = request.POST
		service = Service()
		service.host = req_data.get('hostName')
		service.ip = req_data.get('Ip')
		service.mac = req_data.get('mac')
		service.cpu = req_data.get('cpu')
		service.mem = req_data.get('mem')
		service.disk = req_data.get('Disk')
		service.system = req_data.get('system')
		service.model = req_data.get('model')
		service.save()
		result['status']='success'
	else:
		result['status']='error'	
	return JsonResponse(result)

def setcpu(request):
    command = request.GET.get("command")
    ipaddr = request.GET.get("ipaddr")
    userId = request.GET.get("userId")
    port = int(request.GET.get("port", 22))
    serverId = request.GET.get("serverId")

    stdin,stdout,stderr = parApi(command,userId,ipaddr,port)

    for num,line in enumerate(stdout.readlines()):
        line = line.strip()
        if num >= 2:
            cupIDLE = re.split(r"\s+",line)[-3]
            cpu_used = 100-int(cupIDLE)
            cpu = CpuData()
            cpu.serviceid = serverId
            cpu.cpuload = cpu_used
            cpu.time = datetime.datetime.now()
            cpu.save()
        else:
            pass
    return JsonResponse({"statue":"success"})

def parApi(command,user_id,ip,port=22):
	client = paramiko.SSHClient()
	client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	user = ServiceUser.objects.get(id=user_id)
	client.connect(ip,port,use.serviceUsername,use.servecePasswd)
	return client.exec_command(command)

def runCommand(request):
    command = request.GET.get("command")
    ipaddr = request.GET.get("ipaddr")
    userId = request.GET.get("userId")
    port = int(request.GET.get("port", 22))
    serverId = request.GET.get("serverId")
    stdin, stdout, stderr = parApi(command, userId, ipaddr, port)
    data = stdout.read()
    print data
    return JsonResponse({"status":"success"})

def test(request):
    result = {"state":""}
    if request.method == "GET" and request.GET:
        result["state"] = "GET"
    else:
        result["state"] = "POST"
    return JsonResponse(result)	