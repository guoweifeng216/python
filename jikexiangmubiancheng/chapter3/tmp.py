#!/usr/bin/env python
# coding=utf-8
"""

@athor:weifeng.guo 
@data:2018/12/25 9:55
@filename:tmp

"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

x = np.array([[0, 255, 255], [255, 255, 0], [0, 255, 0]])
plt.imshow(x, interpolation='nearest')
plt.show()