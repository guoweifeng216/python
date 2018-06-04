## Determine number of states that have produced presidents.
infile = open("PresStates.txt", 'r')
statesSet = {state.rstrip() for state in infile}
infile.close()
print(statesSet)
print(len(statesSet), "different states have")
print("produced presidents of the \nUnited States.")

