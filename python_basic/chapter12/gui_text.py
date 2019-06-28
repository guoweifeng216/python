#!/usr/bin/env python
# coding=utf-8
"""

@athor:weifeng.guo 
@data:2019/6/21 10:56
@filename:gui_text

"""
from tkinter import *
from tkinter.scrolledtext import ScrolledText



top = Tk()
top.title("Simple Editor")
contents = ScrolledText()
contents.pack(side=BOTTOM, expand=True, fill=BOTH)
filename = Entry()
filename.pack(sid=LEFT, expand=True, fill=X)


def load():
    with open(filename.get()) as file:
        contents.delete('1.0', END)
        contents.insert(INSERT, file.read())


def save():
    with open(filename.get(), 'w') as file:
        file.write(contents.get('1.0', END))


Button(text='Open',command=load).pack(side=LEFT)
Button(text='Save', command=save).pack(side=LEFT)
mainloop()
