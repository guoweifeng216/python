def main():
    ## Determine the dogs of the DOW.
    stockList = placeDataIntoList("DOW.txt")
    stockList.sort(key=byDividendToPriceRatio, reverse=True)
    displayDogs(stockList)

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

def byDividendToPriceRatio(stock):
    return stock[7] / stock[5]

def displayDogs(listOfStocks):
    print("{0:25} {1:11} {2:s}".
             format("Company", "Symbol", "Yield as of 12/31/2013"))
    for i in range(10):
        print("{0:25} {1:11} {2:0.2f}%".format(listOfStocks[i][0],
        listOfStocks[i][1], 100 * listOfStocks[i][7] / listOfStocks[i][5]))

main()
