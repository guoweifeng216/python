def main():
    ## Validate a ten-character ISBN number.
    isbn = input("Enter ten-character ISBN number: ")
    isbn = stripDashes(isbn)
    if checkFormat(isbn):
        if isValidISBN(isbn):
            print("The number is valid.")
        else:
            print("The number is not valid.")
    else:
        print("ISBN is not properly formatted.")

def stripDashes(isbn):
    noDashes = ""
    for ch in isbn:
        if ch != '-':
            noDashes += ch
    return noDashes        

def checkFormat(isbn):
    if (len(isbn) == 10) and isbn[:-1].isdigit() and \
       (isbn[-1].isdigit() or isbn[-1] == 'X'):
        return True
    else:
        return False
                 
def isValidISBN(isbn):
    L = list(isbn)
    if L[-1] == 'X':
        L[-1] = 10
    total = 0
    for i in range(10):
        total += (10 - i) * int(L[i]) 
    if total % 11:
        return False
    else:
        return True
    
main()
