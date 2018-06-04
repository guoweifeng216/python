def main():
    ## Count the three affiliations.
    republicans = 0
    democrats = 0
    independents = 0
    infile = open("Senate114.txt", 'r')
    for line in infile:
        party = (line.split(','))[2]
        if party == 'R\n':
            republicans += 1
        elif party == 'D\n':
            democrats += 1
        else:
            independents += 1
    infile.close()        
    print("Party Affiliations:")
    print(" ", "Republicans:", republicans)
    print(" ", "Democrats:", democrats)  
    print(" ", "Independents:", independents)

main()
