window.mainloop()from tkinter import *

window = Tk()
window.title("Presidents")
infile = open("USpres.txt", 'r')
listOfPresidents = [line.rstrip() for line in infile]
infile.close()
conOFlstPres = StringVar()
lstPres = Listbox(window, height=5, width=18, listvariable=conOFlstPres)
lstPres.grid(padx=75, pady=5)
conOFlstPres.set(tuple(listOfPresidents))
        

##from tkinter import *
##
##class Presidents:
##
##    def __init__(self):
##        window = Tk()
##        window.title("Presidents")
##        
##        listOfPresidents = [line for line in open("USpres.txt", 'r')]
##        conOFlstPres = StringVar()
##        lstPres = Listbox(window, height=5, width=18, listvariable=conOFlstPres)
##        lstPres.grid(padx=75, pady=5)
##        conOFlstPres.set(tuple(listOfPresidents))
##        window.mainloop()

##Presidents()
