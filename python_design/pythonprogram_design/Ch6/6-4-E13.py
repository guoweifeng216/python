def main():
    ## Reverse the order of items entered by the user.
    state = ""
    getState(state)

def getState(state):
    state = input("Enter a state: ")
    if state != "End":
        getState(state)
        print(state)

main()
      

