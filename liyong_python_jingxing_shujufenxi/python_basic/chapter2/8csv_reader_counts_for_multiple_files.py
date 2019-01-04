#!/usr/bin/env python
# coding=utf-8
"""

@athor:weifeng.guo 
@data:2019/1/4 15:43
@filename:8csv_reader_counts_for_multiple_files

"""
import csv
import glob
import os
import sys
input_path = sys.argv[1]

file_counter = 0
for input_file in glob.glob(os.path.join(input_path, 'supplier*.csv')):
    row_counter = 0
    with open(input_file, 'r', newline='') as csv_file:
        filereader = csv.reader(csv_file)
        header = next(filereader, None)
        for row in filereader:
            row_counter +=1
    print("{0!s}: \t{1:d} rows \t{2:d} columns".format(os.path.basename(input_file), row_counter, len(header)))
    file_counter += 1
print("Number of files: {0:d}".format(file_counter))