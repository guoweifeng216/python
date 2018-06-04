def main():
    ## Sort New England states by length of name.
    NE = [("Maine", 30840, 1.329), ("Vermont", 9217, .626),
          ("New Hampshire", 8953, 1.321), ("Massachusetts", 7800, 6.646),
          ("Connecticut", 4842, 3.59), ("Rhode Island", 1044, 1.05)]
    NE.sort(key=sortByLengthOfName)
    print("Sorted by length of name in ascending order:")
    for state in NE:
        print(state[0], " ", end="")
   
def sortByLengthOfName(state):
    return len(state[0])
    
main()
