# -*- coding: utf-8 -*-
import math
#函数式编程
print "=================================="
# 2-3
import math
print abs(-10)

# 高阶函数


def add(x, y, f):
    return f(x) + f(y)
print add(-5, 9, abs)
print abs(-5) + abs(9)
f = math.sqrt
print add(25, 9, f)
print add(36, 9, math.sqrt)


print "=================================="
# 2-4
# map()是 Python 内置的高阶函数，它接收一个函数 f 和一个 list，
# 并通过把函数 f 依次作用在 list 的每个元素上，得到一个新的 list 并返回.


def f(x):
    return x * x
print map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
# 注意：map()函数不改变原有的 list，而是返回一个新的 list


def format_name(s):
    return s[0].upper() + s[1:].lower()
print map(format_name, ['adam', 'LISA', 'barT'])


print "=================================="
# 2-5
# reduce()函数也是Python内置的一个高阶函数.reduce()函数接收的参数和 map()类似，
# 一个函数 f，一个list，但行为和 map()不同，reduce()传入的函数 f 必须接收两个参数，
# reduce()对list的每个元素反复调用函数f，并返回最终结果值.
# reduce()还可以接收第3个可选参数，作为计算的初始值.

def f(x, y):
    return x + y
print reduce(f, [1, 3, 5, 7, 9])
print reduce(f, [1, 3, 5, 7, 9], 100)          # 100为初始值


def f(x, y):
    return x * y
print reduce(f, [2, 4, 5, 7, 12])


print "=================================="
# 2-6
# filter()函数是 Python 内置的另一个有用的高阶函数，
# filter()函数接收一个函数 f 和一个list，这个函数 f 的作用是对每个元素进行判断，
# 返回 True或 False，filter()根据判断结果自动过滤掉不符合条件的元素，
# 返回由符合条件元素组成的新list


def is_odd(x):
    return x % 2 == 1
print filter(is_odd, [1, 4, 6, 7, 9, 12, 17])


def is_not_empty(s):
    return s and len(s.strip()) > 0      # s.strip(rm) 删除 s 字符串中开头、结尾处的 rm 序列的字符。
print filter(is_not_empty, ['test', None, "asf", '', 'str', '  ', "  ", 'END'])


a = '     123'
print a.strip()
print len(a.strip())
a = '\t\t123\r\n'
print a
print a.strip()
print len(a.strip())


def is_sqrt(x):
    return math.sqrt(x) == int(math.sqrt(x))
print filter(is_sqrt, range(1, 101))


def is_sqr(x):
    r = int(math.sqrt(x))
    return r * r == x
print filter(is_sqr, range(1, 101))

print "=================================="
# 2-7
# Python内置的 sorted()函数可对list进行排序
# 但 sorted()也是一个高阶函数，它可以接收一个比较函数来实现自定义排序，
# 比较函数的定义是，传入两个待比较的元素 x, y，如果 x 应该排在 y 的前面，
# 返回 -1，如果 x 应该排在 y 的后面，返回 1。如果 x 和 y 相等，返回 0.
def reversed_cmd(x, y):
    if x > y:
        return -1
    if x < y:
        return 1
    return 0
print sorted([36, 5, 12, 9, 21], reversed_cmd)


def reversed_cmd(x, y):
    if x > y:
        return 1
    if x < y:
        return -1
    return 0
print sorted([36, 5, 12, 9, 21], reversed_cmd)
print sorted(['bob', 'about', 'Zoo', 'Credit'], reversed_cmd)
# 大写字母的ASCII比小写字母的小


def cmp_ignore_case(s1, s2):
    if s1.upper() < s2.upper():
        return -1
    if s1.upper() > s2.upper():
        return 1
    return 0
print sorted(['bob', 'about', 'Zoo', 'Credit'], cmp_ignore_case)


def cmp_ignore_case(s1, s2):
    if s1.upper() < s2.upper():
        return -1
    elif s1.upper() > s2.upper():
        return 1
    else:
        return 0
print sorted(['bob', 'about', 'Zoo', 'Credit'], cmp_ignore_case)


print "=================================="
# 2-8


def f():
    print 'call f()...'
    def g():
        print 'call g()...'
    return g                         # 每次调用f()打印都会打印g函数的初始地址
