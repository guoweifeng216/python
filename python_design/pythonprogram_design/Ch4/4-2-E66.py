def main():
    ## Calculate pay raise.
    (firstName, lastName, currentSalary) = getNameAndCurrentSalary()
    newSalary = calculateNewSalary(currentSalary)
    displayResult(firstName, lastName, newSalary) 

def getNameAndCurrentSalary():
    firstName = input("Enter first name: ")
    lastName = input("Enter second name: ")
    currentSalary = float(input("Enter current salary: "))
    return (firstName, lastName, currentSalary)

def calculateNewSalary(currentSalary):
    if currentSalary < 40000:
        return (currentSalary * 1.05)
    else:
        return 2000 + currentSalary + (.02 * (currentSalary - 40000))

def displayResult(firstName, lastName, newSalary):
    print("New salary for {0} {1}: ${2:,.2f}"
          .format(firstName, lastName, newSalary))

main()
