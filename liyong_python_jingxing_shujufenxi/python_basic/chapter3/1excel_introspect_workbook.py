#!/usr/bin/env python
# coding=utf-8
"""

@athor:weifeng.guo 
@data:2019/1/7 10:46
@filename:1excel_introspect_workbook

"""
import sys
from xlrd import open_workbook
input_file = sys.argv[1]
workbook = open_workbook(input_file)
print("Number of worksheets:{}".format(workbook.nsheets))
for worksheet in workbook.sheets():
    print("Worksheet name:", worksheet.name, "\tRows:", worksheet.nrows, "\tColumns:", worksheet.ncols)
