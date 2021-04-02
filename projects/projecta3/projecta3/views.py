from django.http import HttpResponse
from django.shortcuts import render

def ren(request):
    return render(request,"sample.html")