def main():
    ## Display name of currency and exchange rate for requested country.
    country = input("Enter the name of a country: ")
    infile = open("Exchrate.txt", 'r')
    foundFlag = False
    for line in infile:
        line = line.rstrip()
        data = line.split(',')
        if data[0] == country:
            foundFlag = True
            print("Currency:", data[1])
            print("Exchange rate:", data[2])
            break
    if not foundFlag:
        print(country, "is not in the file.")
main()
