import random

## Randomly select a perfect square integer from 1 to 10,000.
list1 = [n ** 2 for n in range(1, 101)]
x = random.choice(list1)
print(x)



          
