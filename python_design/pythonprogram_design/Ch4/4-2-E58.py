def main():
    ## Sort numbers by the sum of their digits in ascending order.
    numbers = [865, 1169, 1208, 1243, 290]
    numbers.sort(key=sumOfDigits)
    print("Sorted by sum of digits:")
    print(numbers)

def sumOfDigits(num):
    listNums = list(str(num))
    for i in range(len(listNums)):
        listNums[i] = int(listNums[i]) 
    return sum(listNums)    

main()
