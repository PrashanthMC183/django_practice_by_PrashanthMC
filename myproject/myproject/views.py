from django.http import HttpResponse
from django.shortcuts import render

#def Sample(request):
    #return HttpResponse('<h1>I am Inevitable </h2>')

def sample2(request):
    return render(request,"sample.html")

def form(request):
    return render(request,"index.html")