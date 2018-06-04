import random

## Create a file containing the states in a random order.
infile = open("StatesAlpha.txt", 'r')
states = [line for line in infile]
infile.close()
random.shuffle(states)
outfile = open("RandomStates.txt", 'w')
outfile.writelines(states)
outfile.close()




          
