def main():
    ## Sort numbers in descending order by their last digit.
    numbers = [865, 1169, 1208, 1243, 290]
    numbers.sort(key=lastDigit, reverse=True)
    print("Sorted by last digit:")
    print(numbers)

def lastDigit(num):
    return str(num)[-1]

main()
