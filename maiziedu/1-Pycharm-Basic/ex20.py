# -*- coding: utf-8 -*-
"""
面向对象编程
    Python支持面向对象编程

    类(class): 现实世界中一些事物的封装(如：学生)
    类：属性 (如: 名字, 成绩)

    类对象
    实例对象

    引用: 通过引用对类的属性和方法进行操作
    实例化: 创建一个类的具体实例对象(如：学生张三)

装饰器(decorator)
"""


# 1:

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def introduce(self):
        print "Hi, I'm " + self.name
        print "my grade is: " + str(self.grade)

jim = Student("jim", 86)
jim.introduce()


# 2:
def add_candles(cake_func):
    def insert_candles():
        return cake_func() + " candles"
    return insert_candles()


def make_cake():
    return "cake"

gift_func = add_candles(make_cake)

print make_cake()
print gift_func


# 2-2:
def add_candles(cake_func):
    def insert_candles():
        return cake_func() + " candles"
    return insert_candles()


def make_cake():
    return "cake"

make_cake = add_candles(make_cake)

print make_cake
print gift_func


# 2-3:
def add_candles(cake_func):
    def insert_candles():
        return cake_func() + " and candles"
    return insert_candles


@add_candles
def make_cake():
    return "cake"
# make_cake = add_candles(make_cake)
print make_cake()
print gift_func



