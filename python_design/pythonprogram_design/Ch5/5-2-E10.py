def main():
    ## Determine the Small Dogs of the DOW.
    stockList = placeDataIntoList("DOW.txt")
    stockList.sort(key=byEndOfYearPrice)
    displaySmallDogs(stockList)

def placeDataIntoList(fileName):
    infile = open(fileName, 'r')
    listOfLines = [line.rstrip() for line in infile]
    infile.close()
    for i in range(len(listOfLines)):
        listOfLines[i] = listOfLines[i].split(',')
        listOfLines[i][4] = eval(listOfLines[i][4])
        listOfLines[i][5] = eval(listOfLines[i][5])
        listOfLines[i][6] = eval(listOfLines[i][6])
        listOfLines[i][7] = eval(listOfLines[i][7])
    return listOfLines

def byEndOfYearPrice(stock):
    return stock[5]

def displaySmallDogs(listOfStocks):
    print("{0:20} {1:8}   {2:s}".format("Company", "Symbol",
                                        "Price on 12/31/2013"))
    for i in range(5):
        print("{0:20} {1:8}   ${2:0.2f}".format(listOfStocks[i][0],
                           listOfStocks[i][1], listOfStocks[i][5]))

main()
