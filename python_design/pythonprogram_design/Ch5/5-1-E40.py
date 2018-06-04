import os

def main():
    ## Delete months that do not contain the letter r.
    infile = open("SomeMonths.txt", 'r')
    outfile = open("Temp.txt", 'w')
    for month in infile:
        if 'r' in month.lower():
            outfile.write(month)
    infile.close()
    outfile.close()
    os.remove("SomeMonths.txt")
    os.rename("Temp.txt", "SomeMonths.txt")
  
main()

            
        
