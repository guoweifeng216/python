def main():
    ## Calculate the original cost of mailing an airmail letter.
    weight = float(input("Enter the number of ounces: "))
    print("Cost: ${0:0,.2f}".format(cost(weight)))

def cost(weight):
    return 0.05 + 0.1 * ceil(weight - 1)

def ceil(x):
    if int(x) != x:
        return int(x + 1)
    else:
        return x

main()
