def main():
    ## Determine best and worst performing stocks in the DOW.
    stockList = placeDataIntoList("DOW.txt")
    print(stockList)
    stockList.sort(key=byPercentGrowth)
    print(stockList)
    increase = (float(stockList[-1][5]) - float(stockList[-1][4])) / \
                                                 float(stockList[-1][4])
    print("Best performing stock: {0:1}  {1:0,.2f}%".
                               format(stockList[-1][0], 100 * increase))
    increase = (float(stockList[0][5]) - float(stockList[0][4])) / \
                                                  float(stockList[0][4])
    print("Worst performing stock: {0:1}  {1:0,.2f}%".
                                format(stockList[0][0], 100 * increase))    

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

def byPercentGrowth(stock):
    print(stock)
    percentIncrease = (float(stock[5]) - float(stock[4])) / float(stock[4])
    return percentIncrease

main()
