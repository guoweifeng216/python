def main():
    ## Display justices from a specified state.
    state = input("Enter a state abbreviation: ")
    justices = getJusticesByState(state)
    fixCurrentJustices(justices)
    justices.sort(key=lambda justice: justice[5] - justice[4],
                  reverse=True)
    print("\n{0:18} {1:20}  {2}".format("Justice", "Appointing Pres",
                                        "Yrs Served"))
    for justice in justices:
        print("{0:18} {1:20}  {2}".format(justice[0] + " " + justice[1],
                    justice[2].split(" ")[-1], justice[5] - justice[4]))
        
def getJusticesByState(state):
    infile = open("Justices.txt", 'r')
    listOfRecords = [line for line in infile if line.split(',')[3] == state]
    infile.close()
    for i in range(len(listOfRecords)):
        listOfRecords[i] = listOfRecords[i].split(',')
        listOfRecords[i][4] = int(listOfRecords[i][4])
        listOfRecords[i][5] = int(listOfRecords[i][5])
    return listOfRecords

def fixCurrentJustices(justices):
    for justice in justices:
        if justice[5] == 0:
            justice[5] = 2015

main() 
