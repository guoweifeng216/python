def main():
    ## Display line of Pascal's Triangle.
    n = int(input("Enter a nonnegative integer: "))
    line = [str(x) for x in pascal(n)]
    print("Row", str(n) + ':' ,"  ".join(line))

def pascal(n):
    # Display the nth line of Pascal's triangle.
    if n == 0:
        return [1]
    else:
        line = [1]
        previous_line = pascal(n-1)
        for i in range(len(previous_line)-1):
            line.append(previous_line[i] + previous_line[i+1])
        line += [1]
    return line

main()

