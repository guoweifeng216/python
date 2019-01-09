#!/usr/bin/env python
# coding=utf-8
"""

@athor:weifeng.guo 
@data:2019/1/8 10:43
@filename:8excel_column_by_name

"""
import sys
from datetime import date
from xlrd import open_workbook, xldate_as_tuple
from xlwt import Workbook
input_file = sys.argv[1]
output_file = sys.argv[2]
output_workbook = Workbook()
output_worksheet = output_workbook.add_sheet('jan_2013_output')
my_column = ['Customer ID', 'Purchase Date']
purchase_date_column_index = 4
with open_workbook(input_file) as workbook:
    worksheet = workbook.sheet_by_name('january_2013')
    data = [my_column]
    header_list = worksheet.row_values(0)
    header_index_list = []
    for header_index in range(len(header_list)):
        if header_list[header_index] in my_column:
            header_index_list.append(header_index)
    print(header_index_list)
    for row_index in range(worksheet.nrows):
        row_list = []
        for column_index in header_index_list:
            cell_value = worksheet.cell_value(row_index, column_index)
            cell_type = worksheet.cell_type(row_index, column_index)
            if cell_type == 3:
                date_cell = xldate_as_tuple(cell_value, workbook.datemode)
                date_cell = date(*date_cell[0:3]).strftime('%m/%d/%Y')
                row_list.append(date_cell)
            else:
                row_list.append(cell_value)

        data.append(row_list)
    for list_index, output_list in enumerate(data):
        for element_index, element in enumerate(output_list):
            output_worksheet.write(list_index, element_index, element)

output_workbook.save(output_file)