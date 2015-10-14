# -*- coding:utf-8 -*-
import fileinput

for line in fileinput.input(inplace=True):
    line = line.rstrip()
    num = fileinput.lineno()
    print '%-40s # %2i' % (line, num)



# python 10-6.py 10-6.py