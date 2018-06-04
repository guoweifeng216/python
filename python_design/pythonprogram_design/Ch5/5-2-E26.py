def main():
    ## Add an article to the end of the file Cowboy.txt.
    outfile = open("Cowboy.txt", 'a')
    outfile.write("Winchester Rifle,20.50\n")
    outfile.close()

main()                  
