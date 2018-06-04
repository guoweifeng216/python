infile = open("USpres.txt")
presidents = infile.readlines()
firstName = input("Enter a first name: ")   
for pres in presidents:
    temp = pres.split()
    if temp[0] == firstName:
        print(pres, end="")
infile.close()
