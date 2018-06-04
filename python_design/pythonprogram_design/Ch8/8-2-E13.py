from tkinter import *
window = Tk()
window.title("Calculate")
Label(window, text="First \nnumber:").grid(row=0, column=0)
Label(window, text="Second \nnumber: ").grid(row=0, column=2)
entFirst = Entry(window, width=5)
entFirst.grid(row=1, column=0)
entSecond = Entry(window, width=5)
entSecond.grid(row=1, column=2)
btnAdd = Button(window, text='+', width=3)
btnAdd.grid(row=0, column=1, padx=15)
btnSubtract = Button(window, text='-', width=3)
btnSubtract.grid(row=1, column=1, padx=15)
btnMultiply = Button(window, text='x', width=3)
btnMultiply.grid(row=2, column=1, padx=15, pady=5)
entResult = Entry(window, state="readonly", width=20)
entResult.grid(row=3, column=0, columnspan=3, padx=40, pady=5)
window.mainloop()



