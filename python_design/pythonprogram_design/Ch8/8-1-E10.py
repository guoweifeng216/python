from tkinter import *

window = Tk()
window.title("Presidents")
infile = open("USpres.txt", 'r')
listOfPresidents = [line for line in infile]
infile.close()
listOfPresidents.sort(key=lambda x: x.split(" ")[-1])
conOFlstPres = StringVar()
lstPres = Listbox(window, height=5, width=18,
listvariable=conOFlstPres)
lstPres.grid(padx=75, pady=5)
conOFlstPres.set(tuple(listOfPresidents))
window.mainloop()
