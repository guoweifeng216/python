def main():
    ## Sort countries by number of units of their currency 
    ## that can be purchased for one American dollar.
    infile = open("Exchrate.txt", 'r')
    countryList = [line.rstrip() for line in infile]
    infile.close()
    for i in range(len(countryList)):
        countryList[i] = countryList[i].split(',')
    countryList.sort(key=lambda x: x[2])
    for i in range(3):
        print(countryList[i][0])

main()
