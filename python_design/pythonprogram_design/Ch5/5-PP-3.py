def main():
    ## Sort teams by percentage of games won.
    teams = placeRecordsIntoList("ALE.txt")
    teams.sort(key=lambda team: team[1]/team[2], reverse=True)
    createNewFile(teams)  # Create file of teams and their wins and losses.

def placeRecordsIntoList(fileName):
    infile = open(fileName, 'r')
    listOfRecords = [line.rstrip() for line in infile]
    infile.close()
    for i in range(len(listOfRecords)):
        listOfRecords[i] = listOfRecords[i].split(',')
        listOfRecords[i][1] = eval(listOfRecords[i][1])  # won
        listOfRecords[i][2] = eval(listOfRecords[i][2])  # lost
    return listOfRecords
       
def createNewFile(teams):
     outfile = open("OrderedALE.txt", 'w')
     for team in teams:
         outfile.write(team[0] + ',' + str(team[1]) + ',' +
                   str(team[2]) + ',' + str(round(team[1]/162, 3)) + "\n")
     outfile.close()    

main()
