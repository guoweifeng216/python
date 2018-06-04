def main():
    ## Display information about a DOW stock.
    symbols = placeSymbolsIntoList("DOW.txt")
    displaySymbols(symbols)
    print()
    symbol = input("Enter a symbol: ")
    infile = open("DOW.txt", 'r')
    abbrev = ""
    while abbrev != symbol:
        line = infile.readline()
        lineList = line.split(',')
        print(len(lineList))
        abbrev = lineList[1]
    infile.close()

    print("Company:", lineList[0])
    print("Industry:", lineList[3])
    print("Exchange:", lineList[2])
    increase = (float(lineList[5]) - float(lineList[4])) / float(lineList[4])
    print("Growth in 2013: {0:0,.2f}%".format(100 * increase))
    priceEarningsRatio = float(lineList[5]) / float(lineList[6])
    print("Price/Earnings ratio in 2013: {0:0,.2f}".
                       format(priceEarningsRatio))
    
def placeSymbolsIntoList(fileName):
    symbolList = [""] * 30
    infile = open(fileName, 'r')
    for i in range(30):
        line = infile.readline()
        lineList = line.split(',')
        symbolList[i] = lineList[1]
        # symbolList.append(lineList[1])
    infile.close()    
    return symbolList

def displaySymbols(symbols):
    ## Display symbols in alphabetical order
    symbols.sort()
    print("Symbols for the Thirty DOW Stocks")
    for symbol in symbols:
        print("{0:5}\t".format(symbol), end='')
   
main()
