# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

"""
# 1:
def hello(request):
    return HttpResponse('<h1>Hello, maizi</h1>')
"""


# 2:
def hello(request, offset):
    return HttpResponse('<h1>Hello, maizi: %s</h1>' % offset)