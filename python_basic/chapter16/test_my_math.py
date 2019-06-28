#!/usr/bin/env python3
# coding=utf-8
"""

@athor:weifeng.guo 
@data:2019/6/25 9:41
@filename:test_my_math

"""
import unittest
from chapter16 import my_math


class test_integer(unittest.TestCase):

    def test_integers(self):
        for x in range(-10, 10):
            for y in range(-10, 10):
                p = my_math.product(x, y)
                self.assertEqual(p, x * y, 'Integer multiplication failed')

    def test_floats(self):
        for x in range(-10, 10):
            for y in range(-10, 10):
                x = x /10
                y = y / 10
                p = my_math.product(x, y)
                self.assertEqual(p, x * y, 'Floats multiplication failed')