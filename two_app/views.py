#coding=utf-8
from django.shortcuts import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,render_to_response
from models import WebUser
from models import User
from django import forms
from django.template import RequestContext

# Create your views here.

class UserForm(forms.Form):
    username = forms.CharField(label='用户名',max_length=100)
    password = forms.CharField(label='密码',widget=forms.PasswordInput())

def regist(req):
    if req.method == 'POST':
        uf = UserForm(req.POST)
        if uf.is_valid():
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            #添加到数据库

            User.objects.create(username= username,password=password)
            #return HttpResponse('regist success!!')
            return HttpResponseRedirect('/2/login/')
    else:
        uf = UserForm()
    return render_to_response('register.html',{'uf':uf}, context_instance=RequestContext(req))

#登陆
def login(req):
    if req.method == 'POST':
        uf = UserForm(req.POST)
        if uf.is_valid():
            #获取表单用户密码
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            #获取的表单数据与数据库进行比较
            user = User.objects.filter(username=username, password=password).count()
            if user:
                #比较成功，跳转inde
                req.session["username"] = username
                return HttpResponseRedirect('/2/index/')
            else:
                #比较失败，还在login
                return HttpResponseRedirect('/2/login/')
    else:
        uf = UserForm()
    return render_to_response('login.html',{'uf':uf},context_instance=RequestContext(req))

#登陆成功
def index(request):
    ip = request.environ.get('REMOTE_ADDR', None)
    user = request.session.get("username",None)
    print(user)
    web_user, created = WebUser.objects.get_or_create(ip=ip)
    if not created:
        web_user.pv += 1
        web_user.save()
    return render(request, '2.html', {'data': web_user,"user":user})

def logout(req):
    response = HttpResponse('logout !!')
    return response