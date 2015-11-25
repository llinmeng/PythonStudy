# -*- coding: utf-8 -*-
# 集合
print "     -*-Set-*-"
# 集合直接创建即可
print set(range(10))

# 集合的副本被忽略
print set([0, 1, 2, 3, 0, 1, 2, 3, 4, 5])

# 集合的顺序随意
print set(['fee', 'fie', 'foe'])

# 并集
a = set([1, 2, 3])
b = set([2, 3, 4])
print a.union(b)
print a|b

# 其他运算
print 1
c = a & b
print c.issubset(a)
print 2
print c <= a
print 3
print c.issuperset(a)
print 4
print c >= a
print 5
print a.intersection(b)
print 6
print a & b
print 7
print a.difference(b)
print 8
print a - b
print 9
print a.symmetric_difference(b)
print 10
print a ^ b
print 11
print a.copy()
print 12
print a.copy() is a

print "================================="
# set类型的union方法
mySets = []
for i in range(10):
    mySets.append(set(range(i, i + 5)))

print reduce(set.union, mySets)


# frozenset()=不可变/可散列的集合
a = set()
b = set()
# a.add(b)
a.add(frozenset(b))


# 堆(只有包含堆操作函数的模块-heapq)
print "     -*-heap-*-"

from heapq import *
from random import shuffle
data = range(10)
shuffle(data)
heap = []
for n in data:
    heappush(heap, n)               # heappush(heap, x) 将x入堆

print heap
heappush(heap, 0.5)
print heap

print heappop(heap)                 # heappop(heap) 将堆中最小的元素弹出
print heappop(heap)
print heappop(heap)
print heap


heap = [5, 8, 0, 3, 6, 7, 9, 1, 4, 2]
heapify(heap)                       # heapify(heap) 将heap属性强制应用到任意一个列表
print heap


print
print heapreplace(heap, 0.5)        # heapreplace(heap, x) 弹出堆的最小元素. 并将新元素x推入
print heap
print heapreplace(heap, 10)
print heap


# 双端队列
print "     -*-double-ended queue-*_"
from collections import deque
q = deque(range(5))
q.append(5)
q.appendleft(5)
print q
print q.pop()                       # 队列右端
print q.popleft()
print q
q.rotate()                    # 旋转元素
print q


# time
print "     -*-time-*-"
from time import *
print asctime()


# 随机函数
print "     -*-random-*-"
from random import *
from time import *
date1 = (2008, 1, 1, 0, 0, 0, -1, -1, -1)
time1 = mktime(date1)
date2 = (2009, 1, 1, 0, 0, 0, -1, -1, -1)
time2 = mktime(date2)
random_time = uniform(time1, time2)
print asctime(localtime(random_time))


from random import randrange
num = input('How many dice? ')
sides = input('How many sides per die? ')
sum = 0
for i in range(num):
    sum += randrange(sides) + 1
print 'The result is', sum


values = range(1, 11) + 'Jack Queen King'.split()
suits = 'diamonds clubs hearts spades'.split()
deck = ['%s of %s' % (v, s) for v in values for s in suits]
from pprint import pprint
pprint(deck[:12])

print
from random import shuffle
shuffle(deck)
pprint(deck[:12])
# 每按一次回车, 发一次牌
while deck:
    raw_input(deck.pop())