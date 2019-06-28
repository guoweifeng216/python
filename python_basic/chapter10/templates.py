#!/usr/bin/env python
# coding=utf-8
"""

@athor:weifeng.guo 
@data:2019/6/20 14:11
@filename:templates

"""
import fileinput, re

field_pat = re.compile(r'\[(.+?)\]')
scope = {}


def replacement(match):
    code = match.group(1)
    try:
        return str(eval(code, scope))
    except SyntaxError:
        return ''


lines = []

for line in fileinput.input():
    lines.append(line)

text = ''.join(lines)

print(text)
print(field_pat.sub(replacement, text))
