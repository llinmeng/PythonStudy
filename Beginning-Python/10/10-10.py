# -*- coding:utf-8 -*-
# find_sender.py

import fileinput
import re

pat = re.compile('From: (.*) <.*?>$')
for line in fileinput.input():
    m = pat.match(line)
    if m:
        print m.group(1)


pat = re.compile(r'[a-z\-\.]+@[a-z\-\.]+', re.IGNORECASE)
addresses = set()
for line in fileinput.input():
    for address in pat.findall(line):
        addresses.add(address)
for address in sorted(addresses):
    print address


'''
# exec
from math import sqrt
scope = {}
exec 'sqrt = 1' in scope
print sqrt(4)
print scope['sqrt']
print "len = ", len(scope)
print scope.keys()
'''


'''
# eval
# print eval(raw_input("Enter an asrithmet expression: "))

scope = {}
scope['x'] = 2
scope['y'] = 3
print eval('x * y', scope)

scope = {}
exec 'x = 2' in scope
print eval('x * x', scope)
'''