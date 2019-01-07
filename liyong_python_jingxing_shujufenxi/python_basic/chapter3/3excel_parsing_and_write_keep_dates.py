#!/usr/bin/env python
# coding=utf-8
"""

@athor:weifeng.guo 
@data:2019/1/7 14:16
@filename:3excel_parsing_and_write_keep_dates

"""
import sys
from datetime import date
from xlrd import open_workbook, xldate_as_tuple
from xlwt import Workbook
input_file = sys.argv[1]
output_file = sys.argv[2]
output_workbook = Workbook()
output_worksheet = output_workbook.add_sheet('jan_2013_output')
with open_workbook(input_file) as workbook:
    worksheet = workbook.sheet_by_name('january_2013')
    for row_index in range(worksheet.nrows):
        row_list_output = []
        for column_index in range(worksheet.ncols):
            if worksheet.cell_type(row_index, column_index) == 3:
                data_cell = xldate_as_tuple(worksheet.cell_value(row_index, column_index),workbook.datemode)
                data_cell = date(*data_cell[0:3]).strftime('%m/%d/%Y')
                row_list_output.append(data_cell)
                output_worksheet.write(row_index, column_index, data_cell)
            else:
                non_date_cell = worksheet.cell_value(row_index,column_index)
                row_list_output.append(non_date_cell)
                output_worksheet.write(row_index,column_index,non_date_cell)

output_workbook.save(output_file)