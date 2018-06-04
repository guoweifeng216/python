from tkinter import *

window = Tk()
window.title("Major Subjects")
L = ["reading", "writing", "arithmetic", "coding"]
conOFlstSubjects = StringVar()
lstSubjects = Listbox(window, width=15, height=4, fg="blue",
                      listvariable=conOFlstSubjects)
lstSubjects.grid(padx=100, pady=15)    
conOFlstSubjects.set(tuple(L))
window.mainloop()




