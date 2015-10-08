# -*- coding: utf-8 -*-
print "=================================="
# 4-1
l = ['Adam', 95.5, 'Lisa', 85, 'Bart', 59]
print l

print "=================================="
# 4-2
l = [95, 5, 85, 59]
# print l
print l[0]
print l[1]
print l[2]
print l[3]

l = ['Adam', 'Lisa', 'Bart']
print l[0]
print l[1]
print l[2]
l = [95.5, 85, 59]
print l[0]
print l[1]
print l[2]
# print l[3]

print "=================================="
# 4-3
l = [95.5, 85, 59]
print l[-1]
print l[-2]
print l[-3]
# print l[-4]                              # 不要越界

print "=================================="
# 4-4
l = ['Adam', 'Lisa', 'Bart']
l.append('Paul')
print l
l = ['Adam', 'Lisa', 'Bart']
l.insert(0, 'Paul')
print l
l = ['Adam', 'Lisa', 'Bart']
l.insert(2, 'Paul')
print l

print "=================================="
# 4-5
print l
l = ['Adam', 'Lisa', 'Bart', 'Paul']
print l.pop()
print l
l = ['Adam', 'Lisa', 'Bart', 'Paul']
print l.pop(2)
print l
l = ['Adam', 'Lisa', 'Paul', 'Bart']
print l.pop(3)
print l.pop(2)
print l

print "=================================="
# 4-6
l = ['Adam', 'Lisa', 'Bart']
print l
l[2] = 'Paul'
print l
l[-1] = 'Paull'
print l
l = ['Adam', 'Lisa', 'Bart']
l[0] = 'Bart'
l[-1] = 'Adam'
print l

print "=================================="
# 4-7
t = ('Adam', 'Lisa', 'Bart')
print t
# t[0] = 'Paul'
t = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
print t

print "=================================="
# 4-8
t = ()
print t
t = (1)
print t
t = (1,)
print t
t = (1, 2, 3,)
print t
t = ('Adam')
print t

print "=================================="
# 4-9
t = ('a', 'b', ['A', 'B'])
print t
l = t[2]
print l
l[0] = 'X'
l[1] = 'Y'
print l
t = ('a', 'b', ('A', 'B'))
print t
