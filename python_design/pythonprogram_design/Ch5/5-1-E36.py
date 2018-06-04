def main():
    ## Display the smallest number in the file Numbers.txt.
    min = getMin("Numbers.txt")
    print("The smallest number in the \nfile Numbers.txt is",
          str(min) + ".") 
    	
def getMin(fileName):
    infile = open("Numbers.txt", 'r')
    min = int(infile.readline())
    for line in infile:
        num = int(line)
        if num < min:
            min = num
    infile.close()            
    return min

main() 
