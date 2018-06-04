from tkinter import *

window = Tk()
window.title("States")
infile = open("StatesANC.txt", 'r')
listOfStates = [line.split(',')[0] for line in infile]
infile.close()
conOFlstStates = StringVar()
lstStates = Listbox(window, height=10, width=12,
                    listvariable=conOFlstStates)
lstStates.grid(padx=75, pady=5)
conOFlstStates.set(tuple(listOfStates))
window.mainloop()


##from tkinter import *
##
##class States:
##
##    def __init__(self):
##        window = Tk()
##        window.title("States")
##        listOfStates = [line.split(',')[0] \
##                        for line in open("StatesANC.txt", 'r')]
##        conOFlstStates = StringVar()
##        lstStates = Listbox(window, height=10, 
##                             width=12, listvariable=conOFlstStates)
##        lstStates.grid(row=1, column=0, padx=75, pady=5)
##        conOFlstStates.set(tuple(listOfStates))
##        
##States()
