from tkinter import *

def films(e):
    genre = lstGenres.get(lstGenres.curselection())
    F = [line.split(',')[0] for line in open("Oscars.txt", 'r') if line.split(',')[1].rstrip() == genre]
    conOFlstFilms.set(tuple(F))

window = Tk()
window.title("Academy Award Winners")
Label(window, text="GENRES").grid(row=0, column=0)
Label(window, text="FILMS").grid(row=0, column=1)
genreSet = {line.split(',')[1].rstrip() for line in open("Oscars.txt", 'r')}
L = list(genreSet)
L.sort()
conOFlstGenres = StringVar()
lstGenres = Listbox(window, width=9, height=len(L), listvariable=conOFlstGenres)
lstGenres.grid(row=1, column=0, padx=10, sticky=N)
conOFlstGenres.set(tuple(L))
lstGenres.bind("<<ListboxSelect>>", films)
yscroll = Scrollbar(window, orient=VERTICAL)
yscroll.grid(row=1, column=2, sticky=NS)
conOFlstFilms = StringVar()
lstFilms = Listbox(window, width=45, height=len(L), listvariable=conOFlstFilms,
                   yscrollcommand=yscroll.set)
lstFilms.grid(row=1, column=1, sticky=NSEW)
yscroll["command"] = lstFilms.yview
window.mainloop()


##from tkinter import *
##
##class Oscars:
##
##    def __init__(self):
##        window = Tk()
##        window.title("Academy Award Winners")
##        Label(window, text="GENRES").grid(row=0, column=0)
##        Label(window, text="FILMS").grid(row=0, column=1)
##        self._genreSet = {line.split(',')[1].rstrip() \
##                          for line in open("Oscars.txt", 'r')}
##        self._L = list(self._genreSet)
##        self._L.sort()
##        self._conOFlstGenres = StringVar()
##        self._lstGenres = Listbox(window, width=9, height=len(self._L),
##                                  listvariable=self._conOFlstGenres)
##        self._lstGenres.grid(row=1, column=0, padx=10, sticky=N)
##        self._conOFlstGenres.set(tuple(self._L))
##        self._lstGenres.bind("<<ListboxSelect>>", self.films)
##        yscroll = Scrollbar(window, orient=VERTICAL)
##        yscroll.grid(row=1, column=2, sticky=NS)
##        self._conOFlstFilms = StringVar()
##        lstFilms = Listbox(window, width=45, height=len(self._L),
##                           listvariable=self._conOFlstFilms,
##                           yscrollcommand=yscroll.set)
##        lstFilms.grid(row=1, column=1, sticky=NSEW)
##        yscroll["command"] = lstFilms.yview
##        window.mainloop()
##
##    def films(self, e):
##        genre = self._lstGenres.get(self._lstGenres.curselection())
##        F = [line.split(',')[0] for line in open("Oscars.txt", 'r') \
##             if line.split(',')[1].rstrip() == genre]
##        self._conOFlstFilms.set(tuple(F))
##
##Oscars()
