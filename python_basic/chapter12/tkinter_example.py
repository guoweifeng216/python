#!/usr/bin/env python
# coding=utf-8
"""

@athor:weifeng.guo 
@data:2019/6/21 9:50
@filename:tkinter_example

"""
from tkinter import *
top = Tk()
def clicked():
    print("I was clicked!")
# btn = Button()
# btn.pack()
# btn['text'] = 'Click me!'
# btn['command'] = clicked
# # Label(text="I'm in the first window!").pack()
# second = Toplevel()
# Label(second, text="I'm in the second window!").pack()
# for i in range(10):
#     Button(text=i).pack()
def callback(event):
    print(event.x, event.y)

top.bind('Button-1', callback)
mainloop()