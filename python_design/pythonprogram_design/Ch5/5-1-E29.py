## Count the words in the Gettysburg Address.
infile = open("Gettysburg.txt")
originalLine = infile.readline()
originalLine1=[line.split() for line in originalLine]
infile.close()
print(originalLine1)
print(originalLine[:89])
originalLine = originalLine.lower()
# Remove punctuation marks from the original line.
line = ""
for ch in originalLine:
    if ('a' <= ch <= 'z') or (ch == " "):
        line += ch
# Place the words into a list.
listOfWords = line.split()
# Form a set of the words without duplications.
setOfWords = set(listOfWords)
print("The Gettysburg Address contains", len(listOfWords), "words.")
print("The Gettysburg Address contains", len(setOfWords),
      "different words.")
