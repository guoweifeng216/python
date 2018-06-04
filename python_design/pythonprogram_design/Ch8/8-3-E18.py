from tkinter import *

class PresColleges:

    def __init__(self):
        window = Tk()
        window.title("Presidential Colleges")
        instruction = "Click on a college."
        Label(window, text=instruction).grid(row=0, column=0,
                                             columnspan=3, pady=5)
        Label(window, text="COLLEGE", width=14).grid(row=1, column=0)
        Label(window, text="PRESIDENTS").grid(row=1, column=2)
        yscroll = Scrollbar(window, orient=VERTICAL)
        yscroll.grid(row=2, column=1, pady=5, sticky=NS)

        infile = open("PresColl.txt", 'r')
        collegeSet = {line.split(',')[1].rstrip() for line in infile}
        infile.close()
        collegeList = list(collegeSet)
        collegeList.sort()
        conOFlstColleges = StringVar()
        self._lstColleges = Listbox(window, width=20, height=8, 
                 listvariable=conOFlstColleges, yscrollcommand=yscroll.set)
        self._lstColleges.grid(row=2, column=0, padx=(5,0), pady=5, sticky=E)
        self._lstColleges.bind("<<ListboxSelect>>", self.presidents)
        conOFlstColleges.set(tuple(collegeList))

        self._conOFlstPresidents = StringVar()
        self._lstPresidents = Listbox(window, width=18, height=8,
                                    listvariable=self._conOFlstPresidents)
        self._lstPresidents.grid(row=2, column=2, padx=8, pady=5, sticky=N)
        yscroll["command"] = self._lstColleges.yview
        window.mainloop()
        
    def presidents(self, e):
        self.L = []
        college = self._lstColleges.get(self._lstColleges.curselection())
        for line in open("PresColl.txt", 'r'):
            temp = line.split(',')
            if temp[1].rstrip() == college:
                self.L.append(temp[0])
        self._conOFlstPresidents.set(tuple(self.L))

PresColleges()


