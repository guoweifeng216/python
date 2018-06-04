def main():
    ## Calculate letter frequencies for a sentence.
    sentence = input("Enter a sentence: ")
    sentence = sentence.upper()
    letterDict = dict([(chr(n),0) for n in range(65, 91)]) 
    for char in sentence:
        if 'A' <= char <= 'Z':
            letterDict[char] += 1
    displaySortedResults(letterDict)      
             
def displaySortedResults(dictionaryName):
    letterList = list(dictionaryName.items())
    letterList.sort(key=f, reverse=True)
    for x in letterList:
        if x[1] != 0:
            print("  " + x[0] + ':', x[1])
            
def f(k):
    return k[1]

main()
