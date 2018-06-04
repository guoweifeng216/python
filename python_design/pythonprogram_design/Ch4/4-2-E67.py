def main():
    ## Calculate new balance and minimum payment for a credit card.
    (oldBalance, charges, credits) = inputData()
    (newBalance, minimumPayment) = calculateNewValues(oldBalance,
                                   charges, credits)
    displayNewData(newBalance, minimumPayment)

def inputData():
   oldBalance = float(input("Enter old balance: "))
   charges = float(input("Enter charges for month: "))
   credits = float(input("Enter credits: "))
   return (oldBalance, charges, credits)

def calculateNewValues(oldBalance, charges, credits):
    newBalance =  (1.015) * oldBalance + charges - credits
    if newBalance <= 20:
        minimumPayment = newBalance  
    else:
        minimumPayment = 20 + (0.1 * (newBalance - 20)  )
    return (newBalance, minimumPayment)       

def displayNewData(newBalance, minimumPayment):
    print("New balance: ${0:0,.2f}".format(newBalance))
    print("Minimum payment: ${0:0,.2f}".format(minimumPayment))     

main()
