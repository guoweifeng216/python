from tkinter import *

def fullName():
    conOFentFullName.set(conOFentFirstName.get() + \
                         " " + conOFentLastName.get())
window = Tk()
window.title("Full Name")
Label(window, text="Last name:").grid(row=0, column=0, sticky=E)
conOFentLastName = StringVar()
entLastName = Entry(window, width=15, textvariable=conOFentLastName)
entLastName.grid(row=0, column=1, padx=5, sticky=W)

Label(window, text="First name:").grid(row=1, column=0, sticky=E)
conOFentFirstName = StringVar()
entFirstName = Entry(window, width=15, textvariable=conOFentFirstName)
entFirstName.grid(row=1, column=1, padx=5, sticky=W)
        
btnDisplay = Button(text="Display Full Name", command=fullName)
btnDisplay.grid(row=2, column=0, columnspan=2, pady = 10)
Label(window, text="Full name:").grid(row=3, column=0, sticky=E)
conOFentFullName = StringVar()
entFullName = Entry(window, state="readonly", textvariable=conOFentFullName)
entFullName.grid(row=3, column=1, padx=5)
window.mainloop()

##from tkinter import *
##
##class FullName:
##
##    def __init__(self):
##        window = Tk()
##        window.title("Full Name")
##        Label(window, text="Last name:").grid(row=0, column=0, sticky=E)
##        self.conOFentLastName = StringVar()
##        entLastName = Entry(window, width=15,
##                            textvariable=self.conOFentLastName)
##        entLastName.grid(row=0, column=1, padx=5, sticky=W)
##
##        Label(window, text="First name:").grid(row=1, column=0, sticky=E)
##        self.conOFentFirstName = StringVar()
##        entFirstName = Entry(window, width=15,
##                             textvariable=self.conOFentFirstName)
##        entFirstName.grid(row=1, column=1, padx=5, sticky=W)
##        
##        btnDisplay = Button(text="Display Full Name", command=self.fullName)
##        btnDisplay.grid(row=2, column=0, columnspan=2, pady = 10)
##        Label(window, text="Full name:").grid(row=3, column=0, sticky=E)
##        self.conOFentFullName = StringVar()
##        self.entFullName = Entry(window, state="readonly",
##                                 textvariable=self.conOFentFullName)
##        self.entFullName.grid(row=3, column=1, padx=5)
##        window.mainloop()
##        
##    def fullName(self):
##        self.conOFentFullName.set(self.conOFentFirstName.get() + \
##                                 " " + self.conOFentLastName.get())
##FullName()


