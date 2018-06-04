import random

## Randomly select two even numbers from 2 through 100.
# Create a list of the even numbers from 2 through 100.
list1 = [n for n in range(2, 101, 2)]
# Select two of the even numbers at random.
list2 = random.sample(list1, 2)
# Display the two numbers.
print(list2[0], list2[1])
