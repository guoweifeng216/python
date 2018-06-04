def main():
    ## Determine whether two words are anagrams.
    string1 = input("Enter the first word or phrase: ")
    string2 = input("Enter the second word or phrase: ")
    if areAnagrams(string1, string2):
        print("Are anagrams.")
    else:
        print("Are not anagrams.")
          
def areAnagrams(string1, string2):
    firstString = string1.lower()
    secondString = string2.lower()
    # In the next two lines, the if clauses remove all
    # punctuation and spaces.
    letters1 = [ch for ch in firstString if 'a' <= ch <= 'z']
    letters2 = [ch for ch in secondString if 'a' <= ch <= 'z']
    letters1.sort()
    letters2.sort()
    return (letters1 == letters2)

main()

 



