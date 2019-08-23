#!/usr/bin/env python
# coding=utf-8
"""
author:     weifeng.guo
data:       2019/8/22 11:45
filename:   numberlines
"""
import fileinput

for line in fileinput.input():
    line = line.rstrip()
    num = fileinput.lineno()
    print('{:<50} # {:2d}'.format(line, num))