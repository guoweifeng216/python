def sumList(L):
    if len(L) == 1:
        return L[0]
    else:
        return L[0] + sumList(L[1:])

        
        
