import pickle

def main():
    ## Display presidents with a specified first name.
    presDict = createDictFromBinaryFile("USpresStatesDict.dat")
    firstName = input("Enter a first name: ")
    displayOutput(presDict, firstName)
    
def createDictFromBinaryFile(fileName):  
    infile = open(fileName, 'rb')
    dictionaryName = pickle.load(infile)
    infile.close()
    return dictionaryName

def displayOutput(dictName, name):
    foundFlag = False
    for k in dictName:
        x = k[1].split()
        if x[0] == name:
            print("  ", k[1], k[0])
            foundFlag = True
    if not foundFlag:
        print("No president has the first name", name + '.')

main()
