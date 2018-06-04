from tkinter import *

class Affiliations:

    def __init__(self):
        window = Tk()
        window.title("U.S. Senate")
        lblDemocrats = Label(window, text="Democrats:")
        lblRepublicans = Label(window, text="Republicans:")
        lblIndependents = Label(window, text="Independents:")
        self._conOFentDemocrats = StringVar()
        self._conOFentRepublicans = StringVar()
        self._conOFentIndependents = StringVar()
        entDemocrats = Entry(window, width=2, state="readonly", 
                             textvariable=self._conOFentDemocrats)
        entRepublicans = Entry(window, width=2, state="readonly",
                               textvariable=self._conOFentRepublicans)
        entIndependents = Entry(window, width=2, state="readonly",
                                textvariable=self._conOFentIndependents)
        lblDemocrats.grid(row=1, column=1, padx=5,pady=3,sticky=E)
        lblRepublicans.grid(row=2, column=1, padx=5,pady=3,sticky=E)                   
        lblIndependents.grid(row=3, column=1, padx=5,pady=3,sticky=E)
        entDemocrats.grid(row=1, column=2, pady=3, padx=5, sticky=W)
        entRepublicans.grid(row=2, column=2, padx=5,pady=3,sticky=W)                   
        entIndependents.grid(row=3, column=2, padx=5,pady=3,sticky=W)
        btnDisplay = Button(text="Count Party Affiliations",
                            command=self.count)
        btnDisplay.grid(row=0, columnspan=4, padx=50, pady=10)
        window.mainloop()
        
    def count(self):
        D = 0
        R = 0
        I = 0
        for line in open("Senate114.txt", 'r'):
            lst = line.split(',')
            if lst[2] == "D\n":
                D += 1
            elif lst[2] == "R\n":
                R += 1
            else:
                I += 1
        self._conOFentDemocrats.set(str(D))
        self._conOFentRepublicans.set(str(R))                
        self._conOFentIndependents.set(str(I))
                              
Affiliations()
                           
