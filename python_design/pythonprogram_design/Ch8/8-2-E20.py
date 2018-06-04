from tkinter import *

window = Tk()
window.title("Academy Awards")
Label(window, text="GENRES").grid(row=0, column=0)
Label(window, text="FILMS").grid(row=0, column=1)
genreSet = {line.split(',')[1].rstrip() \
                  for line in open("Oscars.txt", 'r')}
L = list(genreSet)
lstGenres = Listbox(window, width=9, height=len(L))
lstGenres.grid(row=1, column=0, padx=10, sticky=N)
lstGenres.bind("<<ListboxSelect>>")
yscroll = Scrollbar(window, orient=VERTICAL)
yscroll.grid(row=1, column=2, sticky=NS)
lstFilms = Listbox(window, width=28, height=len(L),
                       yscrollcommand=yscroll.set)
lstFilms.grid(row=1, column=1, sticky=NSEW)
yscroll["command"] = lstFilms.yview
window.mainloop()
