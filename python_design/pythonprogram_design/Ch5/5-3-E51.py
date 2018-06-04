import pickle

def main():
    ## Display justices appointed by a specified president.
    justicesDict = createDictFromFile("JusticesDict.dat")
    displayPresidentialAppointees(justicesDict)
    
def createDictFromFile(fileName):  # from binary file
    infile = open(fileName, 'rb')
    dictionaryName = pickle.load(infile)
    infile.close()
    return dictionaryName

def displayPresidentialAppointees(dictionaryName):
    pres = input("Enter a president: ")
    for x in dictionaryName:
        if dictionaryName[x]["pres"] == pres:
            print("  {0:16} {1:d}".format(x, dictionaryName[x]["yrAppt"]))
                            
main()
