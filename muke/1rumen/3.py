# -*- coding: utf-8 -*-
print "=================================="
# 3-1
print 45678 + 0x12fd2

print 'Learn Python in imooc'

print 100 < 99
print 0xff == 255

print "=================================="
# 3-2
print 'hello, python'
print "hello, python"
print """hello, python"""
print 'hello,', 'python'
print 'hello', ',', 'python'

print "=================================="
# 3-3
# print 'hello, python'
# print "hello, python"
print """hello, python"""
print 'hello,', 'python'
print 'hello', ',', 'python'

print "=================================="
# 3-4
a = 'ABC'
b = a
a = 'XYZ'
print b, a

x = 1
d = 2
n = 1                  # 测试100, 10, 1
x1 = x + (n - 1) * d
s = (x + x1) * n / 2
print s

print "=================================="
# 3-5
str = 'Pyhton was started in 1998 by \"Guido\". \nPython is free and easy to learn.'
print str

print "=================================="
# 3-6
print '''Python is created by "Guido".
It is free and easy to learn.
Let's start learn Python in imooc!'''
print r'''Python is created by "Guido".
It is free and easy to learn.
Let's start learn Python in imooc!'''
print r'''"To be, or not to be": that is the question.
Whether it's nobler in the mind to suffer.'''
print '''"To be, or not to be": that is the question.
Whether it's nobler in the mind to suffer.'''
print r'\"To be, or not to be\": that is the question.\nWhether it\'s nobler in the mind to suffer.'
print '\"To be, or not to be\": that is the question.\nWhether it\'s nobler in the mind to suffer.'

print "=================================="
# 3-8
print 2.5 + 10.0 / 4

print "=================================="
# 3-9
a = True
print a and 'a = T' or 'a = F'   # 因为Python把0、空字符串''和None看成 False，其他数值和非空字符串都看成 True，
print a
# and 和 or 运算的一条重要法则：短路计算。
# 1. 在计算 a and b 时，如果 a 是 False，则根据与运算法则，整个结果必定为 False，
# 因此返回 a；如果 a 是 True，则整个计算结果必定取决与 b，因此返回 b。
# 2. 在计算 a or b 时，如果 a 是 True，则根据或运算法则，整个计算结果必定为 True，因此返回 a；
# 如果 a 是 False，则整个计算结果必定取决于 b，因此返回 b。

print "=================================="
# 3-10
a = 'python'
print 'hello,', a or 'world'
b = ''
print 'hello,', b or 'world'
