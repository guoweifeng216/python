#!/usr/bin/env python
# coding=utf-8
"""

@athor:weifeng.guo 
@data:2019/1/4 11:10
@filename:7csv_reader_column_by_name

"""
import sys
import csv
input_file = sys.argv[1]
output_file = sys.argv[2]
my_columns = ['Invoice Number', 'Parchase Date']
my_columns_index = []
with open(input_file, 'r', newline='') as csv_in_file:
    with open(output_file, 'w', newline='') as csv_out_file:
        filereader = csv.reader(csv_in_file)
        filewrite = csv.writer(csv_out_file)
        header = next(filereader, None)
        for index_value in range(len(header)):
            if header[index_value] in my_columns:
                my_columns_index.append(index_value)
        filewrite.writerow(my_columns)
        for row_list in filereader:
            row_list_out = []
            for index_value in my_columns_index:
                row_list_out.append(row_list[index_value])
            filewrite.writerow(row_list_out)
