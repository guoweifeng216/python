# -*- coding: utf-8 -*-
"""
pandas 学习笔记
"""

"""
pandas数据结构包括：
    DataFrame 是带标签的二维对象，生成DataFrame方式
        1）从另一个DataFrame创建
        2）从一个具有二维形状Numpy数组或者数组的复合结构来生成
        3）可以用pandas中的Series来创建
        4）可以从CSV文件之类的文件生成
        
    Series是不同类型的元素组成的一维数组，生成方式有：
        1）由python的字典来创建
        2）Numpy数组创建，索引值从0开始递增
        3）由单个标量值创建
"""
"""
pandas应用
    1）查询数据
    2）进行统计计算
    3）实现数据聚合（数据聚合）
    4）进行数据连接
    5）处理日期数据
    6）数据透析
    7）访问远程数据
"""
"""
pandas.groupby()分组
pandas.merge()参数
    how：
        1）inner 内连接，取交集,
        2）outer 外连接，取并集，并用nan填充”
        3）left 左连接， 左侧取全部，右侧取部分”
        4）right 有连接，左侧取部分，右侧取全部”
        
    right	参与合并的右侧DataFrame
    on	用于连接的列名，必须存在于左右两个DataFrame
    left_on	左侧DataFrame中用作连接键的列
    right_on	右侧DataFrame中用作连接键的列
    left_index	将左侧的行索引用作其连接键
    right_index	将右侧的行索引用作其连接键
    sort	根据连接键对合并后的数据进行排列，默认为True
    suffixes	字符串值元组，用于追加到重叠列名的末尾，默认为(‘_x’,‘_y’)。如果左右两个DataFrame对象都有“data”，则结果就会出现“data_x”和“data_y”
    copy	默认为True。如果设置为False，可以避免将数据复制到结果数据结构
"""