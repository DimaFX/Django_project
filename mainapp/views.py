# from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View       # для классов


class HelloView(View):
    def get(self, *args):
        return HttpResponse('Hello world')


""" def hello(request):
    return HttpResponse('Hello world!') """


def funk(request, **kwargs):
    return HttpResponse(f'{kwargs}')


