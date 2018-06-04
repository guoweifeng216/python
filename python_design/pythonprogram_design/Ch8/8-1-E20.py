from tkinter import *       
        
def changeText():
    if btnTest["text"] == "HELLO":
        btnTest["text"] = "GOODBYE"
    else:
        btnTest["text"] = "HELLO"
   
window = Tk()
window.title("Salutation")
btnTest = Button(window, text="HELLO", fg="blue", width=12, command=changeText)
btnTest.grid(padx=100, pady=15)
window.mainloop()
