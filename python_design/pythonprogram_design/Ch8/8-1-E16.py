from tkinter import *

window = Tk()
window.title("Continents")
setOfContinents = {line.split(',')[1] for line in open("UN.txt", 'r')}
listOfContinents = list(setOfContinents)
listOfContinents.sort()
conOFlstContinents = StringVar()
lstContinents = Listbox(window, height=len(setOfContinents), 
                        width=15, listvariable=conOFlstContinents)
lstContinents.grid(row=1, column=0, padx=75, pady=5)
conOFlstContinents.set(tuple(listOfContinents))
window.mainloop()
