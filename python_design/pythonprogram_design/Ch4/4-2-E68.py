def main():
    ## Analyze monthly payment of mortgage.
    annualRateOfInterest, monthlyPayment, begBalance = inputData()  
    (intForMonth, redOfPrincipal, endBalance)= \
        calculateValues(annualRateOfInterest, monthlyPayment, begBalance)
    displayOutput(intForMonth, redOfPrincipal, endBalance)

def inputData():
    annualRateOfInterest = eval(input("Enter annual rate of interest: "))
    monthlyPayment = eval(input("Enter monthly payment: "))
    begBalance = eval(input("Enter beg. of month balance: ")) 
    return (annualRateOfInterest, monthlyPayment, begBalance)

def calculateValues(annualRateOfInterest, monthlyPayment, begBalance):
    intForMonth = (annualRateOfInterest / 1200) * begBalance
    redOfPrincipal = monthlyPayment - intForMonth
    endBalance = begBalance - redOfPrincipal
    return (intForMonth, redOfPrincipal, endBalance)

def displayOutput(intForMonth, redOfPrincipal, endBalance):
    print("Interest paid for the month: ${0:,.2f}".format(intForMonth)) 
    print("Reduction of principal: ${0:,.2f}".format(redOfPrincipal))
    print("End of month balance: ${0:,.2f}".format(endBalance))

main()    
