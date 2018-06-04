def main():
    ## Display the last number in the file Numbers.txt.
    lastNumber = getLastNumber("Numbers.txt")
    print("The last number in the \nfile Numbers.txt is",
          str(lastNumber) + '.') 
    	
def getLastNumber(fileName):
    infile = open("Numbers.txt", 'r')
    for line in infile:
        pass
    lastNumber = eval(line)
    infile.close()
    return lastNumber

main()

