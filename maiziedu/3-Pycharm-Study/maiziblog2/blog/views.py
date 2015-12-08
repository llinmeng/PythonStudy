# -*- coding: utf-8-*-
from django.shortcuts import render
from django.http import HttpResponse
from blog.models import *
from datetime import *

# Create your views here.
# 1:
"""
def hello(request):
    return HttpResponse('<h1> Hello maizi. </h1>')
"""


# 2:
def hello(request):
    name = 'MAIzi'
    age = 18
    return render(request, 'hello.html', locals())


# 3:
def index(request):
    d = date.today()
    articles = Article.objects.all()
    return render(request, 'index.html', locals())


def article(request, pid):
    article = Article.objects.get(id = pid)
    return render(request, 'article.html', locals())