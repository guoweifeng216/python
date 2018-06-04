def main():
    ## Calculate the balance owed on a mortgage.
    p = float(input("Enter the principal: "))
    r = float(input("Enter the annual rate of interest: "))
    pmt = float(input("Enter the monthly payment: "))
    n = int(input("Enter the number of monthly payments made: "))
    print("The amount still owed is ${0:,.2f}.".format(balance(p,
          pmt, r, n)))
    
def balance(p, pmt, r, n):
    if n == 0:
        return p
    else:
        return (1 + r/1200) * balance(p, pmt, r, n - 1) - pmt
       
main()
