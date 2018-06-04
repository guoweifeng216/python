import random

numberOfTries = 1
n = random.randint(1, 100)
print("\nI've thought of a number from 1 through 100.")
while True:
    try:
        guess = int(input("Guess the number: "))
        break
    except ValueError:
        numberOfTries += 1
        print("You did not enter a number.")
while guess != n:
    numberOfTries += 1
    if (guess > 100) or (guess < 1):
        print("Number must be from 1 through 100.")
    elif guess > n:
        print("Too high")
    elif guess < n:
        print("Too low")
    while True:
        try:
           guess = int(input("Try again: "))
           break
        except ValueError:
           numberOfTries += 1
           print("You did not enter a number.")
print("Correct.", end=" ")
if numberOfTries == 1:
    print("You got it in one guess.")
else:
    print("You took", numberOfTries, "guesses.")
    
