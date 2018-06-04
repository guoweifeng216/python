import pickle

def main():
    ## Display information about a specific justice.
    justicesDict = createDictFromFile("JusticesDict.dat")
    displayInfoAboutJustice(justicesDict)

def createDictFromFile(fileName):  # from binary file
    infile = open(fileName, 'rb')
    dictionaryName = pickle.load(infile)
    infile.close()
    return dictionaryName

def displayInfoAboutJustice(dictionaryName):
    justice = input("Enter name of a justice: ")
    print("Appointed by", dictionaryName[justice]["pres"])
    print("State:", dictionaryName[justice]["state"])                            
    print("Year of appointment:", dictionaryName[justice]["yrAppt"])
    if dictionaryName[justice]["yrLeft"] == 0:
        print("Currently serving on the Supreme Court.")
    else:
        print("Left court in", dictionaryName[justice]["yrLeft"])

main()
