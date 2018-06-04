import pickle

def main():
    justicesDict = createDictFromFile("JusticesDict.dat")
    displayStatesWithJustices(justicesDict)

def createDictFromFile(fileName):  # from binary file
    infile = open(fileName, 'rb')
    dictionaryName = pickle.load(infile)
    infile.close()
    return dictionaryName

def displayStatesWithJustices(dictionaryName):
    states = {}
    for justice in dictionaryName:
        states[(dictionaryName[justice]["state"])] = 0
    print(len(states), "states have produced justices.")    
    for justice in dictionaryName:
        states[(dictionaryName[justice]["state"])] += 1        
    for state in sorted(states): 
        print("  " +  state + ': ' + str(states[state]))
                            
main()
