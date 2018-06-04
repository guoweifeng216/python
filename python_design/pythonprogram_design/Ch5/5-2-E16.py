def main():
    ## Determine accomplishments of computer pioneers.
    displayNames("Pioneers.txt")
    print('\n')
    name = input("Enter the name of a computer pioneer: ")
    displayAccomplishment("Pioneers.txt", name)
   
def displayNames(fileName):
    infile = open(fileName, 'r')
    for line in infile:
        lineList = line.split(',')
        print((lineList[0] + '\t').expandtabs(20), end="")
    infile.close()  

def displayAccomplishment(fileName, name):
    infile = open(fileName, 'r')
    for line in infile:
        lineList = line.split(',')
        if lineList[0] == name:
            print(name, lineList[1].rstrip() + '.')
            infile.close()
            break
        
main()

