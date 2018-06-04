from tkinter import *

def calculate():
    rate = lstRates.get(lstRates.curselection())
    if rate == "2%":
        intRate = .02
    elif rate == "2.5%":
        intRate = .025
    elif rate == "3%":
        intRate = .03
    elif rate == "3.5%":
        intRate = .035
    elif rate == "4%":
        intRate = .04
    periods = lstPeriods.get(lstPeriods.curselection())
    if periods == "annually":
        n = 1
    elif periods == "semi-annually":
        n = 2
    elif periods == "quarterly":
        n = 4
    elif periods == "monthly":
        n = 12
    elif periods == "weekly":
        n = 52
    amount = 10000 * (1 +  intRate/n) ** (5*n)
    conOFentAmount.set("${0:,.2f}".format(amount))

window = Tk()
window.title("Investment")
Label(window, text="Invest $10,000").grid(row=0, column=1, pady=5)
Label(window, text="Interest\nrate:").grid(row=1, column=0, padx=10, pady=5)
Label(window, text="Compound\nperiods:").grid(row=1, column=1,
                                                 padx=10, pady=5)
btnCalculate = Button(window, text="Calculate\nAmount\nAfter 5\nYears",
                      command=calculate)
btnCalculate.grid(row=3, column=2, padx=5, sticky=N)
conOFlstRates = StringVar()
lstRates = Listbox(window, height=5, width=4, exportselection=0,
                   listvariable=conOFlstRates)
lstRates.grid(row=3, column=0)
conOFlstPeriods = StringVar()
lstPeriods = Listbox(window, height=5, width=12, exportselection=0,
                     listvariable=conOFlstPeriods)
lstPeriods.grid(row=3, column=1)
Label(window, text="Amount after 5 years:").grid(row=4, column=0,
                                                 pady=5, columnspan=2, sticky=E)
conOFentAmount = StringVar()
entAmount = Entry(window, textvariable=conOFentAmount,
                  width=9, state="readonly")
entAmount.grid(row=4, column=2, padx = 3, pady=5, sticky=W)
conOFlstRates.set(("2%", "2.5%","3%","3.5%","4%"))
conOFlstPeriods.set(("annually", "semi-annually",
                     "quarterly", "monthly", "weekly"))
window.mainloop()






