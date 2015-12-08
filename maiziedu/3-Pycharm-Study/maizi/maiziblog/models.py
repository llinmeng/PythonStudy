# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.


class Author(models.Model):                                # 默认的继承类
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=18)


class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    url = models.URLField()
    portal = models.ImageField()
    author = models.ForeignKey(Author)                      # 外键: 可以一对多, 多对一, 一对一关系
    # 代码读取顺序从上至下, 因此, Author需在Article的上方


