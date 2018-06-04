from tkinter import *

window = Tk()
window.title("U.S. Senate")
Label(window, text="State:", width=5).grid(row=0, column=0, sticky=E)
state = StringVar()
entState = Entry(window, textvariable=state)
entState.grid(row=0, column=1, sticky=W)
btnDisplay = Button(text="Display Senators")
btnDisplay.grid(row=1, columnspan=2, pady = 10)
lstSenators = Listbox(window, height=2, width=21)
lstSenators.grid(row=2,column=0, columnspan=2, padx=44, pady=2)
window.mainloop()
