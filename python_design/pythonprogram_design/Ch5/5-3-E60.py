import pickle

def main():
    ## Display the large cities in a specified state.
    largeCities = createDictionaryFromBinaryFile("LargeCitiesDict.dat")
    state = input("Enter the name of a state: ")
    getCities(state, largeCities)

def createDictionaryFromBinaryFile(fileName):
    # Assume pickle module has been imported.
    infile = open(fileName, 'rb')
    dictionaryName = pickle.load(infile)
    infile.close()
    return dictionaryName

def getCities(state, dictionaryName):
    if dictionaryName[state] != []:
        print("Large cities:", "  ".join(dictionaryName[state]))
    else:
        print("There are no large cities in", state + '.')               

main()

