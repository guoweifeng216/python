def main():
    ## Display colleges from requested state.
    colleges = getOrderedListOfColleges()
    displayListOfColleges(colleges)
    
def getOrderedListOfColleges():
    infile = open("Colleges.txt", 'r')
    colleges = [line.rstrip() for line in infile]
    infile.close()
    print(colleges)
    colleges.sort()
    print(colleges)
    return colleges

def displayListOfColleges(colleges):
    found = False
    abbrev = input("Enter a state abbreviation: ")
    for college in colleges:
        college = college.split(",")
        if college[1] == abbrev:
            print(college[0], college[2])
            found = True
    if not found:
        print("There are no early colleges from", abbrev + '.')
    
main()
