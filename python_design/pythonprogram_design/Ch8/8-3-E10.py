from tkinter import *

def makeChange():
    amount = int(conOFentAmount.get())
    remainder = amount
    quarters = remainder // 25
    remainder %= 25
    dimes = remainder // 10
    remainder %= 10
    nickels = remainder // 5
    remainder %= 5
    cents = remainder
    conOFentQuarters.set(str(quarters))
    conOFentDimes.set(str(dimes))
    conOFentNickels.set(str(nickels))
    conOFentCents.set(str(cents))

window = Tk()
window.title("Change")
caption = "Amount: "
Label(window, text=caption).grid(row=0, column=1, sticky=E)
conOFentAmount = StringVar()
entAmount = Entry(window, width=2, textvariable=conOFentAmount)
entAmount.grid(row=0, column=2, sticky=W)
caption = "Determine Composition of Change"
btnDetermine = Button(window, text=caption, command=makeChange)
btnDetermine.grid(row=1, column=0, columnspan=4, padx=20, pady=5)
Label(window, text="Quarters: ").grid(row=2, column=0, sticky=E)
Label(window, text="Nickels: ").grid(row=3, column=0, sticky=E)
Label(window, text="Dimes: ").grid(row=2, column=2, sticky=E)
Label(window, text="Cents: ").grid(row=3, column=2, sticky=E)
conOFentQuarters = StringVar()
entQuarters = Entry(window, width=2, state="readonly",
                   textvariable=conOFentQuarters)
entQuarters.grid(row=2, column=1, sticky=W)
conOFentNickels = StringVar()
entNickels = Entry(window, width=2, state="readonly",
                   textvariable=conOFentNickels)
entNickels.grid(row=3, column=1, sticky=W)
conOFentDimes = StringVar()
entDimes = Entry(window, width=2, state="readonly",
                   textvariable=conOFentDimes)
entDimes.grid(row=2, column=3, sticky=W)
conOFentCents = StringVar()
entCents = Entry(window, width=2, state="readonly",
                         textvariable=conOFentCents)
entCents.grid(row=3, column=3, sticky=W)
window.mainloop()

##from tkinter import *
##
##class Change:
##
##    def __init__(self):
##        window = Tk()
##        window.title("Change")
##        caption = "Amount: "
##        Label(window, text=caption).grid(row=0, column=1,
##                                          sticky=E)
##        self._conOFentAmount = StringVar()
##        self.entAmount = Entry(window, width=2,
##                               textvariable=self._conOFentAmount)
##        self.entAmount.grid(row=0, column=2, sticky=W)
##        caption = "Determine Composition of Change"
##        btnDetermine = Button(window, text=caption, command=self.makeChange)
##        btnDetermine.grid(row=1, column=0, columnspan=4, padx=20, pady=5)
##        Label(window, text="Quarters: ").grid(row=2, column=0, sticky=E)
##        Label(window, text="Nickels: ").grid(row=3, column=0, sticky=E)
##        Label(window, text="Dimes: ").grid(row=2, column=2, sticky=E)
##        Label(window, text="Cents: ").grid(row=3, column=2, sticky=E)
##        self._conOFentQuarters = StringVar()
##        self.entQuarters = Entry(window, width=2, state="readonly",
##                            textvariable=self._conOFentQuarters)
##        self.entQuarters.grid(row=2, column=1, sticky=W)
##        self._conOFentNickels = StringVar()
##        self.entNickels = Entry(window, width=2, state="readonly",
##                            textvariable=self._conOFentNickels)
##        self.entNickels.grid(row=3, column=1, sticky=W)
##        self._conOFentDimes = StringVar()
##        self.entDimes = Entry(window, width=2, state="readonly",
##                            textvariable=self._conOFentDimes)
##        self.entDimes.grid(row=2, column=3, sticky=W)
##        self._conOFentCents = StringVar()
##        self.entCents = Entry(window, width=2, state="readonly",
##                            textvariable=self._conOFentCents)
##        self.entCents.grid(row=3, column=3, sticky=W)
##        window.mainloop()
##        
##    def makeChange(self):
##        amount = int(self._conOFentAmount.get())
##        remainder = amount
##        quarters = remainder // 25
##        remainder %= 25
##        dimes = remainder // 10
##        remainder %= 10
##        nickels = remainder // 5
##        remainder %= 5
##        cents = remainder
##        self._conOFentQuarters.set(str(quarters))
##        self._conOFentDimes.set(str(dimes))
##        self._conOFentNickels.set(str(nickels))
##        self._conOFentCents.set(str(cents))
##
##Change()
