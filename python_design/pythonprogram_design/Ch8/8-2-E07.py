from tkinter import *

window = Tk()
window.title("Reindeer")
Label(window, text="", width = 10).grid(row=0, column=0)
Label(window, text="", width = 10).grid(row=0, column=3)
yscroll = Scrollbar(window, orient=VERTICAL)
yscroll.grid(row=0, column=2, rowspan=9, pady=5, sticky=NS)
deerList = ["Blitzen", "Comet", "Dancer", "Dasher","Donder",  
            "Prancer", "Vixen"]
conOFlstDeer = StringVar()
lstDeer = Listbox(window, width=8, height=5, listvariable=conOFlstDeer,
                  yscrollcommand=yscroll.set)
lstDeer.grid(row=0, column=1, rowspan=4, pady=5, sticky=E)
conOFlstDeer.set(tuple(deerList))
yscroll["command"] = lstDeer.yview     
window.mainloop()
