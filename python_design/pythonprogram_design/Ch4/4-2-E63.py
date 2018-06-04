def main():
    ## Display presidents ordered by length of first name.
    infile = open("USPres.txt", 'r')
    listPres = [pres.rstrip() for pres in infile]
    infile.close()
    listPres.sort(key=sortByLengthOfFirstName)      
    for i in range(6):
        print(listPres[i])

def sortByLengthOfFirstName(pres):
    return len(pres.split()[0])

main()    
