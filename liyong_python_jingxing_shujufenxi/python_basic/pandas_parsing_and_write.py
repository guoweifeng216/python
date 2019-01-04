#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

@athor:weifeng.guo 
@data:2019/1/3 18:47
@filename:pandas_ parsing_and_write

"""
import sys
import pandas as pd
input_file = sys.argv[1]
output_file = sys.argv[2]
data_frame = pd.read_csv(input_file)
print(data_frame)
data_frame.to_csv(output_file, index=False)