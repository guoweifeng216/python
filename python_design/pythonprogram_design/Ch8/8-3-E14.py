from tkinter import *

class Oscars:
    def __init__(self):
        window = Tk()
        window.title("Academy Awards")
        caption = "Year (1928-2013): "
        Label(window, text=caption).grid(row=0, column=0)
        self._conOFentYear = StringVar()
        self.entYear = Entry(window, width=4,
                             textvariable=self._conOFentYear)
        self.entYear.grid(row=0, column=1, sticky=W)
        caption = "Find Best Picture"
        btnFind = Button(window, text=caption, command=self.displayFilm)
        btnFind.grid(row=1, column=1, pady=2)
        Label(window, text="Film:").grid(row=2, column=0, sticky=E)
        Label(window, text="Genre:").grid(row=3, column=0, pady=5,
                                          sticky=E)
        self._conOFentFilm = StringVar()
        self.entFilm = Entry(window, width=30, state="readonly",
                            textvariable=self._conOFentFilm)
        self.entFilm.grid(row=2, column=1, padx=5,sticky=W)
        self._conOFentGenre = StringVar()
        self.entGenre = Entry(window, width=30, state="readonly",
                              textvariable=self._conOFentGenre)
        self.entGenre.grid(row=3, column=1, padx=5,pady=5, sticky=W)
        window.mainloop()
 
    def displayFilm(self):
        infile = open("Oscars.txt", 'r')
        for i in range(int(self._conOFentYear.get()) - 1928):
            infile.readline()
        line = infile.readline().rstrip()
        data = line.split(',')
        self._conOFentFilm.set(data[0])
        self._conOFentGenre.set(data[1])

Oscars()
