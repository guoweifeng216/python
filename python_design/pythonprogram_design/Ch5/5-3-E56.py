def main():
    ## display winningest Rose Bowl winners.
    roseBowlDict = createDictionaryFromTextFile("Rosebowl.txt")
    displayTopTenTeams(roseBowlDict)
    
def createDictionaryFromTextFile(fileName):
    # each item of the list will be a line of the file, without \n
    infile = open(fileName, 'r')
    #roseBowlList = infile.read().splitlines()
    roseBowlList = [line.rstrip() for line in infile]
    infile.close()
    aSet = set(roseBowlList)
    infile.close()
    roseBowlDict = {}
    for x in aSet:
        roseBowlDict[x] = 0
    for x in roseBowlList:
        roseBowlDict[x] += 1
    return roseBowlDict

def displayTopTenTeams(dictionaryName):
    dictionaryList = list(dictionaryName.items())
    dictionaryList.sort(key=f, reverse=True)
    print("Teams with four or more")
    print("Rose Bowl wins as of 2014.")
    for x in dictionaryList:
        if x[1] > 3:
            print("  " + x[0] + ':', x[1])
        
def f(k):
    return k[1]

main()

