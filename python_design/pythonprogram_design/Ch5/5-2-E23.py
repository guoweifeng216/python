def main():
    ## Create file of articles purchased by cowboys.
    articles = ["Colt Peacemaker,12.20\n", "Holster,2.00\n",
        "Levi Strauss jeans,1.35\n", "Saddle,40.00\n", "Stetson,10.00\n"]
    outfile = open("Cowboy.txt", 'w')
    outfile.writelines(articles)
    outfile.close()            
            
main()            

