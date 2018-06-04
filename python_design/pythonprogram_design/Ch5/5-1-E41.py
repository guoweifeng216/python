import os

## Delete colors having more than six characters.
infile = open("ShortColors.txt", 'r')
outfile = open("Temp.txt", 'w')
for color in infile:
    if len(color.rstrip()) <= 6:
        outfile.write(color)
infile.close()
outfile.close()
os.remove("ShortColors.txt")
os.rename("Temp.txt", "ShortColors.txt")
           
