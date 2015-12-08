# -*- coding: utf-8 -*-
# Python有两种错误类型：
# 语法错误(Syntax Errors)
# 异常（Exceptions)


# 首先，try语句下的（try和except之间的代码）被执行
# 如果没有出现异常，except语句将被忽略
# 如果try语句之间出现了异常，try之下异常之后的代码被忽略，直接跳跃到except语句
# 如果异常出现，但并不属于except中定义的异常类型，程序将执行外围一层的try语句，如果异常没有被处理，
# 将产生unhandled exception的错误

# 1:
# 处理异常（Handling Exceptions)

# Exception doc:
# https://docs.python.org/3.4/library/exceptions.html

# Example of Syntax errors

# while True print("Hello World!")
"""
while True:
    print("Hello World!")
"""

# Examples of exceptions

"""
print(8/0)
print(hello * 4)
num = 6
print "Hello World " + num
"""
# Handling exceptions
"""
while True:
    try:
        x = int(raw_input("Please enter a number"))
        break
    except ValueError:
        print "Not valid input, try again..."

"""


# 2:
try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())                  # strip(): 清理字符串的空格(前后)
except IOError as err:                  # 系统性的错误
    print "IO error: {0}".format(err)
except ValueError:                      # 自带的错误类型-值错误
    print "Could not convert data to an integer."
