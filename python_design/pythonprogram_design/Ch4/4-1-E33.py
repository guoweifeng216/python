colors = []

def main():
    ## Display colors beginning with a specified letter.
    letter = requestLetter()
    fillListWithColors(letter)
    displayColors()
    
def requestLetter():
    letter = input("Enter a letter: ")
    return letter.upper()

def fillListWithColors(letter):
    global colors
    infile = open("Colors.txt", 'r')
    for color in infile:
         if color.startswith(letter):
             colors.append(color.rstrip())
    infile.close()         

def displayColors():
    for color in colors:
        print(color)
    
main()
