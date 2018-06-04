def main():
    ## Sort states by number of vowels in descending order.
    infile = open("States.txt", 'r')
    listStates = [state.rstrip() for state in infile]
    infile.close()
    listStates.sort(key=numberOfVowels, reverse=True)      
    for i in range(6):
        print(listStates[i])

def numberOfVowels(word):
    vowels = ('a', 'e', 'i', 'o', 'u')
    total = 0
    for vowel in vowels:
        total += word.lower().count(vowel)
    return total

main()
 
