#coding=utf-8
"""
@athor:weifeng.guo 
@data:2018/9/28 14:41
@filename:排序
"""
from operator import itemgetter

alist = [('2', '3', '10'), ('1', '2', '3'), ('5', '6', '7'), ('2', '5', '10'), ('2', '4', '10')]

# 多级排序，先按照第3个元素排序，然后按照第2个元素排序：
print sorted(alist, cmp=None, key=itemgetter(2, 1), reverse=False)
print sorted(alist, cmp=None, key=lambda x: itemgetter(2, 1)(x), reverse=False)
print sorted(alist, cmp=None, key=lambda x: map(int, itemgetter(2, 1)(x)), reverse=False)