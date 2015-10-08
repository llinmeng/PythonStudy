# -*- coding: utf-8 -*-
print "=================================="
# 5-1
age = 20
if age >= 18:
    print 'your age is', age              # Python代码的缩进规则
    print 'adult'
                                          # 退出缩进需要多敲一行回车
print 'END'

score = 75
if score >= 60:
    print 'passed'

print "=================================="
# 5-2
if age >= 18:
    print 'adult'
else:
    print 'teenager'


score = 55
if score >= 60:
    print 'passed'
else:
    print 'failed'

if age >= 18:
    print 'adult'
else:
    if age >= 6:
        print 'teenager'
    else:
        print 'kid'


age = 5
if age >= 18:
    print 'adult'
else:
    if age >= 6:
        print 'teenager'
    else:
        if age >= 3:
            print 'kid'
        else:
            print 'baby'


if age >= 18:
    print 'adult'
elif age >= 6:
    print 'teenager'
elif age >= 3:
    print 'kid'
else:
    print 'baby'


age = 8
if age >= 6:
    print 'teenager'
elif age >= 18:
    print 'adult'
else:
    print 'kid'


age = 20
if age >= 6 and age < 18:
    print 'teenager'
elif age >= 18:
    print 'adult'
else:
    print 'kid'


score = 53
if score >= 90:
      print 'excellent'
elif score >= 80:
      print 'good'
elif score >= 60:
      print 'passed'
else:
      print 'failed'


print "=================================="
# 5-3
l = ['Adam', 'Lisa', 'Bart']
for name in l:
    print name

l = [75, 92, 59, 68]
sum = 0.0
for x in l:
      sum = sum + x
print sum / 4

print "=================================="
# 5-4
N = 10
x = 0
while x < N:
    print x
    x = x + 1


N = 100
x = 1
sum = 0
while x < N:
    x = x + 2
    sum = sum + x

print sum

print "=================================="
# 5-5
sum = 0
x = 1
while True:
      sum = sum + x
      x = x + 1
      if x > 100:
            break
print sum


sum = 0
y = x = 1
while True:
      sum = sum + y
      y = y * 2
      if x == 2:
        break
      x = x + 1
print sum

print "=================================="
# 5-6
L = [75, 98, 59, 81, 66, 43, 69, 85]
sum = 0.0
n = 0
for x in L:
      if x < 60:
            continue
      sum = sum + x
      n = n + 1
print sum / n


sum = 0
x = 0
while True:
    x = x + 1
    if x > 100:
        break
    if x % 2 == 0:
        continue
    sum = sum + x
print sum

print "=================================="
# 5-7
for x in ['A', 'B', 'C']:
    for y in ['1', '2', '3']:
        print x + y

print
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
    for y in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
        if x < y:
            print x * 10 + y