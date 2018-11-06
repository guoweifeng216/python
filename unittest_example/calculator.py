#!/usr/bin/env/python
#coding=utf-8
"""
math calculator
author: weifeng.guo
"""
class Count():
    def __init__(self, a, b):
        self.a = int(a)
        self.b = int(b)

    def add(self):
        """计算加法"""
        return self.a + self.b

    def sub(self):
        """计算减法"""
        return self.a - self.b

