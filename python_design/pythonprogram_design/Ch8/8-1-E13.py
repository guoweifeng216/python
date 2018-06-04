def convertToUC(event):
    state = lstStates.get(lstStates.curselection())
    n = listOfStates.index(state)
    listOfStates.remove(state)
    listOfStates.insert(n, state.upper())
    conOFlstStates.set(tuple(listOfStates))

from tkinter import *
window = Tk()
window.title("States")
infile = open("StatesANC.txt", 'r')
listOfStates = [line.split(',')[0] for line in infile]
infile.close()
conOFlstStates = StringVar()
lstStates = Listbox(window, height=10, 
                    width=15, listvariable=conOFlstStates)
lstStates.grid(padx=75, pady=5)
conOFlstStates.set(tuple(listOfStates))
lstStates.bind("<<ListboxSelect>>", convertToUC)
window.mainloop()



##from tkinter import *
##
##class States:
##
##    def __init__(self):
##        window = Tk()
##        window.title("States")
##        global listOfStates
##        listOfStates = [line.split(',')[0] for line in open("StatesANC.txt", 'r')]
##        self.conOFlstStates = StringVar()
##        global lstStates
##        lstStates = Listbox(window, height=10, 
##                            width=15, listvariable=self.conOFlstStates)
##        lstStates.grid(row=1, column=0, padx=75, pady=5)
##        self.conOFlstStates.set(tuple(listOfStates))
##        lstStates.bind("<<ListboxSelect>>", self.convertToUC)
##
##    def convertToUC(self, e):
##        state = lstStates.get(lstStates.curselection())
##        n = listOfStates.index(state)
##        listOfStates.remove(state)
##        listOfStates.insert(n, state.upper())
##        self.conOFlstStates.set(tuple(listOfStates))
##
##States()
