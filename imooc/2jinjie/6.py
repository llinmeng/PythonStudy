# -*- coding: utf-8 -*-
print "=================================="
# 6-1
print "=================================="
# 6-2

class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
    def __str__(self):
        return '(Person: %s, %s)' % (self.name, self.gender)
p = Person('Bob', 'male')
print p
print p.name


class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
    def __str__(self):
        return'(Person: %s, %s)' % (self.name, self.gender)
    __repr__ = __str__
p = Person('Bob', 'male')
print p

class Student(Person):
    def __init__(self, name, gender, score):
        super(Student, self).__init__(name, gender)
        self.score = score
    def __str__(self):
        return '<Student: %s, %s, %s>' % (self.name, self.gender, self.score)
    __repr__ = __str__
s = Student('A', "M", 99)
print s

print "=================================="
# 6-3
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def __str__(self):
        return '(%s: %s)' % (self.name, self.score)
    __repr__ = __str__
    def __cmp__(self, s):
        if self.name < s.name:
            return -1
        elif self.name > s.name:
            return 1
        else:
            return 0
L = [Student('Tim', 99), Student('Bob', 88), Student('Alice', 77)]
print sorted(L)
# L = [Student('Tim', 99), Student('Bob', 88), 100, 'Hello']
print sorted(L)


class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def __str__(self):
        return '(%s: %s)' % (self.name, self.score)
    __repr__ = __str__
    def __cmp__(self, s):
        if self.score == s.score:
            return cmp(self.name, s.name)
        return -cmp(self.score, s.score)
L = [Student('tim', 99), Student('bob', 88), Student('alice', 99)]

print sorted(L)


print "=================================="
# 6-4
class Students(object):
    def __init__(self, *args):
        self.names = args
    def __len__(self):
        return len(self.names)
ss = Students('Bob', 'Alice', 'Tim')
print len(ss)


class Fib(object):
    def __init__(self, num):
        L = [0, 1]
        for n in range(num - 2):
            L.append(L[-2] + L[-1])
            self.numbers = L
    def __str__(self):
        return str(self.numbers)
    __repr__ = __str__
    def __len__(self):
        return len(self.numbers)
f = Fib(10)
print f
print len(f)


print "=================================="
# 6-5
class Rational(object):
    def __init__(self, p, q):
        self.p = p
        self.q = q
    def __add__(self, r):
        return Rational(self.p * r.q + self.q * r.p, self.q * r.q)
    def __str__(self):
        return '%s / %s' % (self.p, self.q)
    __repr__ = __str__
r1 = Rational(1, 3)
r2 = Rational(1, 2)
print r1 + r2


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)
class Rational(object):
    def __init__(self, p, q):
        self.p = p
        self.q = q
    def __add__(self, r):
        return Rational(self.p * r.q + self.q * r.p, self.q * r.q)
    def __sub__(self, r):
        return Rational(self.p * r.q - self.q * r.p, self.q * r.q)
    def __mul__(self, r):
        return Rational(self.p * r.p, self.q * r.q)
    def __div__(self, r):
        return Rational(self.p * r.q, self.q * r.p)
    def __str__(self):
        g = gcd(self.p, self.q)
        return '%s/%s' % (self.p / g, self.q / g)
    __repr__ = __str__
r1 = Rational(1, 3)
r2 = Rational(1, 2)
print r1 + r2
print r1 - r2
print r1 * r2
print r1 / r2


print "=================================="
# 6-6
print int(12.34)
print float(12)

class Rational(object):
    def __init__(self, p, q):
        self.p = p
        self.q = q
    def __int__(self):
        return self.p // self.q
    def __float__(self):
        return float(self.p) / float(self.q)
print int(Rational(7, 2))
print int(Rational(1, 3))
print float(Rational(7, 2))
print float(Rational(1, 3))


print "=================================="
# 6-7

class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def get_score(self):
        return self.__score
    def set_score(self, score):
        if score < 0 or score > 100:
            raise ValueError('invalid score')
        self.__score = score
s = Student('Bob', 59)
s.score = 60
print s.score
# s.set_score(1000)
print s.score


class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score  = score
    @property
    def score(self):
        return self.__score
    @score.setter
    def score(self, score):
        if score < 0 or score > 100:
            raise ValueError('invalid score')
        self.__score = score
s = Student('Bob', 59)
s.score = 60
print s.score
# s.score = 1000
print s.score


class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.__score = score

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, score):
        if score < 0 or score > 100:
            raise ValueError('invalid score')
        self.__score = score
    @property
    def grade(self):
        if self.score >= 80 and self.score <= 100:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'


s = Student('Bob', 59)
print s.grade

s.score = 60
print s.grade

s.score = 99
print s.grade

print "=================================="
# 6-8
class Student(object):
    __slots__ = ('name', 'gender', 'score')
    def __init__(self, name, gender, score):
        self.name = name
        self.gender = gender
        self.score = score
s = Student('Bob', 'male', 59)
s.name = 'Tim'
s.score = 99
# s.grade = 'A'
print s.name
print s.score


class Person(object):

    __slots__ = ('name', 'gender')

    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

class Student(Person):

    __slots__ = ('name', 'gemder', 'score')

    def __init__(self, name, gender, score):
        super(Student, self).__init__(name, gender)
        self.score = score
s = Student('Bob', 'male', 59)
s.name = 'Tim'
s.score = 99
print s.score


print "=================================="
# 6-9
f = abs
print f.__name__
print f(-123)

class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
    def __call__(self, friend):
        print 'My name is %s...' % self.name
        print 'My friend is %s...' % friend
