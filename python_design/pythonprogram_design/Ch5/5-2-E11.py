def main():
    ##Display justices appointed by a given president.
    president = input("Enter the name of a president: ")
    justices = getJusticesByPresident(president)
    print(justices)
    fixCurrentJustices(justices)
    justices.sort(key=lambda justice: justice[5] - justice[4], reverse=True)
    print(justices)
    if len(justices) > 0:
        print("Justices Appointed:")
        for justice in justices:
            print("  " + justice[0] + " " + justice[1])
    else:
        print(president, "did not appoint any justices.")
   
def getJusticesByPresident(president):
    infile = open("Justices.txt", 'r')
    listOfRecords = [line for line in infile
                     if line.split(',')[2] == president]
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
