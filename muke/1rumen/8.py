# -*- coding:utf-8 -*-
print "=================================="
# 8-1
l = ['Adam', 'Lisa', 'Bart']
print l[0: 3]                            # l[0:3]表示，从索引0开始取，直到索引3为止，但不包括索引3
print l[: 3]                             # 如果第一个索引是0，还可以省略
print l[1: 3]                            # 也可以从索引1开始，取出2个元素出来
print l[:]                               # 只用一个 : ，表示从头到尾,l[:]实际上复制出了一个新list
print l[::2]                             # 第三个参数表示每N个取一个，上面的 l[::2]
print                                    # 会每两个元素取出一个来，也就是隔一个取一个

l = range(1, 101)
print l[: 10]
print l[2:: 3]
print l[4: 50: 5]

print "=================================="
# 8-2
# 记住倒数第一个元素的索引是-1。倒序切片包含起始索引，不包含结束索引
L = range(1, 101)
print L[-10:]

print L[-46::5]
print L[4::5][-10:]                       # [4::5]是正序取5的倍数，[-10:]逆序取后10个

print L[-4:-1:2]

print "=================================="
# 8-3
print 'ABCDEFG'[:3]
print 'ABCDEFG'[-3:]
print 'ABCDEFG'[::2]

print 'abc'.upper()


def firstCharUpper(s):
    return s[0].upper() + s[1:]
print firstCharUpper('hello')
print firstCharUpper('sunday')
print firstCharUpper('september')