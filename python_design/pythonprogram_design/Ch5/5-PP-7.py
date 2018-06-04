def main():
    cities = placeRecordsIntoList("Cities.txt")
    # Sort list by percentage population growth.
    cities.sort(key=lambda city: (city[3] - city[2])/city[2], reverse=True)
    createNewFile(cities)  # Create file of cities and their % growth.

def placeRecordsIntoList(fileName):
    infile = open(fileName, 'r')
    listOfRecords = [line.rstrip() for line in infile]
    infile.close()
    for i in range(len(listOfRecords)):
        listOfRecords[i] = listOfRecords[i].split(',')
        listOfRecords[i][2] = eval(listOfRecords[i][2])  # population in 2000
        listOfRecords[i][3] = eval(listOfRecords[i][3])  # population in 2010
    return listOfRecords
       
def createNewFile(cities):
     outfile = open("OrderedCities.txt", 'w')
     for city in cities:
         outfile.write(city[0] + ',' +
                   str(round(100*((city[3] - city[2])/city[2]),1)) + "\n")
     outfile.close()    

main()
