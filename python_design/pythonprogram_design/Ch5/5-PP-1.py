def main():
    ## Convert units of length.
    feet = populateDictionary("Units.txt")
    displayUnits(feet)
    orig, dest, length = getInput()
    ans = length * feet[orig] / feet[dest]
    print("Length in {0}: {1:,.4f}".format(dest, ans))


def populateDictionary(fileName):
    infile = open(fileName, 'r')
    feet = {}
    for line in infile:
        temp = line.split(',')
        feet[temp[0]] = eval(temp[1])
    return feet

def displayUnits(feet):
    print("UNITS OF LENGTH")
    i = 0
    for key in feet:
        print((key + '\t').expandtabs(12), end="")
        i += 1
        if i % 3 == 0:
            print()
    print()
    
def getInput():
    orig = input("Units to convert from: ")
    dest = input("Units to convert to: ")
    length = eval(input("Enter length in " + orig + ": "))
    return orig, dest, length
         
main()
