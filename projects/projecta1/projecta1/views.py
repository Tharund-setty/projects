from django.http import HttpResponse

def stext(request):
    return HttpResponse("<marquee><h1>HELLO GOOD MORNING WELCOME TO HOME PAGE</h1></marquee>")
