from tkinter import *
      
window = Tk()     
window.title("Quotation")
conOFentQuote = StringVar()   # contents of the Entry widget
entQuote = Entry(window, fg="blue", textvariable=conOFentQuote)
entQuote.grid(padx=40, pady=15)
conOFentQuote.set("Less is More")
window.mainloop()
