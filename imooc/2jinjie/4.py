# -*- coding: utf-8 -*-
import types
print "=================================="
# 4-1
print "=================================="
# 4-2
class Person(object):
    pass
xiaoming = Person()
xiaohong = Person()
print xiaoming
print xiaohong
print xiaoming == xiaohong

print "=================================="
# 4-3
xiaoming.name = 'XiaoMing'
xiaoming.gender = 'Male'
xiaoming.birth = '1990-1-1'

xiaohong.name = 'XiaoHong'
xiaohong.school = 'No.1 High School'
xiaohong.grade = 2

xiaohong.grade = xiaohong.grade + 1
print xiaohong.grade


class Person(object):
    pass

p1 = Person()
p1.name = 'Bart'

p2 = Person()
p2.name = 'Adam'

p3 = Person()
p3.name = 'Lisa'

L1 = [p1, p2, p3]
L2 = sorted(L1, lambda s1, s2: cmp(s1.name, s2.name))
print L2[0].name
print L2[1].name
print L2[2].name


print "=================================="
# 4-4


class Person(object):
    def __init__(self, name, gender, birth):    # self 不可丢
        self.name = name
        self.gender = gender
        self.birth = birth


xiaoming = Person('Xiao Ming', 'Male', '1991-1-1')
xiaohong = Person('xiao Hong', 'Female', '1992-2-2')
print xiaoming.name
print xiaohong.birth


class Person(object):
    def __init__(self, name, gender, birth, **kw):
        self.name = name
        self.gender = gender
        self.birth = birth
        for k, v in kw.iteritems():
            setattr(self, k, v)


xiaoming = Person('xiaoming', 'male', '1993-3-3', job = 'student')
print xiaoming.name
print xiaoming.job
print xiaoming.birth


print "=================================="
# 4-5
class Person(object):
    def __init__(self, name):
        self.name = name
        self._title = 'Mr'
        self.__job = 'Student'


p = Person('Bob')
print p.name
print p._title
# print p.__job


class Person(object):
    def __init__(self, name, score):
        self.name = name
        self.__score = score


p = Person('Bob', 59)
print p.name
#  print p.__score

print "=================================="
# 4-6
class Person(object):
    address = 'Earth'
    def __init__(self, name):
        self.name = name
print Person.address
print
p1 = Person('Bob')
p2 = Person('Alice')
print p1.address
print p1.name
print p2.address
print p2.name
print '*'

class Person(object):
    count = 0
    def __init__(self, name):
        Person.count += 1     # 用类名控制
        self.name = name
p1 = Person('Bob')
print Person.count
p2 = Person('Alice')
print Person.count
p3 = Person('Tim')
print Person.count

print "=================================="
# 3-7
class Person(object):
    address = 'Earth'
    def __init__(self, name):
        self.name = name


p1 = Person('Bob')
p2 = Person('Alice')
print 'Person.address = ' + Person.address

p1.address = 'China'
print 'p1.address = '+ p1.address

print 'Person.address = ' + Person.address
print 'p2.address = ' + p2.address

del p1.address
print p1.address
print '*'

class Person(object):
#    __count = 0
    def __init__(self, name):
#       Person.count += 1     # 用类名控制
        self.name = name
#       print Person.__count
p1 = Person('Bob')
# print Person.__count
p2 = Person('Alice')
# print Person.count
p3 = Person('Tim')
# print Person.count


print "=================================="
# 4-8


class Person2(object):
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

p1 = Person2('Bob')
print p1.get_name()                 # self 不需要显示传入


class Person(object):
    def __init__(self, name, score):
        self.name = name
        self.__score = score
    def get_grade(self):
        if self.__score >= 90 and self.__score <= 100:
            return 'A'
        elif self.__score >= 60 and self.__score < 90:
            return 'B'
        else:
            return 'C'


p1 = Person('Bob', 90)
p2 = Person('Alice', 65)
p3 = Person('Tim', 48)
print p1.get_grade()
print p2.get_grade()
print p3.get_grade()


print "=================================="
# 4-9
class Person(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def get_grade(self):
        return 'A'

p1 = Person('Bob', 0)
# print p1.get_grade
print p1.get_grade()


def fn_get_grade(self):
    if self.score >= 80:
        return 'A'
    if self.score >= 60:
        return 'B'
    return 'C'
class Person(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

p1 = Person('Bob', 90)
p1.get_grade = types.MethodType(fn_get_grade, p1, Person)
print p1.get_grade()
p2 = Person('Alice', 65)

print '*'
class Person(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
        self.get_grade = lambda: 'A'

p1 = Person('Bob', 90)
print p1.get_grade
print p1.get_grade()


print "=================================="
# 4-10
class Person(object):
    count = 0
    @classmethod
    def how_many(cls):
        return cls.count
    def __init__(self, name):
        self.name = name
        Person.count = Person.count + 1

print Person.how_many()
p1 = Person('Bob')
print Person.how_many()


class Person(object):
    __count = 0
    @classmethod
    def how_many(cls):
        return cls.__count
    def __init__(self, name):
        self.name = name
        Person.__count = Person.__count + 1

print Person.how_many()
p1 = Person('Bob')
print Person.how_many()