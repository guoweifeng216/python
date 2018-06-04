import pickle

def main():
    justicesDict = createDictFromFile("JusticesDict.dat")
    displayJusticesFromState(justicesDict)

def createDictFromFile(fileName):  # from binary file
    infile = open(fileName, 'rb')
    dictionaryName = pickle.load(infile)
    infile.close()
    return dictionaryName

def displayJusticesFromState(dictionaryName):
    state = input("Enter a state abbreviation: ")
    for x in dictionaryName:
        if dictionaryName[x]["state"] == state:
            print("  {0:19}{1}".format(x, str(dictionaryName[x]["yrAppt"])))
                      
main()
