## Determine Oscar winning film for a given year.
films = open("Oscars.txt", 'r')
incorrect = True
while incorrect:
    year = int(input("Enter a year from 1928-2013: "))
    if (year >= 1928) and (year <= 2013):
        incorrect = False
        infile = open("Oscars.txt", 'r')
        flicks = [film.rstrip() for film in infile]
        infile.close()
        film = flicks[year - 1928]
        data = film.split(',')
        print("Best File:", data[0])
        print("Genre:", data[1])
        films.close()
    else:
        print("Year must be between 1928 and 2013.\n")
        incorrect = True
