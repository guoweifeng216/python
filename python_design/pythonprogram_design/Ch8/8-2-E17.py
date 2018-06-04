from tkinter import *

window = Tk()
window.title("Verbalize")
instruction = "Enter a number having at most\n" + \
    "27 digits (include commas)."
Label(window, text=instruction).grid(row=0, column=0,
                                columnspan=2, padx=15)
entNum = Entry(window, width=27)
entNum.grid(row=1, column=0, columnspan=2, pady=5)
btnVerbalize = Button(window, text="Verbalize\nNumber")
btnVerbalize.grid(row=2, column=0, sticky=N)
lstEnglish = Listbox(window, height=9, width=14)
lstEnglish.grid(row=2, column=1)
window.mainloop()

