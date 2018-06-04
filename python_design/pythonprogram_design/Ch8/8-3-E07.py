from tkinter import *

def calculate():
   p = eval(principal.get())
   r = eval(interestRate.get())
   n = eval(numberOfYears.get())
   payment = (p*(r/1200)/(1 - (1 + (r/1200)) ** (-12*n)))
   payment = "${0:,.2f}".format(payment)
   monthlyPayment.set(payment)

window = Tk()
window.title("Car Loan")
lblPrincipal = Label(window, text="Amount of loan:", )
lblPrincipal.grid(row=0, column=0, padx=5, pady=5, sticky=E)
lblInterestRate = Label(window, text="Interest rate (as %):" )
lblInterestRate.grid(row=1, column=0, padx=5, pady=5, sticky=E)
lblNumberOfYears = Label(window, text="Number of years:" )
lblNumberOfYears.grid(row=2, column=0, padx=5, pady=5, sticky=E)
lblMonthlyPayment = Label(window, text="Monthly payment:")
lblMonthlyPayment.grid(row=5, column=0, padx=5, pady=5, sticky=E)
principal = StringVar()
interestRate = StringVar()
numberOfYears = StringVar()
monthlyPayment = StringVar()
entPrincipal = Entry(window, width=10, textvariable=principal)
entPrincipal.grid(row=0, column=1, padx=5, pady=5, sticky=W)
entInterestRate = Entry(window, width=6 ,textvariable=interestRate)
entInterestRate.grid(row=1, column=1, padx=5, pady=5, sticky=W)
entNumberOfYears = Entry(window, width=2 ,textvariable=numberOfYears)
entNumberOfYears.grid(row=2, column=1, padx=5, pady=5, sticky=W)
entMonthlyPayment = Entry(window, width=10, state="readonly", textvariable=monthlyPayment)
entMonthlyPayment.grid(row=5, column=1, padx=5, pady=5, sticky=W)
btnCalculate = Button(window, text="Calculate Monthly Payment",
                      command=calculate)
btnCalculate.grid(row=3, column=0, columnspan=2, padx=5, pady=5 )
window.mainloop()

##from tkinter import *
##
##class CarLoan:
##    
##    def __init__(self):
##        window = Tk()
##        window.title("Car Loan")
##        lblPrincipal = Label(window, text="Amount of loan:", )
##        lblPrincipal.grid(row=0, column=0, padx=5, pady=5, sticky=E)
##        lblInterestRate = Label(window, text="Interest rate (as %):" )
##        lblInterestRate.grid(row=1, column=0, padx=5, pady=5, sticky=E)
##        lblNumberOfYears = Label(window, text="Number of years:" )
##        lblNumberOfYears.grid(row=2, column=0, padx=5, pady=5, sticky=E)
##        lblMonthlyPayment = Label(window, text="Monthly payment:")
##        lblMonthlyPayment.grid(row=5, column=0, padx=5, pady=5, sticky=E)
##        self.principal = StringVar()
##        self.interestRate = StringVar()
##        self.numberOfYears = StringVar()
##        self.monthlyPayment = StringVar()
##        entPrincipal = Entry(window, width=10, textvariable=self.principal)
##        entPrincipal.grid(row=0, column=1, padx=5, pady=5, sticky=W)
##        entInterestRate = Entry(window, width=6 ,textvariable=self.interestRate)
##        entInterestRate.grid(row=1, column=1, padx=5, pady=5, sticky=W)
##        entNumberOfYears = Entry(window, width=2 ,textvariable=self.numberOfYears)
##        entNumberOfYears.grid(row=2, column=1, padx=5, pady=5, sticky=W)
##        entMonthlyPayment = Entry(window, width=10, state="readonly", textvariable=self.monthlyPayment)
##        entMonthlyPayment.grid(row=5, column=1, padx=5, pady=5, sticky=W)
##        btnCalculate = Button(window, text="Calculate Monthly Payment",
##                              command=self.calculate)
##        btnCalculate.grid(row=3, column=0, columnspan=2, padx=5, pady=5)
##        window.mainloop()
##       
##    def calculate(self):
##        p = eval(self.principal.get())
##        r = eval(self.interestRate.get())
##        n = eval(self.numberOfYears.get())
##        payment = (p*(r/1200)/(1 - (1 + (r/1200)) ** (-12*n)))
##        payment = "${0:,.2f}".format(payment)
##        self.monthlyPayment.set(payment)
##        
##CarLoan()
