def main():
    ## Find the greatest common divisor of two non-negative integers.
    m = int(input("Enter the first integer: "))
    n = int(input("Enter the second integer: "))
    print("GCD =", GCD(m, n))
    
def GCD(m, n):
    if n == 0:
        return m
    else:
        return GCD(n, m % n)

main()

        


    

      

