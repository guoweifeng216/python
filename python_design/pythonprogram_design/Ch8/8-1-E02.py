from tkinter import *
      
window = Tk()     
window.title("Readonly Entry")
conOFentQuote = StringVar()   # contents of the Entry widget
entQuote = Entry(window, fg="blue", state="readonly",
                 width=2, textvariable=conOFentQuote)
entQuote.grid(padx=150, pady=15)
conOFentQuote.set("HI")
window.mainloop()
