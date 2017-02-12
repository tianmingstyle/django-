#coding:utf-8
from django.shortcuts import render_to_response
from User.forms import *
from User.models import *
from Service.models import *
from django.http import HttpResponseRedirect
import hashlib
#from django.contrib.auth.decorators import login_required 




def login_valid(func):
	def inner(request,*args,**kwargs):
		try:
			username = request.session['username']
			return func(request,*args,**kwargs)
		except KeyError as e:
			if repr(e) == "KeyError('username',)":
				error = '当前用户未登陆请登陆'
			else:
				error = str(e)
			url = '/404/'+error
			return HttpResponseRedirect(url)		
	return inner		

@login_valid
def index(request):
	return render_to_response('index.html',locals())

@login_valid
def base(request):
	return render_to_response('base.html',locals())	

def user_valid(username,password):
	try:
		user = User.objects.get(username=username)
		if user.password == hashpasswd(password):
			return True
		else:
			return False
	except:
		return False	

def login(request):
	result = {}
	if request.method == "POST" and request.POST:
		username = request.POST.get("username","")
		password = request.POST.get("password","")
		if username and password and user_valid(username,password):
			response = HttpResponseRedirect("/index")
			response.set_cookie("username",username)
			request.session["username"] = username
			return response
		else:
			result["error"] = "用户或者密码错误"
			return render_to_response("login.html", locals())
	else:
		return render_to_response('login.html',locals())	

def hashpasswd(pw):
	m = hashlib.md5()
	m.update(pw)
	return m.hexdigest()

def user_exist(username):
	try:
		User.objects.filter(username=username)
		return True
	except:
		return False

		
	
@login_valid
def register(request):
	statue = "用户注册"
	if request.method == 'POST' and request.POST:
		registerForms = RegisterForm(request.POST)
		if registerForms.is_valid():
			clean_data = registerForms.cleaned_data
			u = User(
				username = clean_data.get("username"),
				password = hashpasswd(clean_data.get("password")),
				email = clean_data.get("email"),
				phone = clean_data.get("phone"),
				photo = clean_data.get("photo")

			)
			u.save()
			del request.COOKIES["username"]
			del request.session["username"]
			return HttpResponseRedirect("/login")
	else:
		registerForms = RegisterForm()
	return render_to_response("register.html",locals())

def logout(request):
	del request.COOKIES["username"]
	del request.session["username"]
	return render_to_response("logout.html",locals())	

def forbidden(request,error):
	return render_to_response('404.html',locals())	

def listUser(request):
	statue="用户列表信息"
	user_list = User.objects.all()
	return render_to_response("listuser.html",locals())