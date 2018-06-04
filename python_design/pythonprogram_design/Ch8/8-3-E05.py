from tkinter import *

def newSalary():
    begSalary = eval(conOFentBegSalary.get())
    salary = begSalary + (.1 * begSalary)
    salary = salary - (.1 * salary)
    conOFentNewSalary.set("${0:,.2f}".format(salary))
    begSalary = eval(conOFentBegSalary.get())
    change = (salary - begSalary) / begSalary
    conOFentChange.set("{0:,.2%}".format(change))

window = Tk()
window.title("Salary")
Label(window, text="Beginning salary:").grid(row=0, column=0, sticky=E)
conOFentBegSalary = StringVar()
entBegSalary = Entry(window, width=11,
                    textvariable=conOFentBegSalary)
entBegSalary.grid(row=0, column=1, padx=5, pady=5, sticky=W)

btnCalculate = Button(text="Calculate New Salary", command=newSalary)
btnCalculate.grid(row=2, column=0, columnspan=2, padx=50)
Label(window, text="New salary:").grid(row=3, column=0, sticky=E)
conOFentNewSalary = StringVar()
entNewSalary = Entry(window, width=11, state="readonly",
                          textvariable=conOFentNewSalary)
entNewSalary.grid(row=3, column=1, padx=5, pady=5, sticky=W)
Label(window, text="Change:").grid(row=4, column=0, sticky=E)
conOFentChange = StringVar()
entChange = Entry(window, width=11, state="readonly",
                         textvariable=conOFentChange)
entChange.grid(row=4, column=1, padx=5, pady=5, sticky=W)
window.mainloop()

def newSalary(self):
    begSalary = eval(conOFentBegSalary.get())
    salary = begSalary + (.1 * begSalary)
    salary = salary - (.1 * salary)
    conOFentNewSalary.set("${0:,.2f}".format(salary))
    begSalary = eval(conOFentBegSalary.get())
    change = (salary - begSalary) / begSalary
    conOFentChange.set("{0:,.2%}".format(change))


##from tkinter import *
##
##class Salary:
##
##    def __init__(self):
##        window = Tk()
##        window.title("Salary")
##        Label(window, text="Beginning salary:").grid(row=0, column=0, sticky=E)
##        self.conOFentBegSalary = StringVar()
##        entBegSalary = Entry(window, width=11,
##                            textvariable=self.conOFentBegSalary)
##        entBegSalary.grid(row=0, column=1, padx=5, pady=5, sticky=W)
##
##        btnCalculate = Button(text="Calculate New Salary", command=self.newSalary)
##        btnCalculate.grid(row=2, column=0, columnspan=2, padx=50)
##        Label(window, text="New salary:").grid(row=3, column=0, sticky=E)
##        self.conOFentNewSalary = StringVar()
##        self.entNewSalary = Entry(window, width=11, state="readonly",
##                                  textvariable=self.conOFentNewSalary)
##        self.entNewSalary.grid(row=3, column=1, padx=5, pady=5, sticky=W)
##        Label(window, text="Change:").grid(row=4, column=0, sticky=E)
##        self.conOFentChange = StringVar()
##        self.entChange = Entry(window, width=11, state="readonly",
##                                 textvariable=self.conOFentChange)
##        self.entChange.grid(row=4, column=1, padx=5, pady=5, sticky=W)
##        window.mainloop()
##        
##    def newSalary(self):
##        begSalary = eval(self.conOFentBegSalary.get())
##        salary = begSalary + (.1 * begSalary)
##        salary = salary - (.1 * salary)
##        self.conOFentNewSalary.set("${0:,.2f}".format(salary))
##        begSalary = eval(self.conOFentBegSalary.get())
##        change = (salary - begSalary) / begSalary
##        self.conOFentChange.set("{0:,.2%}".format(change))
##        
##Salary()
