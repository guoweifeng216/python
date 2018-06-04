import random

plays = ("rock", "paper", "scissors")
p1 = random.choice(plays)  # Player 1
p2 = random.choice(plays)  # Player 1
print("Player 1:", p1)
print("Player 2:", p2)
winner = ""
if ((p1 == "rock") and (p2 == "scissors") or
    (p1 == "paper") and (p2 == "rock") or
    (p1 == "scissors") and (p2 == "paper")):
    print("Player 1 wins.")
elif p1 == p2:
    print("TIE")
else:    
    print("Player 2 wins.")
