def main():
    word = input("Enter a word: ")
    if isQwerty(word):
        print(word, "is a Qwerty word.")
    else:
        print(word, "is not a Qwerty word.")        

def isQwerty(word):
    word = word.upper()
    for ch in word:
        if ch not in "QWERTYUIOP":
            return False
    return True

main()
