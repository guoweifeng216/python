#!/usr/bin/env python
# coding=utf-8
"""

@athor:weifeng.guo 
@data:2019/1/8 14:19
@filename:pandas_value_ meets_condition_all_worksheets

"""
import pandas as pd
import sys
input_file = sys.argv[1]
output_file = sys.argv[2]
"""
在 pandas 中，通过在 read_excel 函数中设置 sheetname=None，可以一次性读取工作簿中的
所有工作表。 
"""
data_frame = pd.read_excel(input_file, sheetname=None, index_col=None)
row_output = []

for worksheet_name, data in data_frame.items():
    row_output.append(data[data['Sale Amount'].astype(float) > 1500.0])
filtered_rows = pd.concat(row_output, axis=0, ignore_index=True)
writer = pd.ExcelWriter(output_file)
filtered_rows.to_excel(writer, sheet_name='sale_amount_gt2000', index=False)
writer.save()