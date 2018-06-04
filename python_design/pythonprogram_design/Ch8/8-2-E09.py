from tkinter import *

window = Tk()
window.title("Full Name")
Label(window, text="Last name:").grid(row=0, column=0, sticky=E)
entLastName = Entry(window, width=15)
entLastName.grid(row=0, column=1, padx=5, sticky=W)
Label(window, text="First name:").grid(row=1, column=0, sticky=E)
entFirstName = Entry(window, width=15)
entFirstName.grid(row=1, column=1, padx=5, sticky=W)
btnDisplay = Button(text="Display Full Name")
btnDisplay.grid(row=2, column=0, columnspan=2, pady = 10)
Label(window, text="Full name:").grid(row=3, column=0, sticky=E)
entFullName = Entry(window, state="readonly")
entFullName.grid(row=3, column=1, padx=5)
window.mainloop()


