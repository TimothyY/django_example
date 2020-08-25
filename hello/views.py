from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import requests

def homePageView(request):
    server_ip = requests.get("https://httpbin.org/ip").json()['origin']
    return HttpResponse('Hello, World! This is '+ server_ip +' speaking')