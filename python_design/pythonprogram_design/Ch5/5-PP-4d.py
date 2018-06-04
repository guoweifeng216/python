def main():
    ## Identify senators from a specified state.
    state = input("Enter the name of a state: ")
    infile = open("Senate114.txt", 'r')
    for line in infile:
        if line.split(',')[1] == state:
            print(" ", line.split(',')[0])
            line2 = infile.readline()
            print(" ", line2.split(',')[0])
            break

main()
