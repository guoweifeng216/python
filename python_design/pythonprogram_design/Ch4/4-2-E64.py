def main():
    ## Sort states by length of name in descending order.
    infile = open("States.txt", 'r')
    listStates = [state.rstrip() for state in infile]
    infile.close()
    listStates.sort(key=sortByLengthOfName, reverse=True)      
    for i in range(6):
        print(listStates[i])

def sortByLengthOfName(state):
    return len(state)

main()
