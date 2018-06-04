## Insert name into file.
name = input("Enter name to be inserted into file: ")
infile = open("Names.txt", 'r')
setOfNames = {name for name in infile}
infile.close()
setOfNames.add(name + "\n")
listOfNames = list(setOfNames)
listOfNames.sort()
outfile = open("Names.txt", 'w')
outfile.writelines(listOfNames)
outfile.close()