x = f()
print x
print x()

print
def myabs():
    return abs                        # 返回函数
def myabs2(x):
    return abs(x)                     # 返回函数调用的结果，返回值是一个数值
print myabs()
print myabs2(-2)


def calc_sum(lst):
    return sum(lst)
print calc_sum([1, 2, 3])


def calc_sum(lst):
    def lazy_sum():
        return sum(lst)
    return lazy_sum
f = calc_sum([1, 3, 5])
print f             # 调用calc_sum（）并没有计算出结果，而是返回函数
print f()           # 对返回的函数进行调用时， 才计算结果
print
print calc_sum([1, 3, 5])()

def calc_prod(lst):
    def lazy_prod():
        def f(x, y):
            return x * y
        return reduce(f, lst, 1)
    return lazy_prod
f = calc_prod([1, 2, 3, 4, 5])
print f()


print "=================================="
# 2-9


def g():
    print 'g()......'


def f():
    print 'f()......'
    return g
print f()

print
def f():
    print 'f()......'
    def g():
        print 'g().....'
    return g()
print f()
print f                                # 打印函数f的首地址
print


# 内层函数引用了外层函数的变量（参数也算变量），
# 然后返回内层函数的情况，称为闭包（Closure）.
def calc_sum(lst):
    def lazy_sum():
        return sum(lst)
    return lazy_sum()
print calc_sum([1, 2, 3, 4])


# 闭包的特点是返回的函数还引用了外层函数的局部变量，所以，
# 要正确使用闭包，就要确保引用的局部变量在函数返回后不能变.
print '*'
def count():
    fs = []
    for i in range(1, 4):
        def f9():
            print i * i
            return i * i
        fs.append(f9)
    return fs
a1, a2, a3 = count()
print a1()
print a2()
print a3()

# 当count()函数返回了3个函数时，这3个函数所引用的变量 i 的值已经变成了3.
# 由于f1、f2、f3并没有被调用，所以，此时他们并未计算 i*i，
# 当 f1 被调用时才计算i * i, 但此时的i值已经变为3了.
# 因此，返回函数不要引用任何循环变量，或者后续会发生变化的变量.

print '*'
def count():
    fs = []
    for i in range(1, 4):
        def f(j):
            def g():                   #### 闭包
                print j * j
                return j * j
            return g                   ####
        r = f(i)
        fs.append(r)
    return fs
f1, f2, f3 = count()
f1(), f2(), f3()


print '*'
def count():
    fs = []
    for i in range(1, 4):
        def f(j):
            print j * j
            print '+'
            return j * j
        r = f(i)
        fs.append(r)
    return fs
f1, f2, f3 = count()
print f1, f2, f3

print "=================================="
# 2-10
print map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])
# lambda x: x * x   为匿名函数, lambda表示关键字,:前的x表示函数参数.
# 匿名函数只能有一个表达式,不写return.使用时,不必定义函数名而是直接创建函数对象.
# def f(x):
#   return x * x
print sorted([1, 3, 9, 5, 0], lambda x, y: -cmp(x, y))    # -为取负
myabs = lambda x: -x if x < 0 else x
print myabs(-1)
print myabs(1)


def is_not_empty(s):
    return s and len(s.strip()) > 0
print filter(is_not_empty, ['test', 'None', '', 'str', '   ', 'END'])

print filter(lambda s: s and len(s.strip()) > 0, ['test', 'None', '', 'str', '   ', 'END'])


print "=================================="
# 2-11
# python的decorator本质是高阶函数(可以使用函数作为参数, 然后返回一个新函数)
# @
print "=================================="
# 2-12
# 装饰器函数就是对原函数进行改造，重新使用，但原函数定义不变，仍可以直接调用
print '++++++++++++++++++'
def log(f):
    def fn(x):
        print 'call ' + f.__name__ + '()...'
        return f(x)
    return fn

@log
def factorial(n):
    return reduce(lambda x, y: x * y, range(1, n + 1))
print factorial(10)
print '++++++++++++++++++'

# 函数的参数不止一个,将报错,log写死了只含有一个参数的返回函数
# @log
def add(x, y):
    return x + y
print add(1, 3)


