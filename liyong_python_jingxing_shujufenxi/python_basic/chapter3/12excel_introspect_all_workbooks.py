#!/usr/bin/env python
# coding=utf-8
"""

@athor:weifeng.guo 
@data:2019/1/9 15:33
@filename:12excel_introspect_all_workbooks

"""
import csv
import glob
import os
import sys
from xlrd import open_workbook

input_path = sys.argv[1]

workbook_counter = 0
for input_file in glob.glob(os.path.join(input_path, '*.xls')):
    workbook = open_workbook(input_file)
    print('Workbook: %s' % os.path.basename(input_file))
    print('Number of worksheets: %d' % workbook.nsheets)
    for worksheet in workbook.sheets():
        print('Worksheet name:', worksheet.name, '\tRows:',worksheet.nrows, '\tColumns:', worksheet.ncols)
    workbook_counter += 1
print("Number of files: {0:d}".format(workbook_counter))