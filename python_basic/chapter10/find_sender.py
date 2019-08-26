#!/usr/bin/env python
# coding=utf-8
"""
author:     weifeng.guo 
data:       2019/8/23 10:21
filename:   find_sender
"""
import fileinput, re

pat = re.compile('From: (.*) <.*?>$')
for line in fileinput.input():
    m = pat.match(line)
    if m:print(m.group(1))
