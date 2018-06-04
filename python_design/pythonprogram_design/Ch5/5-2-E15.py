
def main():
    ## Twelve Days of Christmas
    listOfDaysCosts = createListOfDaysCosts()
    print(listOfDaysCosts)
    day = int(input("Enter a number from 1 through 12: "))
    displayOutput(day, listOfDaysCosts)

def createListOfDaysCosts():
    infile = open("Gifts.txt", 'r')
    costs = [float(line.split(',')[2]) for line in infile]
    infile.close()
    listOfDaysCosts = [0] * 12
    for i in range(12):
        listOfDaysCosts[i] = (i + 1) * costs[i]
    return listOfDaysCosts

def displayOutput(day, listOfDaysCosts):
    print("The gifts for day", day, "are")
    infile = open("Gifts.txt", 'r')
    for i in range(day):
        data = infile.readline().split(',')
        print(int(data[0]), data[1])
    print()
    print("Cost for day {0}: ${1:,.2f}".
           format(day, sum(listOfDaysCosts[:day])))
    totalCosts = 0
    for i in range(day):
        totalCosts += sum(listOfDaysCosts[:i + 1])
        print(totalCosts)
    print("Total cost for the first {0} days: ${1:,.2f}"
           .format(day, totalCosts))
    
main()
