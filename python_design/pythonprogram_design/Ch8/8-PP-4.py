from tkinter import *

def stripOutLeadingZeros(front):
    if front == "000":
        front = "0"
    elif front[:2] == "00":
        front = front[2]
    elif front[0] == "0":
        front = front[1:]
    return front    

def verbalize():
    L = ["", " thousand", " million", " billion", " trillion",
         " quadrillion", " quintillion", " sextillion", " septillion"]
    N = []
    number = conOFentNumber.get()
    numberOfCommas = number.count(',')
    L = L[:numberOfCommas + 1]
    for i in range(numberOfCommas + 1, 0, -1): 
        loc = number.find(',')
        if loc == -1:
            number = stripOutLeadingZeros(number)
            N.append(number)
        else:
            front = number[:loc]
            front = stripOutLeadingZeros(front)
            N.append(front + L[-1])
        conOflstBox.set(tuple(N))
        number = number[loc + 1:]
        del L[-1]
 
window = Tk()
window.title("Verbalize")
instructions = "Enter a number having at most\n27 digits (include commas)."
lbl = Label(window, text=instructions)
lbl.grid(row=0, column=0, columnspan=2)
conOFentNumber = StringVar()
entNumber = Entry(window, width=30, textvariable=conOFentNumber)
entNumber.grid(row=1, column=0, columnspan=2,padx=5, pady=10)
conOflstBox = StringVar()
lstBox = Listbox(window, width=12, height=9, listvariable=conOflstBox)
lstBox.grid(row=2, column=1)
b = Button(window, text="Verbalize \nNumber", command=verbalize)
b.grid(row=2, column=0, sticky=N)
window.mainloop()
