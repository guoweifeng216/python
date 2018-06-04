## Display cars sorted by average miles per gallon.
infile = open("Mileage.txt",'r')
data = [line.rstrip() for line in infile]
infile.close()
data = [s.split(',') for s in data]
cars = {}
# Place data into dictionary.
for line in data:
    model = line[0]
    gal = float(line[1])
    # if we haven't come across this model yet
    if not model in cars:
        cars[model] = (1, gal)
    # if we have come across this model before
    else:
        cars[model] = (cars[model][0] + 1, cars[model][1] + gal)
# Convert dictionary into list with average mpg.
lst = [[model, tup[0] * 100 / tup[1]] for (model, tup) in
                                            list(cars.items())]
print("Model\t  MPG")
for car in sorted(lst, key=lambda k: k[1], reverse=True):
    print("{0}\t  {1:.2f}".format(car[0], car[1]))

