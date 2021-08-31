#from myproject.views import sample2
#from django import http
from django.http import request, response
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def sample1(request):
    return render(request,"sample.html",context={"Name":"Prashanth","Age": 24,"Gender":"Male"})

def login(request):
    return render(request,"login.html",{"user_login":False})

def fruites(request):
    return render(request,"login.html",{"fruites":["Apple","Banana","Orange","Mango"]})

def greatest(request,a,b,c,d):
    res = 0
    if a > b:
        if a > c:
            if a > d:
                res = a
            else:
               res = d
    else:
        if b > c:
            if b > d:
                res = b
            else:
                res = d
        else:
            if c > d:
                res = c
            else:
                res = d
    return render(request,"greatest_number.html",{"Answer":res,"a":a,"b":b,"c":c,"d":d})
                
def emp(request,name,phno,email,dsig,sal):

    return render(request,"emp_detailes.html",{"name":name,"phno":phno,"email":email,"dsig":dsig,"sal":sal})