# -*- coding: utf-8 -*-
import numpy as np

np.arange() #默认生成一维数组
np.arange(6).reshape(2,3) #生成二维数组，每维含有三个元素
np.arange(9).reshape(3,3) #生成三维数组，每维含有单行三列
a = np.arange(27).reshape(3,3,3)#生成三维数组，每维含有三行三列
a.ravel() #将a数组转化成一维数组
a.flatten()#将数组拉直，类似ravel,但是flatten返回的是真实数组，需要分配内存，而ravel不需要内存
a.tanspose()#将数组转置
a.reshape()#用来定义数组的形状
a.resize()#与reshape功能类似
#数组叠加水平叠加、垂直叠加、深度叠加、列式叠加、行式叠加
#数组拆分纵向拆分、横向拆分、深向拆分
"""
数组属性包括:
        a.ndim 表示维度的数量
        a.size表示数组的元素的数量
        a.itemsize 表示返回数组中各个元素所占的字节数
        a.nbytes表示数组总共字节大小
        a.T 与transpose功能相同
        a.real返回数组的实部
        a.image返回数组的虚部
"""
"""
数组转换：
    转换成列表用属性tolist()函数
    astype()可以将数组元素转换成指定的类型，数据类型要以字符串的方式转入astype('数据类型')
    复数转换成整数时虚部将会被舍弃
"""
"""
numpy.linalg.inv()来求矩阵的逆矩阵（原矩阵乘以逆矩阵为单位矩阵）
numpy.linalg.solve()求解线性方程组的解
numpy.dot()用来校验线性方程的解
numpy.linalg.eigvals()来求线性方程组的特征值
numpy.linalg.eig()来求线性方程组的特征向量,返回是一个元组，其中第一个元素是特征值，第二个元素是相应的特征向量
numpy.random.binomial()用来随机数

"""
