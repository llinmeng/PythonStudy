# -*- coding: utf-8 -*-
print "=================================="
# 7-1
# Python不但能非常灵活地定义函数，而且本身内置了很多有用的函数，可以直接调用。

print "=================================="
# 7-2
# 调用函数的时候，如果传入的参数数量不对，会报TypeError的错误
# 如果传入的参数数量是对的，但参数类型不能被函数所接受，也会报TypeError的错误
print abs(-100)
# 比较函数 cmp(x, y) 就需要两个参数，如果 x<y，返回 -1，如果 x==y，返回 0，如果 x>y，返回 1
print cmp(1, 2)
print cmp(2, 2)
print cmp(2, 1)
print int(12.34)
print str(123)

l = []
x = 1
while x <= 100:
    l.append(x * x)
    x = x + 1
print sum(l)

l = []
x = 1
while True:
    l.append(x * x)
    x = x + 1
    if x > 100:
        break
print sum(l)

print "=================================="
# 7-3
# 定义一个函数要使用 def 语句，依次写出函数名、括号、括号中的参数和冒号:，
# 然后，在缩进块中编写函数体，函数的返回值用 return 语句返回
# 如果没有return语句，函数执行完毕后也会返回结果，只是结果为 None。
# return None可以简写为return
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x
print my_abs(-3)

def square_of_sum(l):
    sum = 0
    for x in l:
        sum = sum + x * x
    return sum
print square_of_sum([1, 2, 3, 4, 5])
print square_of_sum([-5, 0, 5, 15, 25])

print "=================================="
# 7-4
# math包提供了sin()和 cos()函数，我们先用import引用它
import math


def move(xx, y, step, angle):
    nx = xx + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny
x, y = move(100, 100, 60, math.pi / 6)
print x, y
r = move(100, 100, 60, math.pi / 6)           # Python的函数返回多值其实就是返回一个tuple
print r


import math


def quadratic_equation(a, b, c):
    t = math.sqrt(b * b - 4 * a * c)
    return (-b + t) / (2 * a), (-b - t) / (2 * a)
print quadratic_equation(2, 3, 0)
print quadratic_equation(1, -6, 5)

print "=================================="
# 7-5
# 如果一个函数在内部调用自身本身，这个函数就是递归函数。
def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)
print fact(3)
# 使用递归函数需要注意防止栈溢出

def move(n, a, b, c):
    if n == 1:
        print a, '-->', c
        return
    move(n-1, a, c, b)
    print a, '-->', c
    move(n-1, b, a, c)
move(4, 'A', 'B', 'C')

print "=================================="
# 7-6
# 定义函数的时候，还可以有默认参数
print int('123', 8)

def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
print power(5)

# 由于函数的参数按从左到右的顺序匹配，所以默认参数只能定义在必需参数的后面：
# OK:
def fn1(a, b=1, c=2):
    pass
# Error:
# def fn2(a=1, b):
    pass


def greet(name = 'world'):
    print 'Hello, ' + name + '.'
print greet()
print greet('Bart')

print "=================================="
# 7-7
# 可变参数的名字前面有个 * 号，我们可以传入0个、1个或多个参数给可变参数
def fn(*args):
    print args
print fn()
print fn('a', )
print fn('a', 'b', 'c')


def average(*args):
    sum = 0.0
    if len(args) == 0:
        return sum
    for x in args:
        sum = sum + x
    return sum / len(args)
print average()
print average(1, 2)
print average(1, 2, 2, 3, 4)