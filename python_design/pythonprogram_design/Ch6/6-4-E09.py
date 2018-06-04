def main():
    n = int(input("Enter a positive integer: "))
    for r in range(0, n + 1):
        print(C(n, r), end="  ")

def C(n, r):
    if (n == 0) or (r == 0) or (n == r):
        return 1
    else:
        return C(n - 1, r - 1) + C(n - 1, r)

main()    
        
    

      

