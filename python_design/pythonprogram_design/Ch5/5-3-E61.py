import pickle

def main():
    ## Determine states having a specified number of large cities.
    largeCities = createDictionaryFromBinaryFile("LargeCitiesDict.dat")
    number = int(input("Enter an integer from 1 to 13: "))
    states = sorted(getStates(number, largeCities))
    displayResult(number, states)
    
def createDictionaryFromBinaryFile(fileName):
    # Assume pickle module has been imported.
    infile = open(fileName, 'rb')
    dictionaryName = pickle.load(infile)
    infile.close()
    return dictionaryName

def getStates(number,dictionaryName):
    states = []
    for state in dictionaryName:
        if len(dictionaryName[state]) == number:
            states.append(state)
    return states        

def displayResult(number, states):
     if len(states) == 0:
         print("No states have exactly", number, "large cities.")
     else:    
         print("The following states have exactly", number, "large cities:")
         print("  ".join(states))
    
main()

