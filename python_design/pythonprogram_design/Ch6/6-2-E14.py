import random

## Approximate the probability of obtaining 7 when rolling a pair of dice.
list1 = [1, 2, 3, 4, 5, 6]
list2 = [1, 2, 3, 4, 5, 6]
numberOfSevens = 0
for i in range(100000):
    if random.choice(list1) + random.choice(list2) == 7:
        numberOfSevens += 1
print(100 * numberOfSevens / 100000, '%')





          
