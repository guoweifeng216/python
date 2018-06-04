def main():
    ## Display the sum of the numbers in the file Numbers.txt.
    sum = getSum("Numbers.txt")
    print("The sum of the numbers in \nthe file Numbers.txt is",
          str(sum) + ".") 
    	
def getSum(fileName):
    infile = open("Numbers.txt", 'r')
    sum = 0
    for line in infile:
        sum += int(line)
    infile.close()        
    return sum

main()

