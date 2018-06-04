## Find states whose name and capital begin with the same letter.
infile = open("StatesANC.txt", 'r')
for line in infile:
    data = line.split(",")
    letter = data[0][0:1]
    if data[3].startswith(letter):
        print((data[3].rstrip()) + ",", data[0])
infile.close()        
      
    
    
