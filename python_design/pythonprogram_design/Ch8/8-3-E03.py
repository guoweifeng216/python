from tkinter import *

def calculateCost():
    costs = [float(conOFentFirst.get()),
             float(conOFentSecond.get()),float(conOFentThird.get())]               
    totalCost = sum(costs) - min(costs)
    conOFentTotalCost.set("${0:,.2f}".format(totalCost))         
                                                 
window = Tk()
window.title("3rd Free")
Label(window, text="Cost of first item:").grid(row=0, column=0,
                                            padx=(5,3), pady=5, sticky=E)
Label(window, text="Cost of second item:").grid(row=1, column=0,
                                            padx=(5,3), pady=5, sticky=E)
Label(window, text="Cost of third item:").grid(row=2, column=0,
                                            padx=(5,3), pady=5, sticky=E)
conOFentFirst = StringVar()
entFirst = Entry(window, width=10, textvariable=conOFentFirst)
entFirst.grid(row=0, column=1, pady=10, sticky=W)
conOFentSecond = StringVar()
entSecond = Entry(window, width=10, textvariable=conOFentSecond)
entSecond.grid(row=1, column=1, pady=10, sticky=W)
conOFentThird = StringVar()
entThird = Entry(window, width=10, textvariable=conOFentThird)
entThird.grid(row=2, column=1, pady=10, sticky=W)

btnCalculate = Button(window, text="Calculate Cost of Items",
                      command=calculateCost)
btnCalculate.grid(row=3, column=0, columnspan=2, pady=(0,8))
Label(window, text="Cost of three items:").grid(row=4, column=0, sticky=E)
conOFentTotalCost = StringVar()
entTotalCost = Entry(window, width=10, textvariable=conOFentTotalCost,
                     state="readonly")
entTotalCost.grid(row=4, column=1, padx=5, pady=(0,5), sticky=W)
window.mainloop()

from tkinter import *

class Cost:
    def __init__(self):
        window = Tk()
        window.title("3rd Free")
        Label(window, text="Cost of first item:").grid(row=0, column=0,
                                            padx=(5,3), pady=5, sticky=E)
        Label(window, text="Cost of second item:").grid(row=1, column=0,
                                            padx=(5,3), pady=5, sticky=E)
        Label(window, text="Cost of third item:").grid(row=2, column=0,
                                            padx=(5,3), pady=5, sticky=E)
        self._conOFentFirst = StringVar()
        entFirst = Entry(window, width=10, textvariable=self._conOFentFirst)
        entFirst.grid(row=0, column=1, pady=10, sticky=W)
        self._conOFentSecond = StringVar()
        entSecond = Entry(window, width=10, textvariable=self._conOFentSecond)
        entSecond.grid(row=1, column=1, pady=10, sticky=W)
        self._conOFentThird = StringVar()
        entThird = Entry(window, width=10, textvariable=self._conOFentThird)
        entThird.grid(row=2, column=1, pady=10, sticky=W)
        btnCalculate = Button(window, text="Calculate Cost of Items",
                              command=self.calculateCost)
        btnCalculate.grid(row=3, column=0, columnspan=2, pady=(0,8))
        Label(window, text="Cost of three items:").grid(row=4, column=0, sticky=E)
        self._conOFentTotalCost = StringVar()
        entTotalCost = Entry(window, width=10, textvariable=self._conOFentTotalCost,
                             state="readonly")
        entTotalCost.grid(row=4, column=1, padx=5, pady=(0,5), sticky=W)
        window.mainloop()
        
    def calculateCost(self):
        costs = [float(self._conOFentFirst.get()),
                 float(self._conOFentSecond.get()),float(self._conOFentThird.get())]               
        totalCost = sum(costs) - min(costs)
        self._conOFentTotalCost.set("${0:,.2f}".format(totalCost))

Cost()

