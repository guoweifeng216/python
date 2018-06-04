from tkinter import *

window = Tk()
window.title("Best Picture")
Label(window, text="Academy Award (1928-2013):").grid(row=0, column=0,
                                    padx=(20,3), pady=5, columnspan=2)
entYear = Entry(window, width=6)
entYear.grid(row=0, column=2, pady=10, sticky=W)
btnFind = Button(window, text="Find Best Picture")
btnFind.grid(row=1, column=0, columnspan=3, pady=(0,8))
Label(window, text="Film:").grid(row=2, column=0, sticky=E)
entFilm = Entry(window, width=37, state="readonly")
entFilm.grid(row=2, column=1, columnspan=2, padx=5, sticky=W)
Label(window, text="Genre:").grid(row=3, column=0, pady=5, sticky=E)
entGenre = Entry(window, width=37, state="readonly")
entGenre.grid(row=3, column=1, columnspan=2, padx=5, sticky=W)
window.mainloop()
