def addAbbreviation(e):
    state = lstStates.get(lstStates.curselection())
    abbreviation = findAbbreviation(state)
    n = listOfStates.index(state)
    listOfStates.remove(state)
    listOfStates.insert(n, state + " (" + abbreviation + ")")
    conOFlstStates.set(tuple(listOfStates))

def findAbbreviation(state):
    infile = open("StatesANC.txt", 'r')
    for line in infile:
        if line.split(',')[0] == state:
            return line.split(',')[1]

from tkinter import *
window = Tk()
window.title("States")
global listOfStates
listOfStates = [line.split(',')[0] for line in open("StatesANC.txt", 'r')]
conOFlstStates = StringVar()
global lstStates
lstStates = Listbox(window, height=10,                                                                                                                                              
                    width=15, listvariable=conOFlstStates)
lstStates.grid(padx=75, pady=5)
conOFlstStates.set(tuple(listOfStates))
lstStates.bind("<<ListboxSelect>>", addAbbreviation)
window.mainloop()
