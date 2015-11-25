# -*- coding: utf-8 -*-
import json
print "=================================="
# 5-1
print "=================================="
# 5-2
class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
class Student(Person):
    def __init__(self, name, gender, score):
        super(Student, self).__init__(name, gender)
        self.score = score
s1 = Student('A', 'M', 99)
print s1.gender
print s1.name
print s1.score


class Teacher(Person):
    def __init__(self, name, gender, course):
        super(Teacher, self).__init__(name, gender)
        self.course = course
t1 = Teacher('B', 'N', 2)
print t1.gender
print t1.name
print t1.course

print "=================================="
# 5-3


class Student(Person):
    def __init__(self, name, gender, score):
        super(Student, self).__init__(name, gender)
        self.score = score
class Teacher(Person):
    def __init__(self, name, gender, course):
        super(Teacher, self).__init__(name, gender)
        self.course = course
p = Person('Tim', 'Male')
s = Student('Bob', 'Male', 88)
t = Teacher('Alice', 'Female', 'English')
print isinstance(s, Person)
print isinstance(p, Student)
print isinstance(p, Teacher)
print isinstance(s, Student)

print '&'
print isinstance(t, Person)
print isinstance(t, Student)
print isinstance(t, Teacher)
print isinstance(t, object)


print "=================================="
# 5-4


class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
    def whoAmI(self):
        return 'I am a Person, my is %s' % self.name
class Student(Person):
    def __init__(self, name, gender, score):
        super(Student, self).__init__(name, gender)
        self.score = score
    def whoAmI(self):
            return 'I am a Student, my name, is %s' % self.name
class Teacher(Person):
    def __init__(self, name, gender, course):
        super(Teacher, self).__init__(name, gender)
        self.course = course
    def whoAmI(self):
        return 'I am a Teacher, my name is %s' % self.name
class Book(object):
    def whoAmI(self):
        return 'I am a book'
def who_am_i(x):
    print x.whoAmI()
p = Person('Tim', 'Male')
s = Student('Bob', 'Male', 88)
t = Teacher('Alice', 'Female', 'English')
b = Book()
who_am_i(p)
who_am_i(s)
who_am_i(t)
who_am_i(b)


class Students(object):
    def read(self):
        return r'["Tim", "Bob", "Alice"]'

s = Students()

print json.load(s)                      # u'Tim' 表示Tim是Unicode字符串，2.7里面是这样显示的，3.X就省掉u


print "=================================="
# 5-5
class A(object):
    def __init__(self, a):
        print 'init A...'
        self.a = a


class B(A):
    def __init__(self, a):
        super(B, self).__init__(a)
        print 'init B...'


class C(A):
    def __init__(self, a):
        super(C, self).__init__(a)
        print 'init C...'


class D(B, C):
    def __init__(self, a):
        super(D, self).__init__(a)
        print 'init D...'

d = D('d')


class Person(object):
    pass
class Student(Person):
    pass
class Teacher(Person):
    pass
class SkillMixin(object):
    pass
class BasketballMixin(SkillMixin):
    def ball(self):
        return 'Basketball...'
class FootballMixin(SkillMixin):
    def ball(self):
        return 'Football...'
class BStudent(Student, BasketballMixin):
    pass
class FTeacher(Teacher, FootballMixin):
    pass

s = BStudent()
print s.ball()
t = FTeacher()
print t.ball()


print "=================================="
# 5-6
print "**********************************"
class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
class Student(Person):
    def __init__(self, name, gender, score):
        super(Student, self).__init__(name, gender)
        self.score = score
    def whoAmI(self):
        return 'I am a Student, my name is %s' % self.name

print type(123)
s = Student('Bob', 'Male', 88)
print type(s)

print dir(123)
print'^'
print dir(s)

print '*'
print getattr(s, 'name')

L = tuple(dir(s))
print "L = ", L


def skip_item(data):
    key = "__"
    result = []
    if isinstance(data, tuple):
        data = list(data)
    if isinstance(data, list):
        for item in data:
            if item and item.startswith(key) and item.endswith(key):
                continue
            else:
                result.append(item)
    return result



def skip_item2(data):
    key = "__"
    result = []
    if isinstance(data, tuple):
        data = list(data)
    elif isinstance(data, list):
        for item in data:
            if item and not item.startswith("__") and not item.endswith("__"):
                result.append(item)
    return result


def is_need(item):
    key = "__"
    return item and not item.startswith(key) and not item.endswith(key)


def is_need2(item):
    return len(item) >= 2 and item[0:2].find("__") and item[-2:].find("__")

f = lambda item: item and not item.startswith("__") and not item.endswith("__")

print "skip : ", skip_item(L)
print "result = ", filter(is_need, L)
print "result2 = ", filter(is_need2, L)
print "lambda result = ", filter(f, L)
print "lambda result = ", filter(lambda item: item and not item.startswith("__") and not item.endswith("__"), L)

f2 = lambda item: item and item == item.lstrip("__") and item == item.rstrip("__")
f3 = lambda item: item and item.strip("__") == item

print "f2 result = ", filter(f2, L)
print "f3 result = ", filter(f3, L)
data = filter(f3, L)
print data, type(data), list(data)

print "**********************************"



print getattr(s, 'name')
setattr(s, 'name', 'Adam')
print s.name

# print getattr(s, 'age')
print getattr(s, 'age', 20)

class Person(object):
    def __init__(self, name, gender, **kw):
        self.name = name
        self.gender = gender
        for k, v in kw.iteritems():
            setattr(self, k, v)
p = Person('Bob', 'Male', age = 18, course = 'Python')
print p.age
print p.course