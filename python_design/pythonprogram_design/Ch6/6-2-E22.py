import random

## Think of the cards as being numbered 1 through 52.
cards = [n for n in range(1, 53)]
total = 0
for i in range(100000):
    aceLocations = random.sample(cards, 4)
    n = min(aceLocations)
    total += n
print("The average number of cards \nturned up was {0:.2f}".
      format(total / 100000))

    



