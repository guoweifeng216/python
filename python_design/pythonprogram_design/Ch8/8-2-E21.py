from tkinter import *
import pickle
window = Tk()
window.title("Members of U.N.")
yscroll = Scrollbar(window, orient=VERTICAL)
yscroll.grid(row=0, column=1, rowspan=7, sticky=NS)
lstNations = Listbox(window, height=10, width=30, yscrollcommand=yscroll.set)
lstNations.grid(row=0, column=0, rowspan=7, sticky=NSEW)
yscroll["command"] = lstNations.yview
Label(window, text="Continent:").grid(row=0, column=3, padx=4, sticky=E)
Label(window, text="Population:").grid(row=1, column=3, padx=4, sticky=E)
Label(window, text="Area (sq. miles):").grid(row=2, column=3, padx=4, sticky=E)
entContinent = Entry(window, width=15, state="readonly")
entContinent.grid(row=0, column=4, sticky=W)
entPopulation = Entry(window, width=15, state="readonly")
entPopulation.grid(row=1, column=4,)
entArea = Entry(window, width=15, state="readonly")
entArea.grid(row=2, column=4)
window.mainloop()

