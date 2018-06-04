from tkinter import *

def clearBoxes(e):
    state.set("")
    listContents.set(tuple([]))
     
def senate():
    L = []
    result = state.get()
    for line in open("Senate114.txt", 'r'):
        temp = line.split(',')
        if temp[1] == result:
            L.append(temp[0] + "  " + temp[2])
            listContents.set(tuple(L))

window = Tk()
window.title("U.S. Senate")
Label(window, text="State:", width=5).grid(row=0, column=0, sticky=E)
state = StringVar()
entState = Entry(window, textvariable=state)
entState.grid(row=0, column=1, sticky=W)
entState.focus_set()
entState.bind("<Button-1>", clearBoxes) # to trigger event
                    # click on Entry box with left mouse button
btnDisplay = Button(text="Display Senators", command=senate)
btnDisplay.grid(row=1, columnspan=2, pady = 10)
L = []
listContents = StringVar()
listContents.set(tuple(L))
lstSenators = Listbox(window, height=2, width=21, listvariable=listContents)
lstSenators.grid(row=2,column=0, columnspan=2, padx=44, pady=2)
window.mainloop()


##from tkinter import *
##
##class Senators:
##
##    def __init__(self):
##        window = Tk()
##        window.title("U.S. Senate")
##        Label(window, text="State:", width=5).grid(row=0, column=0, sticky=E)
##        self.state = StringVar()
##        entState = Entry(window, textvariable=self.state)
##        entState.grid(row=0, column=1, sticky=W)
##        entState.focus_set()
##        entState.bind("<Button-1>", self.clearBoxes) # to trigger event
##                            # click on Entry box with left mouse button
##        btnDisplay = Button(text="Display Senators", command=self.senate)
##        btnDisplay.grid(row=1, columnspan=2, pady = 10)
##        self.L = []
##        self.listContents = StringVar()
##        self.listContents.set(tuple(self.L))
##        lstSenators = Listbox(window, height=2, width=21,
##                              listvariable=self.listContents)
##        lstSenators.grid(row=2,column=0, columnspan=2, padx=44, pady=2)
##        window.mainloop()
##        
##    def clearBoxes(self, e):
##        self.state.set("")
##        self.listContents.set(tuple([]))
##         
##    def senate(self):
##        self.L = []
##        result = self.state.get()
##        for line in open("Senate114.txt", 'r'):
##            temp = line.split(',')
##            if temp[1] == result:
##                self.L.append(temp[0] + "  " + temp[2])
##                self.listContents.set(tuple(self.L))
##                         
##Senators()
##
##
