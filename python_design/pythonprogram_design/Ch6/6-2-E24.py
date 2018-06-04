import random

numbers_used = []    # will prevent a number from being repeated
numbers_missed = []  # numbers of questions missed
infile = open("StatesANC.txt", 'r')
state_data = [line.rstrip() for line in infile]
infile.close()
# Get five different randomly selected numbers
for num in range(5):
    num = random.randint(0, 49)
    while num in numbers_used:
        num = random.randint(0, 49) 
    numbers_used.append(num)
    item = state_data[num].split(',')
    capital = input("What is the capital of " + item[0] + "? ")
    if capital != item[3]:
        numbers_missed.append(num)
# give score and corrections
print()
total_number_missed = len(numbers_missed)
if total_number_missed == 0:
    print("Congratulations. You answered every question correctly.")
else:
    if total_number_missed == 1:
        print("You missed 1 question.")
    else:          
        print("You missed", total_number_missed, "questions.")
    for number in numbers_missed:
        item = state_data[number].split(',')
        print(item[3], "is the capital of", item[0]) 
