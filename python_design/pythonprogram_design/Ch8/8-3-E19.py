from tkinter import *

def checkAnswer():
    m = people.index(lstPeople.get(lstPeople.curselection()))
    n = places.index(lstPlaces.get(lstPlaces.curselection()))
    if m == n:
        conOFentAnswer.set("CORRECT")
    else:                               
        conOFentAnswer.set("INCORRECT")                   

window = Tk()
window.title("Workplaces")
Label(window, text="Person").grid(row=0, column=0)
Label(window, text="Workplace").grid(row=0, column=1)
people = ["Bruce Wayne", "Clark Kent", "Peter Parker",
          "Rick Blaine", "Willie Wonka"]
places = ["Wayne Enterprises", "Daily Planet", "Daily Bugle",
          "Rick's American Cafe", "Chocolate Factory"]
placesSorted = list(places)
placesSorted.sort()
conOFlstPeople = StringVar()
lstPeople = Listbox(window, width=12, height=5, exportselection=0, listvariable=conOFlstPeople)
lstPeople.grid(row=1, column=0, padx=10)
conOFlstPeople.set(tuple(people))
conOFlstPlaces = StringVar()
lstPlaces = Listbox(window, width=18, height=5, exportselection=0, listvariable=conOFlstPlaces)
lstPlaces.grid(row=1, column=1, padx=10)
conOFlstPlaces.set(tuple(placesSorted))
btnDetermine = Button(window, text="Determine if Match is Correct", command=checkAnswer)
btnDetermine.grid(row=2, column=0, columnspan=2, pady=5)
Label(window, text="Answer:").grid(row=3, column=0, sticky=E)
conOFentAnswer = StringVar()
entAnswer = Entry(window, width=10, textvariable=conOFentAnswer, state="readonly")
entAnswer.grid(row=3, column=1, padx=10, pady=(0,5), sticky=W)
window.mainloop()

##from tkinter import *
##
##class Workplaces:
##
##    def __init__(self):
##        window = Tk()
##        window.title("Workplaces")
##        Label(window, text="Person").grid(row=0, column=0)
##        Label(window, text="Workplace").grid(row=0, column=1)
##        self._people = ["Bruce Wayne", "Clark Kent", "Peter Parker",
##                        "Rick Blaine", "Willie Wonka"]
##        self._places = ["Wayne Enterprises", "Daily Planet", "Daily Bugle",
##                        "Rick's American Cafe", "Chocolate Factory"]
##        self._placesSorted = list(self._places)
##        self._placesSorted.sort()
##        self._conOFlstPeople = StringVar()
##        self._lstPeople = Listbox(window, width=12, height=5, exportselection=0,
##                                  listvariable=self._conOFlstPeople)
##        self._lstPeople.grid(row=1, column=0, padx=10)
##        self._conOFlstPeople.set(tuple(self._people))
##        
##        self._conOFlstPlaces = StringVar()
##        self._lstPlaces = Listbox(window, width=18, height=5, exportselection=0,
##                                  listvariable=self._conOFlstPlaces)
##        self._lstPlaces.grid(row=1, column=1, padx=10)
##        self._conOFlstPlaces.set(tuple(self._placesSorted))
##        self._btnDetermine = Button(window, text="Determine if Match is Correct",
##                           command=self.checkAnswer)
##        self._btnDetermine.grid(row=2, column=0, columnspan=2, pady=5)
##        Label(window, text="Answer:").grid(row=3, column=0, sticky=E)
##        self._conOFentAnswer = StringVar()
##        self._entAnswer = Entry(window, width=10,
##                                textvariable=self._conOFentAnswer,
##                                state="readonly")
##        self._entAnswer.grid(row=3, column=1, padx=10, pady=(0,5), sticky=W)
##        window.mainloop()
##        
##    def checkAnswer(self):
##        m = self._people.index(self._lstPeople.get(self._lstPeople.curselection()))
##        n = self._places.index(self._lstPlaces.get(self._lstPlaces.curselection()))
##        if m == n:
##            self._conOFentAnswer.set("CORRECT")
##        else:                               
##            self._conOFentAnswer.set("INCORRECT")                   
##
##Workplaces()
