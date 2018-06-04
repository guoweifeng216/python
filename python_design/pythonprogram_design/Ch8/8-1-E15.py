from tkinter import *
window = Tk()
window.title("Nations")
infile = open("UN.txt", 'r')
listOfNations = [line.split(',')[0] for line in infile]
conOFlstNations = StringVar()
lstNations = Listbox(window, height=10, 
                     width=38, listvariable=conOFlstNations)
lstNations.grid(padx=15, pady=5)
conOFlstNations.set(tuple(listOfNations))
window.mainloop()


##from tkinter import *
##
##class Continents:
##
##    def __init__(self):
##        window = Tk()
##        window.title("Nations")
##        listOfNations = [line.split(',')[0] for line in open("UN.txt", 'r')]
##        conOFlstNations = StringVar()
##        lstNations = Listbox(window, height=10, 
##                             width=38, listvariable=conOFlstNations)
##        lstNations.grid(row=1, column=0, padx=15, pady=5)
##        conOFlstNations.set(tuple(listOfNations))
##        window.mainloop()
##
##Continents()
