from django.http import HttpResponse
import os

file_path = os.path.abspath(__file__)
pro_dir = os.path.dirname(file_path)
dir_path = os.path.dirname(pro_dir)


def html_res(request):
    file_addr = os.path.join(dir_path,'sam.html')
    fp = open(file_addr,'r')
    data = fp.read()
    return HttpResponse(data)