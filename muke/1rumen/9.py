# -*- coding: utf-8 -*-
print "=================================="
# 9-1
# 如果给定一个list或tuple，我们可以通过for循环来遍历这个list或tuple，
# 这种遍历我们成为迭代（Iteration），迭代是通过 for ... in 来完成的
# 1. 有序集合：list，tuple，str和unicode；
# 2. 无序集合：set
# 3. 无序集合并且具有 key-value 对：dict
for i in range(1, 101):
    if i % 7 == 0:
        print i

print "=================================="
# 9-2
# 迭代永远是取出元素本身，而非元素的索引。
L = ['Adam', 'Lisa', 'Bart', 'Paul']
for index, name in enumerate(L):
    print index, '-', name

print
L = [
    'Adam',
    'Lisa', 'Bart', 'Paul'
]
for index, name in zip(range(1, len(L)+1), L):
    print index, '-', name
print
for index, name in enumerate(L):
    print index + 1, '-', name


print "=================================="
# 9-3
d = {
    'Adam': 95,
    'Lisa': 85,
    'Bart': 59,
    'Paul': 74
}
sum = 0.0
for v in d.itervalues():
    sum = sum + v
print sum / len(d)


print "=================================="
# 9-4
d = {
    'Adam': 95,
    'Lisa': 85,
    'Bart': 59
}
print d.items()
for key, value in d.items():            # iteritems()
    print key, ':', value


d = {
    'Adam': 95,
    'Lisa': 85,
    'Bart': 59,
    'Pual':74
}
sum4 = 0.0
for key, value in d.iteritems():        #items()
    sum4 = sum4 + value
    print key, ':', value
print 'average', ':', sum / len(d)
