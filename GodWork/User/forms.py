#coding:utf-8
from django import forms

class RegisterForm(forms.Form):
	username = forms.CharField(max_length=64,label="用户名称",widget=forms.TextInput(attrs={'class':'form-control'}))
	password = forms.CharField(max_length=64,label="用户密码",widget=forms.TextInput(attrs={'class':'form-control'}))
	email = forms.EmailField(label="用户邮箱",widget=forms.TextInput(attrs={'class':'form-control'}))
	phone = forms.IntegerField(required=False,label="手机",widget=forms.TextInput(attrs={'class':'form-control'}))
	photo = forms.ImageField(required=False,label="照片")

	def clean_username(self):
		username = self.cleaned_data.get("username","")
		if len(username)<6 and username:
			raise forms.ValidationError("用户名必须大于六位")
		if not username.isalnum() and username:
			raise forms.ValidationError("用户名不能带有特殊符号")
		return username
	
	def clean_password(self):
		password = self.cleaned_data.get("password","")
		if len(password)<6 and password:
			raise forms.ValidationError("密码必须大于六位")
		return password			