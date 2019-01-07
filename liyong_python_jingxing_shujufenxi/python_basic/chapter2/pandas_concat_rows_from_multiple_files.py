#!/usr/bin/env python
# coding=utf-8
"""

@athor:weifeng.guo 
@data:2019/1/4 16:55
@filename:pandas_concat_rows_from_multiple_files

"""
import pandas as pd
import glob
import os
import sys
input_path = sys.argv[1]
output_file = sys.argv[2]
all_files = glob.glob(os.path.join(input_path,'supplier*.csv'))
all_data_frames = []
for file in all_files:
    data_frame = pd.read_csv(file, index_col=None)
    all_data_frames.append(data_frame)
# print(all_data_frames[0])
# print(all_data_frames[1])
# print(all_data_frames[2])
data_frame_concat = pd.concat([all_data_frames[0],all_data_frames[1],all_data_frames[2]], axis=0, sort=True, ignore_index=True)
"""# 这段代码垂直堆叠数据框。如果你需要平行连接数据，那么就在 concat 函数中设置
axis=1 """
print(data_frame_concat)
data_frame_concat.to_csv(output_file, index=False)