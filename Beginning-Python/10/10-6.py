# -*- coding:utf-8 -*-
# 为python脚本添加行号  # 每运行一次, 添加一次行号
import fileinput

for line in fileinput.input(inplace=True):          # inplace=True: 原地处理
    line = line.rstrip()                            # rstrip(): 可以返回字符串副本的字符串方法, 右侧的空格都被删除
    num = fileinput.lineno()                        # lineno(): 返回当前(累计)的行数
    print '%-40s # %2i' % (line, num)



# python 10-6.py 10-6.py