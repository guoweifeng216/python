def main():
    ## Create receipt
    createOrderFile()
    total = 0
    infile1 = open("Cowboy.txt", 'r')
    infile2 = open("Order.txt", 'r')
    for line in infile1:
        quantity = int(infile2.readline())
        cost = quantity * float(line.split(',')[1])
        print("{0} {1}: ${2:,.2f}".format(quantity, line.split(',')[0], cost))
        total += cost
    print("{0}: ${1:,.2f}".format("TOTAL", total))

def createOrderFile():
    orders = ["3\n", "2\n", "10\n", "1\n", "4\n"]
    outfile = open("Order.txt", 'w')
    outfile.writelines(orders)
    outfile.close()

main()
