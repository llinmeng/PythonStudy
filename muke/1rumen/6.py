# -*- coding: utf-8 -*-
print "=================================="
# 6-1
# 花括号 {} 表示这是一个dict，然后按照 key: value, 写出来即可。最后一个 key: value 的逗号可以省略。
d = {
    'Adam': 95,
    'Lisa': 85,
    'Bart': 59,
    'Paul': 75
}
print d

print "=================================="
# 6-2
# list 必须使用索引返回对应的元素，而dict使用key
d = {
    'Adam': 95,
    'Lisa': 85,
    'Bart': 59,
    'Paul': 75
}
print 'Adam:', d['Adam']
print 'Lisa:', d['Lisa']
print 'Bart:', d['Bart']

print "=================================="
# 6-3
# dict的第一个特点是查找速度快，无论dict有10个元素还是10万个元素，查找速度都一样.
# dict的缺点是占用内存大，还会浪费很多内容.
# 由于dict是按 key 查找，所以，在一个dict中，key不能重复
# dict的第二个特点就是存储的key-value序对是没有顺序的
# 打印的顺序不一定是我们创建时的顺序
# dict的第三个特点是作为 key 的元素必须不可变
# 不可变这个限制仅作用于key，value是否可变无所谓
d = {
    'Adam': 95,
    'Lisa': 85,
    'Bart': 59,
    'Paul': 75
}
print d

d = {
    '123': [1, 2, 3],  # key 是 str，value是list
    123: '123',  # key 是 int，value 是 str
    ('a', 'b'): True  # key 是 tuple，并且tuple的每个元素都是不可变对象，value是 boolean
}
print d

dict3 = {
    95: 'Adam',
    85: 'Lisa',
    59: 'Bart'
}
print dict3[59]

print "=================================="
# 6-4
# dict是可变的
dict4 = {
    'Adam': 95,
    'Lisa': 85,
    'Bart': 59
}
d['Paul'] = 72
print dict4
dict4['Bart'] = 60                       # 如果 key 已经存在，则赋值会用新的 value 替换掉原来的 value
print dict4

d = {
    95: 'Adam',
    85: 'Lisa',
    59: 'Bart'
}
d[72] = 'Pual'
print d

print "=================================="
# 6-5
d = {
    'Adam': 95,
    'Lisa': 85,
    'Bart': 59
}
for key in d:
    print key

print
for key in d:
    print key + ":", d[key]


print "=================================="
# 6-6
# set 持有一系列元素，这一点和 list 很像，但是set的元素没有重复，而且是无序的，这点和 dict 的 key很像
# 打印的顺序不一定是我们创建时的顺序
s = set(['A', 'B', 'C'])
print s

# set内部存储的元素是无序的, set不能包含重复的元素
s = set(['a', 'b', 'c', 'a', 'a'])
print s
print len(s)

s = set(['Adam', 'Lisa', 'Bart', 'Paul'])
print s

print "=================================="
# 6-7
print 'Bart' in s
print 'bart' in s                        # 区分大小写
print 'Bill' in s

s = set(['Adam', 'adam', 'Lisa', 'lisa', 'Bart', 'bart', 'Paul', 'paul'])
print 'adam' in s
print 'bart' in s

print "=================================="
# 6-8
# set存储的元素和dict的key类似，必须是不变对象，因此，任何可变对象是不能放入set中的。
x = 'MON'
if x != 'MON' and x != 'TUE' and x != 'WED' and x != 'THU' and x != 'FRI' and x != 'SAT' and x != 'SUN':
    print 'input error'
else:
    print 'input ok'

weekdays = set(['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN'])
x = 'FDS'
if x in weekdays:
    print 'input ok'
else:
    print 'input error'

months = set(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
x1 = 'Feb'
x2 = 'Sun'
if x1 in months:
    print 'x1: ok'
else:
    print 'x1: error'

if x2 in months:
    print 'x2: ok'
else:
    print 'x2: error'


print "=================================="
# 6-9
s = set(['Adam', 'Lisa', 'Bart'])
for name in s:
    print name


s = set([('Adam', 95), ('Lisa', 85), ('Bart', 59)])
for x in s:
    print x[0] + ':', x[1]

print "=================================="
# 6-10
# 由于set存储的是一组不重复的无序元素，因此，更新set主要做两件事：
# 一是把新的元素添加到set中，二是把已有元素从set中删除。
s = set([1, 2, 3])
print s
s.add(4)
print s
s.add(3)
print s
s.remove(3)
print s
# s.remove(3)                          # 无此元素时,删除报错
# 用add()可以直接添加，而remove()前需要判断
print s

s = set(['Adam', 'Paul'])
l = ['Adam', 'Lisa', 'Bart', 'Paul']
for name in l:
    if name in s:
        s.remove(name)
    else:
        s.add(name)
print s

