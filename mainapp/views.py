# from django.shortcuts import render
from django.http import HttpResponse


def hello(request):
    return HttpResponse('Hello world!')

def blog(request):
    return HttpResponse('I am blog!')

def funk(request, **kwargs):
    return HttpResponse(f'{kwargs}')


