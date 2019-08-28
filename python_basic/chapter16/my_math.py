#!/usr/bin/env python
# coding=utf-8
"""

@athor:weifeng.guo 
@data:2019/6/25 9:46
@filename:my_math

"""


def product(x, y):
    return x * y


if __name__ == '__main__':
    import doctest
    import my_math
    import unittest
    doctest.testmod(my_math)
