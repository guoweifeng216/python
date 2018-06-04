from tkinter import *

window = Tk()
window.title("Oceans")
Label(window, text="", width = 10).grid(row=0, column=0)
Label(window, text="", width = 10).grid(row=0, column=3)
yscroll = Scrollbar(window, orient=VERTICAL)
yscroll.grid(row=0, column=2, rowspan=9, pady=5, sticky=NS)
oceanList = ["Atlantic", "Pacific", "Indian", "Arctic","Antarctic"]
conOFlstOcean = StringVar()
lstOcean = Listbox(window, width=8, height=4, listvariable=conOFlstOcean,
                  yscrollcommand=yscroll.set)
lstOcean.grid(row=0, column=1, rowspan=4, pady=5, sticky=E)
conOFlstOcean.set(tuple(oceanList))
yscroll["command"] = lstOcean.yview
window.mainloop()
