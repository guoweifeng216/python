def factor(n):
    ## Return a list containing the prime factors of n.
    if n==1:
        return []
    b = 2
    while b <= n:
        while not n % b:
            return [b] + factor(n // b)
        b += 1

