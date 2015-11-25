# -*- coding:utf-8 -*-
# 为以编号的行进行编号
import fileinput

for line in fileinput.input(inplace=1):
    line = line.rstrip()
    num = fileinput.lineno()
    print '%-40s # %2i' % (line, num)



