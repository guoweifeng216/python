from tkinter import *

def honors():
    gpa = float(conOFentGPA.get())
    if gpa >= 3.9:
        honor = " summa cum laude."
    elif gpa >= 3.6:
        honor = " magna cum laude."
    elif gpa >= 3.3:
        honor = " cum laude."
    else:
        honor = "."
    # Display conclusion.
    conOFentHonors.set("You graduated" + honor)       
       
window = Tk()
window.title("Graduation Honors")
caption = "GPA (2 through 4):"
Label(window, text=caption).grid(row=0, column=0, pady=5, sticky=E)
conOFentGPA = StringVar()
entGPA = Entry(window, width=4, textvariable=conOFentGPA)
entGPA.grid(row=0, column=1, padx=5, sticky=W)

btnDisplay = Button(text="Determine Honors", command=honors)
btnDisplay.grid(row=1, column=0, columnspan=2, padx=100)
conOFentHonors = StringVar()
entHonors = Entry(window, state="readonly", width=30,
                         textvariable=conOFentHonors)
entHonors.grid(row=2, column=0, columnspan=2, padx=5, pady=5)
window.mainloop()

##from tkinter import *
##
##class GPA:
##
##    def __init__(self):
##        window = Tk()
##        window.title("Graduation Honors")
##        caption = "GPA (2 through 4):"
##        Label(window, text=caption).grid(row=0, column=0, pady=5, sticky=E)
##        self.conOFentGPA = StringVar()
##        entGPA = Entry(window, width=4, textvariable=self.conOFentGPA)
##        entGPA.grid(row=0, column=1, padx=5, sticky=W)
##        btnDisplay = Button(text="Determine Honors", command=self.honors)
##        btnDisplay.grid(row=1, column=0, columnspan=2, padx=100)
##        self.conOFentHonors = StringVar()
##        self.entHonors = Entry(window, state="readonly", width=30,
##                                 textvariable=self.conOFentHonors)
##        self.entHonors.grid(row=2, column=0, columnspan=2, padx=5, pady=5)
 #        window.mainloop()
##        
##    def honors(self):
##        gpa = float(self.conOFentGPA.get())
##        if gpa >= 3.9:
##            honor = " summa cum laude."
##        elif gpa >= 3.6:
##            honor = " magna cum laude."
##        elif gpa >= 3.3:
##            honor = " cum laude."
##        else:
##            honor = "."
##        # Display conclusion.
##        self.conOFentHonors.set("You graduated" + honor)
##       
##GPA()


