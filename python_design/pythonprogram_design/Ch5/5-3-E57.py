import pickle

def main():
    ## Determine states that were home to three or more presidents.
    presidents = getDictionary("USpresStatesDict.dat")
    states = createStatesDict(presidents)
    sortedStates = [state for state in states if states[state] > 2]
    sortedStates.sort(key=lambda state: states[state], reverse=True)
    print("States that produced three or")
    print("more presidents as of 2016:")
    for state in sortedStates:
        print(" ", state + ":", states[state])
    
def getDictionary(fileName):
    infile = open(fileName, 'rb')
    dictName = pickle.load(infile)
    infile.close()
    return dictName

def createStatesDict(presidents):
    states = {}
    for state in presidents.values():
        if not states.get(state, False):
            states[state] = 1
        else:
            states[state] += 1
    return states

main()


