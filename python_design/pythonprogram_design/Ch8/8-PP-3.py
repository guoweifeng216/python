from tkinter import *

def calculate():
    ave = (eval(conOFentSalary1.get()) + eval(conOFentSalary2.get()) +
           eval(conOFentSalary3.get())) / 3
    yrs = eval(conOFentYears.get())
    months = eval(conOFentMonths.get())
    yrs += months / 12
    percentage = 36.25 + (2 * (yrs - 20))
    if percentage > 80:
        percentage = 80
    pension = ave * (percentage / 100)
    conOFentPension.set("${0:,.2f}".format(pension))

window = Tk()
window.title("Pension")
Label(window, text="Three\nHighest\nAnnual\nSalaries").grid(row=0,
                                            column=0, rowspan=3, padx=5)
conOFentSalary1 = StringVar()
entSalary1 = Entry(window, width=10, textvariable=conOFentSalary1)
entSalary1.grid(row=0, column=1)
conOFentSalary2 = StringVar()
entSalary2 = Entry(window, width=10, textvariable=conOFentSalary2)
entSalary2.grid(row=1, column=1)
conOFentSalary3 = StringVar()
entSalary3 = Entry(window, width=10, textvariable=conOFentSalary3)
entSalary3.grid(row=2, column=1)
Label(window, text="Service").grid(row=0, column=2, sticky=E)
Label(window, text="Years: ").grid(row=1, column=2, sticky=E)
conOFentYears = StringVar()
entYears = Entry(window, width=2, textvariable=conOFentYears)
entYears.grid(row=1, column=3, padx=(0, 10), sticky=W)        
Label(window, text="Months: ").grid(row=2, column=2, sticky=E)
conOFentMonths = StringVar()
entMonths = Entry(window, width=2, textvariable=conOFentMonths)
entMonths.grid(row=2, column=3, sticky=W)  
Label(window, text="Age: ").grid(row=3, column=0, sticky=E)
conOFentAge = StringVar()
entAge = Entry(window, width=2, textvariable=conOFentAge)
entAge.grid(row=3, column=1, sticky=W)
btnCalculate = Button(window, text="Calculate Pension", command=calculate)
btnCalculate.grid(row=4, column=1, columnspan=2)
Label(window, text="Pension: ").grid(row=5, column=1, sticky=E)
conOFentPension = StringVar()
entPension = Entry(window, width=13, textvariable=conOFentPension, state="readonly")
entPension.grid(row=5, column=2, pady=10)
window.mainloop()


