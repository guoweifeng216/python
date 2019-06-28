#!/usr/bin/env python
# coding=utf-8
"""

@athor:weifeng.guo 
@data:2019/6/25 14:00
@filename:simple_mark

"""
import sys,re
from chapter20.util import *

print('<html><head><title>...</title><body>')
title = True
for block in blocks(sys.stdin):
    block = re.sub(r'\*(.+?)\*', r'<em>\1</em>', block)
    if title:
        print('<h1>')
        print(block)
        print('</h1>')
        title = False
    else:
        print('<p>')
        print(block)
        print('</p>')
print('</body></html>')