from tkinter import *

def senate(e):
    L = []
    state = lstStates.get(lstStates.curselection())
    for line in open("Senate114.txt", 'r'):
        temp = line.split(',')
        if temp[1] == state:
            L.append(temp[0] + "  " + temp[2])
    conOFlstSenators.set(tuple(L))

window = Tk()
window.title("U.S. Senate")
instruction = "Click on a state."
Label(window, text=instruction).grid(row=0, column=0, columnspan=3, pady=5)
Label(window, text="STATE", width=14).grid(row=1, column=0)
Label(window, text="SENATORS").grid(row=1, column=2)
yscroll = Scrollbar(window, orient=VERTICAL)
yscroll.grid(row=2, column=1, pady=5, sticky=NS)
stateSet = {line.split(',')[1] for line in open("Senate114.txt", 'r')}
stateList = list(stateSet)
stateList.sort()
conOFlstStates = StringVar()
lstStates = Listbox(window, width=14, height=7, listvariable=conOFlstStates, yscrollcommand=yscroll.set)
lstStates.grid(row=2, column=0, pady=5, sticky=E)
lstStates.bind("<<ListboxSelect>>", senate)
conOFlstStates.set(tuple(stateList))
conOFlstSenators = StringVar()
lstSenators = Listbox(window, width=18, height=2, listvariable=conOFlstSenators)
lstSenators.grid(row=2, column=2, padx=8, pady=5, sticky=N)
yscroll["command"] = lstStates.yview               
window.mainloop()

##from tkinter import *
##
##class Senators:
##
##    def __init__(self):
##        window = Tk()
##        window.title("U.S. Senate")
##        instruction = "Click on a state."
##        Label(window, text=instruction).grid(row=0, column=0,
##                                             columnspan=3, pady=5)
##        Label(window, text="STATE", width=14).grid(row=1, column=0)
##        Label(window, text="SENATORS").grid(row=1, column=2)
##        yscroll = Scrollbar(window, orient=VERTICAL)
##        yscroll.grid(row=2, column=1, pady=5, sticky=NS)
##        stateSet = {line.split(',')[1] for line in open("Senate113.txt", 'r')}
##        stateList = list(stateSet)
##        stateList.sort()
##        conOFlstStates = StringVar()
##        self._lstStates = Listbox(window, width=14, height=7,
##                     listvariable=conOFlstStates, yscrollcommand=yscroll.set)
##        self._lstStates.grid(row=2, column=0, pady=5, sticky=E)
##        self._lstStates.bind("<<ListboxSelect>>", self.senate)
##        conOFlstStates.set(tuple(stateList))
##
##        self._conOFlstSenators = StringVar()
##        self._lstSenators = Listbox(window, width=18, height=2,
##                                    listvariable=self._conOFlstSenators)
##        self._lstSenators.grid(row=2, column=2, padx=8, pady=5, sticky=N)
##        yscroll["command"] = self._lstStates.yview               
##        window.mainloop()
##
##    def senate(self, e):
##        self.L = []
##        state = self._lstStates.get(self._lstStates.curselection())
##        for line in open("Senate113.txt", 'r'):
##            temp = line.split(',')
##            if temp[1] == state:
##                self.L.append(temp[0] + "  " + temp[2])
##        self._conOFlstSenators.set(tuple(self.L))
##
##Senators()
##
##
