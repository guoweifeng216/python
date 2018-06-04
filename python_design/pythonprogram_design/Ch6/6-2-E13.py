import random

## Count the number of "Heads" in 100 coin tosses.
numberOfHeads = 0
for i in range(100):
    if (random.choice(["Head","Tail"]) == "Head"):
        numberOfHeads += 1
print("In 100 tosses, Heads occurred {0} times.".format(numberOfHeads))
