# -*-  coding: utf-8 -*-
import fileinput
import re

field_pat = re.compile(r'\[(.+?)\]')

scope = {}


def replacement(match):
    code = match.group(1)
    try:
        return str(eval(code, scope))
    except SyntaxError:
        exec code in scope
        return ''


lines = []
for line in fileinput.input():
    lines.append(line)
text = ''.join(lines)

print field_pat.sub(replacement, text)


# 10-12 为其模板示例
# 10-13 模板定义
# 10-14 模板文件