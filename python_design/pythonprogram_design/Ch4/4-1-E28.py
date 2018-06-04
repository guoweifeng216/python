def main():
    ## Calculate a factorial.
    n = getN()
    print(str(n) + '!', "is", fact(n))

def getN():
    while True:
        n = eval(input("Enter a positive integer: "))
        if isinstance(n, int) and (n > 0):
            return n
        else:
            print("The number you entered is not a positve integer.")

def fact(n):
    product = 1
    for i in range(2, n + 1):
        product *= i
    return product
 
main()
        
    

