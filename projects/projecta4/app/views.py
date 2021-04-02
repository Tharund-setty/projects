from django.shortcuts import render
from django.http import HttpResponse


# Create your views 

def ren(request):
    return render(request,'sample.html')
