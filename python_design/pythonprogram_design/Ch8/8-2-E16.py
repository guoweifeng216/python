from tkinter import *

import pickle
window = Tk()
window.title("Great Lakes")
global lakesDict
lstLakes = Listbox(window, height=5, width=9)
lstLakes.grid(row=0, column=0, padx=5, pady=5, rowspan=5, sticky=NSEW)
lstLakes.bind("<<ListboxSelect>>")
Label(window, text="Area (sq. miles):").grid(row=2, column=1, sticky=E)
entArea = Entry(window, width=7, state="readonly")
entArea.grid(row=2, column=2, padx=5)
window.mainloop()
