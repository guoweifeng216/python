def main():
    ## Determine largest and smallest prime factors of a number.
    n = int(input("Enter a positive integer: "))
    print("Largest prime factor:", extremeFactors(n)[0])
    print("Smallest prime factor:", extremeFactors(n)[1])
    
def extremeFactors(n):
    listOfPrimeFactors = []
    f = 2
    while n > 1:
        if n // f == n / f:    # true if f divides n
            listOfPrimeFactors.append(f)
            n = n // f
        else: 
            f += 1
    largestPrimeFactor = max(listOfPrimeFactors)
    smallestPrimeFactor = min(listOfPrimeFactors)
    return (largestPrimeFactor, smallestPrimeFactor)

main()
