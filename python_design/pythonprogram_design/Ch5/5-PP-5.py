import pickle

def main():
    ## Display tables containing information about bachelor degrees earned.
    degreesDict = createDictFromFile("DegreesDict.dat")
    print("1: Display bachelor degrees conferred.")
    print("2: Display percentage change.")
    print("3: Display histogram.")
    print("4: Quit.")
    while True:
        print()
        choice = int(input("Enter one of the options: "))
        if choice == 1:
            print()
            displayBachelorDegreesConferred(degreesDict)
        elif choice == 2:
            print()
            displayPercentageChange(degreesDict)
        elif choice == 3:
            print()
            displayHistogram(degreesDict)
        else:
            break
    
def createDictFromFile(fileName):  # from binary file
    infile = open(fileName, 'rb')
    dictionaryName = pickle.load(infile)
    infile.close()
    return dictionaryName

def displayBachelorDegreesConferred(degreesDict):
    print("Bachelor degrees conferred in certain fields.\n")
    print("{0:37}     {1}             {2}".
          format("Field of Study", 1981, 2010))
    for field in sorted(degreesDict):
        print("{0:37}{1:10,d}       {2:10,d}".
           format(field,degreesDict[field][0], degreesDict[field][1]))

def displayPercentageChange(degreesDict):
    print("Percentage change in bachelor degrees conferred.\n")
    print("{0:37}{1}".format("Field of Study", "% Change (1981-2010)"))
    for field in sorted(degreesDict, key=lambda k: f(degreesDict[k][1],
                degreesDict[k][0]), reverse=True):
        print("{0:42}{1:>7.1%}".format(field, f(degreesDict[field][1],
                degreesDict[field][0])))
                      
def f(x, y):
    ## return percentage change
    return (x - y) / y

def displayHistogram(degreesDict):
    print("Bachelor degrees conferred in 2010 in certain fields.\n")
    for field in sorted(degreesDict, key=lambda k: degreesDict[k][1]):
        asterisks = '*' * round(degreesDict[field][1] / 10000) 
        print("{0:>27} {1} {2:,d}".
              format(field, asterisks, degreesDict[field][1]))
 
main()

    
