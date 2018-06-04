while True:
    try:
        n = int(input("Enter a nonzero integer: "))
        reciprocal = 1 / n
        print("The reciprocal of {0} is {1:,.3f}".format(n, reciprocal))
        break
    except ValueError:
        print("You did not enter a nonzero integer. Try again.")
    except ZeroDivisionError:
        print("You entered zero. Try again.")
        
    
