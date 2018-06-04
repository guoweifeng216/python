from tkinter import *
      
window = Tk()     
window.title("Inventor (Label)")
conOFlblInventor = StringVar()   # contents of the Entry widget
lblInventor = Label(window, fg="white", bg="blue",
                    textvariable=conOFlblInventor)
lblInventor.grid(padx=95, pady=15)
conOFlblInventor.set("CHARLES BABBAGE")
window.mainloop()
