from django.shortcuts import render
from django.http import HttpResponse

def index(request): 
    print('blog')
    return HttpResponse('blog')