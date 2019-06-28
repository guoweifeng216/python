#!/usr/bin/env python
# coding=utf-8
"""

@athor:weifeng.guo 
@data:2019/6/26 9:37
@filename:hello_report

"""

from reportlab.graphics.shapes import Drawing, String
from reportlab.graphics import renderPDF

d = Drawing(100, 100)
s = String(50, 50, 'Hello, world!', textAnchor='middle')
d.add(s)
renderPDF.drawToFile(d, 'hello.pdf', 'A simple PDF file')