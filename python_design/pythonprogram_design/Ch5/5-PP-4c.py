def main():
    ## Determine number of states having both senators from the same party.
    sameParty = 0
    infile = open("Senate114.txt", 'r')
    for i in range(25):
        line1 = infile.readline()
        line2 = infile.readline()
        if line1.split(',')[2] == line2.split(',')[2]:
            sameParty += 1
    print("In", sameParty, "states both senators ")
    print("are from the same party.")

main()