print '++++++++++++++++++'
# *args, **kw, 保证任一个数的参数都能正常调用
def log(f):
    def fn(*args, **kw):
        print 'call ' + f.__name__ + '()...'
        return f(*args, **kw)
    return fn
@log
def add(x, y):
    return x + y
print add(1, 3)
print '++++++++++++++++++'


import time


def performance(f):
    def fn(*args, **kw):
        t1 = time.time()
        t2 = time.time()
        print 'call %s() in %0.8f s' %(f.__name__, (t2 - t1))
        return f(*args, **kw)
    return fn
@performance
def factorial(n):
    return reduce(lambda x, y: x * y, range(1, n + 1))
print factorial(10)

print "=================================="
# 2-13
print '++++++++++++++++++'


# 闭包, 不可拆解.最内层的wrapper调用了最外层的参数perfix.
def log(prefix):
    def log_decorator(f):
        def wrapper(*args, **wp):
            print '[%s] %s()...' % (prefix, f.__name__)
            return f(*args, **wp)
        return wrapper
    return log_decorator
print '++++++++++++++++++'
@log('DEBUG')
# 返回decorator:
def test():
    pass
print test()


import time


def performance(unit):
    def test(f):
        def fn(*args, **kw):
            t1 = time.time()
            t2 = time.time()
            print 'call %s() in %0.8f s' %(f.__name__, (t2 - t1))
            return f(*args, **kw)
        return fn
    return test
@performance('ms')
def factorial(n):
    return reduce(lambda x, y: x * y, range(1, n + 1))
print factorial(10)

print '*'
import time


def performance(unit):
    def test(f):
        def fn(*args, **kw):
            t1 = time.time()
            t2 = time.time()
            t = (t2 - t1) * 1000 if unit == 'ms' else (t2 - t1)
            print 'call %s() in %0.8f %s' %(f.__name__, t, unit)
            return f(*args, **kw)
        return fn
    return test
@performance('ms')
def factorial(n):
    return reduce(lambda x, y: x * y, range(1, n + 1))
print factorial(10)

print "=================================="
# 2-13
# @decorator 可以动态实现函数功能的增加
def f1(x):
    pass
print f1.__name__


# 由于decorator返回的新函数函数名已经不是'f2'，而是@log内部定义的'wrapper'
def log(f):
    def wrapper(*args, **kw):
        print 'call...'
        return f(*args, **kw)
    return wrapper
@log
def f2(x):
    pass
print f2.__name__


def log(f):
    def wrapper(*args, **kw):
        print 'call...'
        return f(*args, **kw)
    wrapper.__name__ = f.__name__
    wrapper.__doc__ = f.__doc__
    return wrapper
# 把原函数的所有必要属性都一个一个复制到新函数上，
# Python内置的functools可以用来自动化完成这个“复制”的任务.
import functools
def log(f):
    @functools.wraps(f)
    def wrapper(*args, **kw):
        print 'call...'
        return f(*args, **kw)
    return wrapper

print '^'
def performance(unit):
    def perf_decorator(f):
        @functools.wraps(f)
        def wrapper(*args, **kw):
            t1 = time.time()
            t2 = time.time()
            t = (t2 - t1) * 1000 if unit == 'ms' else (t2 - t1)
            print 'call %s() in %f %s' % (f.__name__, t, unit)
            return f(*args, **kw)
        return wrapper
    return perf_decorator
@performance('ms')
def factorial(n):
    return reduce(lambda x, y: x * y, range(1, n + 1))

print factorial.__name__
print factorial(10)


print "=================================="
# 2-14
# 偏函数
print int('12345')
print int('12345', base = 8)
print int('12345', base = 16)


def int2(x, base = 2):
    return int(x, base)
print int2('1000000')
import functools
int2 = functools.partial(int, base = 2)
print int2('1000000')
# functools.partial可以把一个参数多的函数变成一个参数少的新函数,
# 少的参数需要在创建时指定默认值,这样降低新函数调用时的难度
f = lambda s1, s2: cmp(s1.upper(), s2.upper())
sorted_ignore_case = functools.partial(sorted, cmp = f)
print sorted_ignore_case(['bob', 'about', 'Zoo', 'Credit'])
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key = str.lower))

