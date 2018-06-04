from tkinter import *

def convertUnits():
    kph = 1.61 * eval(conOFentMPH.get())
    conOFentKPH.set("{0:,.2f}".format(kph))

window = Tk()
window.title("Conversion")
conOFentMPH = StringVar()
entMPH = Entry(window, width=6, textvariable=conOFentMPH)
entMPH.grid(row=0, column=1, pady=10)
Label(window, text="miles per hour").grid(row=0, column=2, sticky=W)
Label(window, text="is equivalent to").grid(row=1, column=0)
conOFentKPH = StringVar()
entKPH = Entry(window, width=6, textvariable=conOFentKPH, state="readonly")
entKPH.grid(row=1, column=1, padx=5)
Label(window, text="kilometers per hour").grid(row=1, column=2)
btnCalculate = Button(window, text="Convert", command=convertUnits)
btnCalculate.grid(row=2, column=2,pady=10)
window.mainloop()






