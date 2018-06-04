def main():
    ## Display Oscar-winning films of requested genre.
    # displayGenres()
    # displayFilms()
    disPlay()

def displayGenres():
    print("The different film genres are as follows:")
    print("{0:12}{1:12}{2:10}{3:11}{4:11}".
          format("adventure", "bioptic", "comedy", "crime", "drama"))
    print("{0:12}{1:12}{2:10}{3:11}{4:11}".
          format("epic", "fantasy", "musical", "romance", "silent"))
    print("{0:12}{1:12}{2:10}{3:11}".
          format("sports", "thriller", "war", "western"))
    print()

def displayFilms():    
    films = open("Oscars.txt",'r')
    genre = input("Enter a genre: ")
    print()
    print("The Academy Award winners are")
    for line in films:
        if line.endswith(genre + "\n"):
            temp = line.split(",")
            print("  " + temp[0])       
    films.close()



def disPlay():
    infiles=open("Oscars.txt",'r')

    filmsGene={line.split(',')[1] for line in infiles}
    filmsGene=list(filmsGene)
    filmsGene.sort()
    print(filmsGene)


main()