## Display data about a requested state.
state = input("Enter the name of a state: ")
infile = open("StatesANC.txt", 'r')
found = False
state_data = infile.readline()
while (found == False) and (state_data != ""):
    data = state_data.split(",")
    if data[0] == state:
        print("Abbreviation:", data[1])
        print("Nickname:", data[2])
        print("Capital:", data[3].rstrip())
        found = True
    state_data = infile.readline()
infile.close()    
