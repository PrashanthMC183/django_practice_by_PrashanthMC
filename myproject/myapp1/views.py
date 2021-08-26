#from myproject.views import sample2
from django import http
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def sample1(request):
    return render(request,"sample.html",context={"Name":"Prashanth","Age": 24,"Gender":"Male"})

def login(request):
    return render(request,"login.html",{"user_login":False})

def fruites(request):
    return render(request,"login.html",{"fruites":["Apple","Banana","Orange","Mango"]})