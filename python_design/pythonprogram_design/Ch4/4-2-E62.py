def main():
    ## Sort U.S. presidents alphabetically by last name.
    infile = open("USpres.txt", 'r')
    listPres = [pres.rstrip() for pres in infile]
    infile.close()
    listPres.sort(key=sortByLastName)      
    for i in range(6):
        print(listPres[i])

def sortByLastName(pres):
    return pres.split()[-1]

main()    
