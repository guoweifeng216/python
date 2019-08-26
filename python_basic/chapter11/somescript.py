#!/usr/bin/env python
# coding=utf-8
"""
author:     weifeng.guo 
data:       2019/8/23 13:46
filename:   somescript
"""
import sys
text = sys.stdin.read()
words = text.split()
wordcount = len(words)
print('wordcount:', wordcount)
