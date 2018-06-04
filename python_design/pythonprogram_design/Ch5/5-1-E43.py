def main():
    ## Create alphabetical file of last 37 states to join the union.
    lastStates = getListOfLastStates()
    createFileOfLastStates(lastStates)
    
def getListOfLastStates():
    infile = open("AllStates.txt", 'r')
    states = {state.rstrip() for state in infile}
    infile.close()
    infile = open("FirstStates.txt", 'r')
    firstStates = {state.rstrip() for state in infile}
    infile.close()
    lastStates = list(states.difference(firstStates))
    lastStates.sort()
    return lastStates

def createFileOfLastStates(lastStates):
    outfile = open("LastStates.txt", 'w')
    outfile.writelines(lastStates)
    outfile.close()

main()
