def main():
    ## Count the number of numbers in the file Numbers.txt.
    count = getCount("Numbers.txt")
    print("The file Numbers.txt \ncontains", count, "numbers.")
       	
def getCount(fileName):
    infile = open(fileName, 'r')
    count = 0
    for line in infile:
        count += 1
    infile.close()
    return count

main()

