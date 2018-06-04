import random

## Simulate 32 coin tosses and check for runs of length five. 
coin = ['T', 'H'] 
result = "" 
for i in range(32): 
    result += random.choice(coin) 
print(result) 
if ("TTTTT" in result) or ("HHHHH" in result): 
    print("There was a run of five consecutive") 
    print("same outcomes.") 
else: 
    print("There was not a run of five consecutive") 
    print("same outcomes.") 
