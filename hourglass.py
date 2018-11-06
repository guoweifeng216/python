#coding=utf-8
"""
@athor:weifeng.guo 
@data:2018/9/11 16:58
@filename:hourglass
"""

h = 0
i = 0
middle_num = 7 // 2
while i < 7:
    if i <= middle_num:
        h = i
    else:
        h -= 1
    n = 7 - h*2
    print ' '* h,
    j = 0
    while j < n:
        print '*' ,
        j +=1
    print '\n'
    i +=1

