def main():
    ## Convert currency.
    country1 = input("Enter the name of first country: ")
    country2 = input("Enter the name of second country: ")
    amount = eval(input("Enter amount of money to convert: "))
    infile = open("Exchrate.txt", 'r')
    countryList = [line.rstrip() for line in infile]
    infile.close()
    d = {}
    for i in range(len(countryList)):
        countryList[i] = countryList[i].split(',')
        d[countryList[i][0]] = (countryList[i][1], eval(countryList[i][2]))
    print("{0} {1}s from {2} equals {3:,.2f} {4}s from {5}".
        format(amount, d[country1][0].lower(), country1, amount *
        d[country2][1] / d[country1][1], d[country2][0].lower(), country2)) 
         
main()
