# -*- coding: utf-8 -*-
print "=================================="
# 10-1
print range(1, 11)

L = []
for x in range(1, 11):
    L.append(x * x)


print L

# 写列表生成式时，把要生成的元素 x * x 放到前面，
# 后面跟 for 循环，就可以把list创建出来
print [x * x for x in range(1, 11)]     # 列表生成式

print [x * (x + 1) for x in range(1, 100, 2)]
print
print [x * y for x, y in zip(range(1, 101, 2), range(2, 101, 2))]
for x in range(1, 100, 2):
    print x, '*', (x + 1), '=', x * (x + 1)


print "=================================="
# 10-2
# 使用for循环的迭代不仅可以迭代普通的list，还可以迭代dict。
d = {
    'Adam': 95,
    'Lisa': 85,
    'Bart': 59
}
tds = ['<tr><td>%s</td><td>%s</td></tr>' % (name, score) for name, score in d.iteritems()]
print '<table border="1">'
print '<tr><th>Name</th><th>Score</th><tr>'
print '\n'.join(tds)
print '</table>'
# 字符串可以通过 % 进行格式化，用指定的参数替代 %s。
# 字符串的join()方法可以把一个 list 拼接成一个字符串

print
def penerate(name, score):
    if score < 60:
        return '<tr><td>%s</td><td style = "color:red">%s</td></tr>' % (name, score)
    return'<tr><td>%s</td><td>%s</td></tr>' % (name, score)
tds = [penerate(name, score) for name, score in d.iteritems()]
print '<table border="1">'
print '<tr><th>Name</th><th>Score</th><tr>'
print '\n'.join(tds)
print '</table>'
print

print "=================================="
# 10-3
# 列表生成式的 for 循环后面还可以加上 if 判断
print [x * x for x in range(1, 11) if x % 2 == 0]


def judgeiu(L):
    return [x.upper() for x in L if isinstance(x, str)]
print judgeiu(['UwefaJUHHI', 'HUIGYUtfgyuh', 34567])

print "=================================="
# 10-4
print [m + n for m in 'ABC' for n in '123']

L = []
for m in 'ABC':
    for n in '123':
        L.append(m + n)
print L


print [x for x in range(100, 1000) if x / 100 == x % 10]
print [m * 100 + n * 10 + m for m in range(1, 10) for n in range(0, 10)]

