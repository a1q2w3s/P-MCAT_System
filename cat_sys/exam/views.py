# coding=utf8
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from exam import models

import numpy
import pyRserve
conn = pyRserve.connect(host='101.201.149.12')

# 学生登录
def studentLogin(request):
    if request.method == 'POST':
        # 提取表单信息
        sid = request.POST.get('sid')
        # 通过学号获取该学生实体
        try:
            student = models.Student.objects.get(sid=sid)
            request.session['username'] = sid
            request.session['is_login'] = True
            paper = student.test_set.all()
            return render(request, 'index.html', {'student': student,'paper':paper})
        except:
            return render(request,'login.html',{'message':'考生号错误！请核对后重新输入！'})
    
    elif request.method == 'GET':
        return render(request, 'login.html')
    
    else:
        return HttpResponse("请使用GET或POST请求数据！")


def index(request):

    if request.session.get('is_login',None):
        username = request.session.get('username',None)
        student = models.Student.objects.get(sid=username)
        
        paper = student.test_set.all()
        return render(request, 'index.html', {'student':student,'paper':paper})
    
    else:
        return render(request,'index.html')


def studentLogout(request):
    request.session.clear()
    url = reverse('exam:index')
    return redirect(url)


def userfile(request):
    if request.session.get('is_login',None):  #若session认证为真
        username =request.session.get('username',None)
        student =models.Student.objects.get(sid=username)
        return render(request, 'userfile.html',{'student': student})


def startExam(request):
    if request.session.get('is_login',None):  #若session认证为真
        username = request.session.get('username',None)
        student = models.Student.objects.get(sid=username)

        paper = request.GET.get('tid',None)

        temp = 100
        item = conn.r(f'round(runif(1)*{temp})')
        title = models.Item.objects.filter(iid=item+380).values_list('title')[0][0]
        
        return render(request,'startExam.html',{'student':student.sid,'title':title})