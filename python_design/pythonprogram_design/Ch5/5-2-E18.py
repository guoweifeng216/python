def main():
    ## Determine the last college founded in a given state before 1800.
    abbrev = input("Enter a state abbreviation: ")
    colleges = getOrderedListOfColleges(abbrev)
    displayResult(colleges, abbrev)

def getOrderedListOfColleges(abbrev):
    # Colleges will be ordered by date founded.
    infile = open("Colleges.txt", 'r')
    colleges = [line for line in infile if line.split(',')[1] == abbrev]
    colleges.sort(key=lambda x: int(x.split(',')[2]))
    return colleges

def displayResult(colleges, abbrev):
    if len(colleges) > 0:
        print("Last college in", abbrev, "founded before 1800:")
        print(colleges[-1].split(',')[0])
    else:
        print(abbrev, "had no colleges before 1800.")
              
main()
