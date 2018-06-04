def main():
     ## Determine if word has 3 consecutive letters in alphabetical order.
     word = input("Enter a word: ")
     word = word.upper()
     if isTripleConsecutive(word):
         print(word, "contains three successive letters")
     else:
         print(word, "does not contain three successive letters")
     print("in consecutive alphabetical order.")

def isTripleConsecutive(word):
    n = len(word)
    for i in range(n - 2):
        threeLetters = word[i:i+3]
        if (ord(threeLetters[0:1]) + 1 ==
            ord(threeLetters[1:2]) and
            ord(threeLetters[1:2]) + 1 ==
            ord(threeLetters[2:3])):
            return True
    return False
    
main()
