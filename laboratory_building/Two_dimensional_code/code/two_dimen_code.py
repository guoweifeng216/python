#!/usr/bin/env python
# coding=utf-8
"""
author:     weifeng.guo 
data:       2019/10/23 15:34
filename:   two_dimen_code
"""
from MyQR import myqr
myqr.run(words='https://www.shiyanlou.com',
        picture='wm.gif',
        colorized=True,
        save_name='artistic_Color.gif',
         )