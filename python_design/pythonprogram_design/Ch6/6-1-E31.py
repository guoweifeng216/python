while True:
    try:
        num = int(input("Enter an integer from 1 to 100: "))
        if 1 <= num <= 100:
            print("Your number is", str(num) + '.')
            break
        else:
            print("Your number was not between 1 and 100.")
    except ValueError:
        print("You did not enter an integer.")
        


