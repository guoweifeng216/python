from tkinter import *

window = Tk()
window.title("U.S. Senate")
instruction = "Click on a state."
Label(window, text=instruction).grid(row=0, column=0, columnspan=3, pady=5)
Label(window, text="STATE", width=14).grid(row=1, column=0)
Label(window, text="SENATORS").grid(row=1, column=2)
yscroll = Scrollbar(window, orient=VERTICAL)
yscroll.grid(row=2, column=1, pady=5, sticky=NS)
lstStates = Listbox(window, width=14, height=7, yscrollcommand=yscroll.set)
lstStates.grid(row=2, column=0, pady=5, sticky=E)
lstSenators = Listbox(window, width=18, height=2)
lstSenators.grid(row=2, column=2, padx=8, pady=5, sticky=N)
yscroll["command"] = lstStates.yview
window.mainloop()

