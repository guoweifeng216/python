from tkinter import *

window = Tk()
window.title("Change")
caption = "Amount: "
Label(window, text=caption).grid(row=0, column=1, sticky=E)
entAmount = Entry(window, width=2)
entAmount.grid(row=0, column=2, sticky=W)
caption = "Determine Composition of Change"
btnDetermine = Button(window, text=caption)
btnDetermine.grid(row=1, column=0, columnspan=4, padx=20, pady=5)
Label(window, text="Quarters: ").grid(row=2, column=0, sticky=E)
Label(window, text="Nickels: ").grid(row=3, column=0, sticky=E)
Label(window, text="Dimes: ").grid(row=2, column=2, sticky=E)
Label(window, text="Cents: ").grid(row=3, column=2, sticky=E)
entQuarters = Entry(window, width=2, state="readonly")
entQuarters.grid(row=2, column=1, sticky=W)
entNickels = Entry(window, width=2, state="readonly")
entNickels.grid(row=3, column=1, sticky=W)
entDimes = Entry(window, width=2, state="readonly")
entDimes.grid(row=2, column=3, sticky=W)
entCents = Entry(window, width=2, state="readonly")
entCents.grid(row=3, column=3, sticky=W)
window.mainloop()        
