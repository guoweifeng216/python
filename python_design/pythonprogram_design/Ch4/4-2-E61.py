def main():
    ## Sort numbers by the sum of their odd digits in descending order.
    numbers = [865, 1169, 1208, 1243, 290]
    numbers.sort(key=sumOfOddDigits, reverse=True)
    print("Sorted by sum of odd digits:")
    print(numbers)
           
def sumOfOddDigits(num):
    listNums = list(str(num))
    total = 0
    for i in range(len(listNums)):
        if int(listNums[i]) % 2 == 1:
            total += int(listNums[i])
    return total

main()
