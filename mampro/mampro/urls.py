"""mampro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views

"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from testapp import views
#from mampro import testapp
urlpatterns = [
    path('admin/', admin.site.urls),
    #url(r'^admin/', admin.site.urls),
    #url(r'^testapp/', include('testapp.urls')),
    #path('testapp/',include('testapp.urls')),
    path('', views.student, name='student'),
    path('college/', views.college, name='college'),
    path('(?P<stu_id>[0-9]+)/',views.college ,name='college'),
]

    #url(r'^(?P<stu_id>[0-9]+)/$',views.College ,name='College'),

