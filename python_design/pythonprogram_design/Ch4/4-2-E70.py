def main():
    ## Use Wilson's Theorem to determine if a number is prime.
    n = int(input("Enter an integer greater than 1: "))
    if isPrime(n):
        print(n, "is a prime number.")
    else:
        print(n, "is not a prime number.")                                   

def isPrime(n):
    if (factorial(n - 1) + 1) % n:
        return False
    else:
        return True

def factorial(n):
    value = 1
    for i in range(2, n + 1):
        value *= i
    return value    
    
main()
