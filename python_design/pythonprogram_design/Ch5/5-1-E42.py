import os

def main():
    ## Delete states that do not begin with a vowel.
    infile = open("SomeStates.txt", 'r')
    outfile = open("Temp.txt", 'w')
    for state in infile:
        if state[:1]  in "AEIOU":
            outfile.write(state)
    infile.close()
    outfile.close()
    os.remove("SomeStates.txt")
    os.rename("Temp.txt", "SomeStates.txt")
  
main()
