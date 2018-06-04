def main():
    ## Determine all the permutations of a word.
    w = input("Enter a word: ")
    print("  ".join(permutations(w)))
    
def permutations(w):
   # Construct a list consisting of all permutations of the string s 
   if len(w) == 1:
       return w
   listOfPermuations = []         # resulting list
   for i in range(len(w)):
       restOfw = w[:i] + w[i+1:]  # w with ith character removed
       z = permutations(restOfw)  # permutations of remaining characters
       for t in z:
           listOfPermuations.append(w[i] + t)
   return listOfPermuations

main()
