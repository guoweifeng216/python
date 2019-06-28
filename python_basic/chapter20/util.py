#!/usr/bin/env python
# coding=utf-8
"""

@athor:weifeng.guo 
@data:2019/6/25 13:55
@filename:util

"""


def lines(file):
    for line in file: yield line
    yield '\n'

def blocks(file):
    block = []
    for line in lines(file):
        if line.strip():
            block.append(line)
        elif block:
            yield ''.join(block).strip()
            block = []