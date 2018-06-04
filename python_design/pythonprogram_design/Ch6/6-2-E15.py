import random

## Select three states at random from a file containing the 50 states.
allNumbers = [n for n in range(1, 51)]
# Randomly select three numbers from 1 through 50.
threeNumbers = random.sample(allNumbers, 3)
infile = open("StatesAlpha.txt", 'r')
lineNumber = 1
for line in infile:
    if lineNumber in threeNumbers:
        print(line.rstrip())
    lineNumber += 1
infile.close()        







          
