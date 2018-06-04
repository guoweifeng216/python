from tkinter import *

def changeColorandText(e):
    if lblChange["fg"] == "blue":
        lblChange["fg"] = "black"
        lblChange["text"] = "Change Color of Text to Blue"
    else:
        lblChange["fg"] = "blue"
        lblChange["text"] = "Change Color of Text to Black"        
  
window = Tk()
window.title("Change Colors")
lblChange = Label(window, text="Change Color of Text to Black", fg="blue")
lblChange.grid(padx=50, pady=15)
lblChange.bind("<Button-1>", changeColorandText) 
window.mainloop()
 

