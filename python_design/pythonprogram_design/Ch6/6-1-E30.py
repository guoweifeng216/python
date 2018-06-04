## Remove a requested state capital from a list of state capitals.
stateCapitals = ["Dover", "Springfield"]
while True:
    try:
        state = input("Enter a state capital to delete: ")
        stateCapitals.remove(state)
        print("Capital deleted.")
        break
    except ValueError:
        print("Not a state capital.")
     

