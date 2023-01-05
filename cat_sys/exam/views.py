from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from exam import models

# 学生登录
def studentLogin(request):
    if request.method == 'POST':
        # 提取表单信息
        sid = request.POST.get('sid')
        pwd = request.POST.get('pwd')

        # 通过学号获取该学生实体
        student = models.Student.objects.get(sid=sid)

        if pwd == student.pwd: #密码匹配登录成功
            request.session['username'] = sid
            request.session['is_login'] = True

            return render(request, 'index.html', {'student': student})
        else:
            return render(request,'login.html',{'message':'密码错误！'})
    
    elif request.method == 'GET':
        return render(request, 'login.html')
    
    else:
        return HttpResponse("请使用GET或POST请求数据！")


def index(request):
    return render(request,'index.html')
'''
    if request.session.get('is_login',None):
        username = request.session.get('username',None)

        return render(request, 'index.html', {'student':student})
    
    else:
        return render(request,'index.html')
'''

def studentLogout(request):
    request.session.clear()
    url = reverse('exam:index')
    return redirect(url)
