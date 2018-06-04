def main():
    ## Display the largest number in the file Numbers.txt
    max = getMax("Numbers.txt")
    print("The largest number in the \nfile Numbers.txt is",
          str(max) + ".") 
    	
def getMax(fileName):
    infile = open("Numbers.txt", 'r')
    max = int(infile.readline())
    for line in infile:
        num = int(line)
        if num > max:
            max = num
    infile.close()            
    return max

main() 
