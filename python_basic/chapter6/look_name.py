#!/usr/bin/env python
# coding=utf-8
"""

@athor:weifeng.guo 
@data:2019/6/12 14:33
@filename:look_name

"""
import operator

def loop_up_name(data,label,name):
    return data[label].get(name)


def init_data(data):
    data['first'] = {}
    data['middle'] = {}
    data['last'] = {}


def store_data(data, full_name):
    names = full_name.split()
    if len(names) == 2:
        names.insert(1, '')
    labels = 'first', 'middle', 'last'
    for name, label in zip(names,labels):
        people = loop_up_name(data, label, name)
        if people:
            people.append(full_name)
        else:
            data[label][name] = [full_name]


mydict = {}
init_data(mydict)
store_data(mydict, 'Magnus Lie Hetland')
store_data(mydict, 'Robin Hood')
store_data(mydict, 'Robin Locksley')
store_data(mydict, 'Mr. Gumby')
print(loop_up_name(mydict, 'first', 'Robin'))
print(loop_up_name(mydict, 'middle', 'Lie'))
print(loop_up_name(mydict, 'middle', ''))