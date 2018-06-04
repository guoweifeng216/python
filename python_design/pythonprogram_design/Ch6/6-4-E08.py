def displaySequenceOfNumbers2(m, n):
    ## Display the numbers from m to n, where m <= n.
    if m <= n:
        print(m)
        displaySequenceOfNumbers2(m + 1, n) 

displaySequenceOfNumbers2(4,8)
