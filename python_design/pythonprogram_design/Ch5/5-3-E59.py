def main():
    ## Determine the day of the week for a date.
    calendar2015Dict = createDictionary("Calendar2015.txt")
    date = input("Enter a date in 2015: ")
    print(date, "falls on a", calendar2015Dict[date])
                      
def createDictionary(fileName):
    infile = open(fileName, 'r')
    textList = [line.rstrip() for line in infile]
    infile.close()
    return dict([x.split(',') for x in textList])

main()

