"""mampro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views

"""
from django.contrib import admin
from django.urls import path
#from django.conf.urls import include
from testapp import views
#from mampro import testapp
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.student, name='student'),
    path('college/', views.college, name='college'),
    path('hii/<int:stu_id>/',views.college ,name='college'),
]

