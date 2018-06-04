import random

## Simulate a Powerball Drawing. 
whiteBalls = [num for num in range(1, 60)] 
# Randomly sample and display five white balls. 
whiteBallSelection = random.sample(whiteBalls, 5)
for i in range(5):
    whiteBallSelection[i] = str(whiteBallSelection[i])
print("White Balls:", " ".join(whiteBallSelection)) 
# Randomly select and display the Powerball.
powerBall = random.randint(1, 35)
print("Powerball:", powerBall)
