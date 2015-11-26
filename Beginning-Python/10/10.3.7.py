# -*- coding: utf-8 -*-
# 10.3.7
# shelve.open函数返回的对象不是普通的映射
import shelve
s = shelve.open('test.dat')
s['x'] = ['a', 'b', 'c']
s['x'].append('d')
print s['x']
# ['a', 'b', 'c']

import shelve
s = shelve.open('test.dat')
s['x'] = ['a', 'b', 'c']
temp = s['x']
temp.append('d')
s['x'] = temp
print s['x']
# ['a', 'b', 'c', 'd']



