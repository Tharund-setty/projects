from django.shortcuts import render
from django.http import HttpResponse
import os

file_path = os.path.abspath(__file__)
pro_dir = os.path.dirname(file_path)
dir_path = os.path.dirname(pro_dir)


# Create your views here.

def stext(request):
    return HttpResponse("<marquee><h1>HELLO GOOD MORNING WELCOME TO HOME PAGE</h1></marquee>")

def html_res(request):
    file_addr = os.path.join(dir_path,'sam.html')
    fp = open(file_addr,'r')
    data = fp.read()
    return HttpResponse(data)

def ren(request):
    return render(request,"sample.html")

def ren(request):
    return render(request,'sample.html')
