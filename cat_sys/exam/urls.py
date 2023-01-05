from django.contrib import admin
from django.urls import path, re_path
from exam import views

urlpatterns = [
    re_path(r'^$',views.index),
    path('index/',views.index,name='index'),
    path('studentLogin/',views.studentLogin,name='studentLogin'),
    path('studentLogout/',views.studentLogout,name='studentLogout'),
]
