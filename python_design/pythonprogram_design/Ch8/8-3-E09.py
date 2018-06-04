from tkinter import *

def add():
    num1 = eval(conOFentFirst.get())
    num2 = eval(conOFentSecond.get())
    sum = num1 + num2
    conOFentResult.set("Sum: " + str(sum))

def subtract():
    num1 = eval(conOFentFirst.get())
    num2 = eval(conOFentSecond.get())
    difference = num1 - num2
    conOFentResult.set("Difference: " + str(difference))

def multiply():
    num1 = eval(conOFentFirst.get())
    num2 = eval(conOFentSecond.get())
    product = num1 * num2
    conOFentResult.set("Product: " + str(product))

window = Tk()
window.title("Calculate")
Label(window, text="First \nnumber:").grid(row=0, column=0)
Label(window, text="Second \nnumber: ").grid(row=0, column=2)
conOFentFirst = StringVar()
entFirst = Entry(window, width=5, textvariable=conOFentFirst)
entFirst.grid(row=1, column=0)
conOFentSecond = StringVar()
entSecond = Entry(window, width=5, textvariable=conOFentSecond)
entSecond.grid(row=1, column=2)
btnAdd = Button(window, text='+', width=3, command=add)
btnAdd.grid(row=0, column=1, padx=15)
btnSubtract = Button(window, text='-', width=3, command=subtract)
btnSubtract.grid(row=1, column=1, padx=15)
btnMultiply = Button(window, text='x', width=3, command=multiply)
btnMultiply.grid(row=2, column=1, padx=15, pady=5)
conOFentResult = StringVar()
entResult = Entry(window, state="readonly", width=20,
                  textvariable=conOFentResult)
entResult.grid(row=3, column=0, columnspan=3, padx=40, pady=5)
window.mainloop()


##from tkinter import *
##
##class Calculate:
##
##    def __init__(self):
##        window = Tk()
##        window.title("Calculate")
##        Label(window, text="First \nnumber:").grid(row=0, column=0)
##        Label(window, text="Second \nnumber: ").grid(row=0, column=2)
##        self._conOFentFirst = StringVar()
##        self.entFirst = Entry(window, width=5, textvariable=self._conOFentFirst)
##        self.entFirst.grid(row=1, column=0)
##        self._conOFentSecond = StringVar()
##        self.entSecond = Entry(window, width=5, textvariable=self._conOFentSecond)
##        self.entSecond.grid(row=1, column=2)
##        btnAdd = Button(window, text='+', width=3, command=self.add)
##        btnAdd.grid(row=0, column=1, padx=15)
##        btnSubtract = Button(window, text='-', width=3, command=self.subtract)
##        btnSubtract.grid(row=1, column=1, padx=15)
##        btnMultiply = Button(window, text='x', width=3, command=self.multiply)
##        btnMultiply.grid(row=2, column=1, padx=15, pady=5)
##        self.conOFentResult = StringVar()
##        self.entResult = Entry(window, state="readonly", width=20,
##                          textvariable=self.conOFentResult)
##        self.entResult.grid(row=3, column=0, columnspan=3, padx=40, pady=5)
##        window.mainloop()
##
##    def add(self):
##        num1 = eval(self._conOFentFirst.get())
##        num2 = eval(self._conOFentSecond.get())
##        sum = num1 + num2
##        self.conOFentResult.set("Sum: " + str(sum))
##
##    def subtract(self):
##        num1 = eval(self._conOFentFirst.get())
##        num2 = eval(self._conOFentSecond.get())
##        difference = num1 - num2
##        self.conOFentResult.set("Difference: " + str(difference))
##    
##    def multiply(self):
##        num1 = eval(self._conOFentFirst.get())
##        num2 = eval(self._conOFentSecond.get())
##        product = num1 * num2
##        self.conOFentResult.set("Product: " + str(product))
