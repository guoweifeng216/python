def main():
    ## Sort numbers by largest prime factor.
    numbers = [865, 1169, 1208, 1243, 290]
    numbers.sort(key=largestPrimeFactor)
    print("Sorted by largest prime factor:")
    print(numbers)

def largestPrimeFactor(num):
    n = num
    f = 2
    max = 1
    while n > 1:
        if n % f == 0:
            n = int(n / f)
            if f > max:
                max = f
        else:
            f += 1
    return max

main()
