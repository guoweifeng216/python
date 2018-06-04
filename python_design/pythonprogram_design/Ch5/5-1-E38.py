def main():
    ## Display the average of the numbers in the file Numbers.txt.
    average = getAverage("Numbers.txt")
    print("The average of the numbers in \nthe file Numbers.txt is {0:,.1f}."
          .format(average)) 
    	
def getAverage(fileName):
    infile = open("Numbers.txt", 'r')
    sum = 0
    quantity = 0
    for line in infile:
        sum += int(line)
        quantity += 1
    infile.close()
    return sum / quantity

main()

