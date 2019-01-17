
from django.http import HttpResponse

from django.shortcuts import render,reverse
import json

def tologin(request):
    return  render(request,'login.html')


def login(request):
    name = request.GET.get('name')
    name1 = request.POST.get('name')
    print(request.method)
    print(name)
    print(name1)
    data={
    'name':name
    }
    return  HttpResponse(json.dumps(data), content_type="application/json")