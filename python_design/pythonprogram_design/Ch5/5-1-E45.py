def main():
    ## Display a range of presidents.
    lowerNumber, upperNumber = getRange()
    displayPresidents(lowerNumber, upperNumber)

def getRange():
    lowerNumber = int(input("Enter the lower number for the range: "))
    upperNumber = int(input("Enter the upper number for the range: "))
    return (lowerNumber, upperNumber)

def displayPresidents(lowerNumber, upperNumber):   
    infile = open("USpres.txt", 'r')
    count = 0
    for pres in infile:
        count += 1
        if lowerNumber <= count <= upperNumber:
            print(" ", count, pres, end="")
    infile.close()
    
main()
