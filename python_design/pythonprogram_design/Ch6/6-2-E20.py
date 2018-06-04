import random

def main():            
    total = 0   
    for trial in range(100000):
        L = [n for n in range(1, 60)]
        numbers = random.sample(L, 5)
        # Can replace above two lines with
        # numbers = random.sample(range(1,60), 5)
        numbers.sort()
        if two_consecutive(numbers):
            total += 1
    sentence = " of the time there were at least \ntwo consecutive numbers" + \
               "in the set \nof five numbers."        
    print(("{0:.0%}" + sentence).format(total / 100000))

def two_consecutive(x):
    for index in range(0, 4):
        if x[index] + 1 == x[index + 1]:
            return True

main()
