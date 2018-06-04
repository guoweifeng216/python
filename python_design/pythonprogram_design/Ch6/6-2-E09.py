import random

## Select three uppercase letters at random from the alphabet.
# Create a list of the 26 uppercase letters of the alphabet.
list1 = [chr(n) for n in range(ord('A'), ord('Z') + 1)]
# Select three letters at random.
list2 = random.sample(list1, 3)
# Display the three letters
print(", ".join(list2))




          
