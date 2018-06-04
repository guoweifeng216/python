from tkinter import *

window = Tk()
window.title("Investment")
Label(window, text="Invest $10,000").grid(row=0, column=1, pady=5)
Label(window, text="Interest\nrate:").grid(row=1, column=0, padx=10, pady=5)
Label(window, text="Compound\nperiods:").grid(row=1, column=1,
                                                 padx=10, pady=5)
btnCalculate = Button(window, text="Calculate\nAmount\nAfter 5\nYears")
btnCalculate.grid(row=3, column=2, padx=5, sticky=N)
lstRates = Listbox(window, height=5, width=4)
lstRates.grid(row=3, column=0)
lstPeriods = Listbox(window, height=5, width=12)
lstPeriods.grid(row=3, column=1)
Label(window, text="Amount after 5 years:").grid(row=4, column=0,
                                   pady=5, columnspan=2, sticky=E)
entAmount = Entry(window,  width=9, state="readonly")
entAmount.grid(row=4, column=2, padx = 3, pady=5, sticky=W)
window.mainloop()

