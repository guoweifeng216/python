from tkinter import *
import pickle

def displayData(e):
    lake = lstLakes.get(lstLakes.curselection())
    conOFentArea.set("{0:,d}".format(lakesDict[lake]))

window = Tk()
window.title("Great Lakes")
global lakesDict
lakesDict = {"Huron":23000, "Ontario":8000, "Michigan":22000,
                     "Erie":10000, "Superior":32000}
lakeList = list((lakesDict).keys())
lakeList.sort()
conOFlstLakes = StringVar()
global lstLakes
lstLakes = Listbox(window, height=5, width=9, listvariable=conOFlstLakes)
lstLakes.grid(row=0, column=0, padx=5, pady=5, rowspan=5, sticky=NSEW)
conOFlstLakes.set(tuple(lakeList))
lstLakes.bind("<<ListboxSelect>>", displayData)
Label(window, text="Area (sq. miles):").grid(row=2, column=1, sticky=E)
conOFentContinent = StringVar()
conOFentArea = StringVar()
entArea = Entry(window, width=7, state="readonly", textvariable=conOFentArea)
entArea.grid(row=2, column=2, padx=5)
window.mainloop()


##from tkinter import *
##import pickle
##
##class GreatLakes:
##    
##    def __init__(self):
##        window = Tk()
##        window.title("Great Lakes")
##        global lakesDict
##        lakesDict = {"Huron":23000, "Ontario":8000, "Michigan":22000,
##                     "Erie":10000, "Superior":32000}
##        self._lakeList = list((lakesDict).keys())
##        self._lakeList.sort()
##        self._conOFlstLakes = StringVar()
##        global lstLakes
##        lstLakes = Listbox(window, height=5, width=9,
##                listvariable=self._conOFlstLakes)
##        lstLakes.grid(row=0, column=0, padx=5, pady=5, rowspan=5, sticky=NSEW)
##        self._conOFlstLakes.set(tuple(self._lakeList))
##        lstLakes.bind("<<ListboxSelect>>", self.displayData)
##        Label(window, text="Area (sq. miles):").grid(row=2, column=1, sticky=E)
##        self._conOFentContinent = StringVar()
##        self._conOFentArea = StringVar()
##        entArea = Entry(window, width=7, state="readonly",
##                        textvariable=self._conOFentArea)
##        entArea.grid(row=2, column=2, padx=5)
##
##    def displayData(self, e):
##        lake = lstLakes.get(lstLakes.curselection())
##        self._conOFentArea.set("{0:,d}".format(lakesDict[lake]))
##        
##GreatLakes()
