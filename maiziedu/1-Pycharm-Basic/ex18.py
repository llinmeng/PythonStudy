# -*- coding: utf-8 -*-
# 写出文件
# 读入文件

some_sentences = '''\
I love learning python
because python is fun
and also easy to use
'''

# 注意路径
f = open('sentences.txt', 'w')
f.write(some_sentences)
f.close()

f = open('sentences.txt')
while True:
    line = f.readline()
    if len(line) == 0:
        break
    print line
f.close
