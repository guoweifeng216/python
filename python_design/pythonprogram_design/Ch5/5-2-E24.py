def main():
    ## Markdown the price of a saddle by 20% and 
    ## store the new price list into Cowboy2.txt.
    infile = open("Cowboy.txt", 'r')
    outfile = open("Cowboy2.txt", 'w')
    for line in infile:
        data = line.split(',')
        if data[0] == "Saddle":
            newPrice = round(0.8 * eval(data[1]), 2)
            outfile.write("Saddle," + str(newPrice) + "\n")
        else:
            outfile.write(line)
    outfile.close()
    infile.close()

main()                  
