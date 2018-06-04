from tkinter import *
import random

def drawing():
    conOFentWhiteBalls.set("")
    nums = [x for x in range(1, 60)]
    five = random.sample(nums, 5)
    fiveString = [str(x) for x in five]
    conOFentWhiteBalls.set(" ".join(fiveString))
    num = random.choice(range(1, 36))
    conOFentRedBalls.set(str(num))
    
window = Tk()
window.title("Powerball")
btnProduce = Button(window, text="Produce a Drawing", command=drawing)
btnProduce.grid(row=0, column=0, columnspan=2, padx=60, pady=5)
Label(window, text="White balls: ").grid(row=1, column=0, sticky=E)
conOFentWhiteBalls = StringVar()
entWhiteBalls = Entry(window, width=13, fg="white", bg="blue", 
                      textvariable=conOFentWhiteBalls)
entWhiteBalls.grid(row=1, column=1, pady=10, sticky=W)
Label(window, text="Red ball: ").grid(row=2, column=0, sticky=E)
conOFentRedBalls = StringVar()
entRedBalls = Entry(window, width=2, fg="black", bg="white",
                    textvariable=conOFentRedBalls)
entRedBalls.grid(row=2, column=1, pady=10, sticky=W)
window.mainloop()


