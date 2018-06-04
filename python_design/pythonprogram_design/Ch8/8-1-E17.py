from tkinter import *

def changeColorandText():
    if btnChange["fg"] == "blue":
        btnChange["fg"] = "black"
        btnChange["text"] = "Change Color of Text to Blue"
    else:
        btnChange["fg"] = "blue"
        btnChange["text"] = "Change Color of Text to Black"        
       
window = Tk()
window.title("Change Colors")
btnChange = Button(window, text="Change Color of Text to Black",
                   command=changeColorandText, fg="blue")
btnChange.grid(padx=50, pady=15)
window.mainloop()
 

