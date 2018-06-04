def main():
    ## Depreciation
    (item, purchYear, cost, numYears, methodOfDepreciation) = inputData()
    showDepSchedule(item, purchYear, cost, numYears, methodOfDepreciation)

def inputData():
    item = input("Enter name of item purchased: ")
    purchYear = int(input("Enter year purchased: "))
    cost = float(input("Enter cost of item: "))
    numYears = int(input("Enter estimated life of item (in years): "))
    methodOfDepreciation = input("Enter method of depreciation (SL or DDB): ")
    return (item, purchYear, cost, numYears, methodOfDepreciation)

def showDepSchedule(item, purchYear, cost, numYears, methodOfDepreciation):
    showHeading(item, purchYear, cost, numYears, methodOfDepreciation)
    if methodOfDepreciation == "SL":
        showSLtable(purchYear, cost, numYears)
    else:
        showDDBtable(purchYear, cost, numYears)

def showHeading(item, purchYear, cost, numYears, methodOfDepreciation):
    print()
    print("Description:", item)
    print("Year of purchase:", purchYear)
    print("Cost: ${0:,.2f}".format(cost))
    print("Estimated life:", numYears, "years")
    if methodOfDepreciation.upper() == "SL":
        method = "straight-line"
        print("Method of depreciation:", method)
    elif methodOfDepreciation.upper() == "DDB":
        method = "double-declining balance"
        print("Method of depreciation:",method)
    print()
    print("{0:5s} {1:>12s} {2:>15s} {3:>20s}".format("", "Value at",
                                    "Amount Deprec", "Total Depreciation"))
    print("{0:5s} {1:>12s} {2:>15s} {3:>20s}".format("", "Beg of Yr.",
                                          "During Year", "to End of Year"))

def showSLtable(purchYear, cost, numYears):
    straightLineDep = (1 / numYears) * cost
    value = cost
    totalDeprec = 0
    for i in range(numYears):
        depDuringYear = straightLineDep
        totalDeprec += depDuringYear
        print("{0:<5d} {1:12,.2f} {2:15,.2f} {3:20,.2f}".format(purchYear + i,
                                           value, depDuringYear, totalDeprec))
        value -=  straightLineDep

def showDDBtable(purchYear, cost, numYears):
    value = cost
    totalDeprec = 0
    for i in range(numYears - 1):
        depDuringYear = (2 / numYears) * value
        totalDeprec += depDuringYear
        print("{0:<5d} {1:12,.2f} {2:15,.2f} {3:20,.2f}".format(purchYear + i,
                                          value, depDuringYear, totalDeprec))
        value -=  depDuringYear 
    print("{0:<5d} {1:12,.2f} {2:15,.2f} {3:20,.2f}".format(purchYear + i + 1,
                                            value, value, totalDeprec + value))

main()


