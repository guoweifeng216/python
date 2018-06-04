from tkinter import *
window = Tk()
window.title("Graduation Honors")
caption = "GPA (2 through 4):"
Label(window, text=caption).grid(row=0, column=0, pady=5, sticky=E)
entGPA = Entry(window, width=4)
entGPA.grid(row=0, column=1, padx=5, sticky=W)
btnDisplay = Button(text="Determine Honors")
btnDisplay.grid(row=1, column=0, columnspan=2, padx=100)
entHonors = Entry(window, state="readonly", width=30)
entHonors.grid(row=2, column=0, columnspan=2, padx=5, pady=5)
window.mainloop()


