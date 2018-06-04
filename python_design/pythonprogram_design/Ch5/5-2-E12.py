## Makeup of Supreme Court in January 2015
infile = open("Justices.txt", 'r')
justices = [line for line in infile if (int(line.split(',')[5]) == 0)]
justices.sort(key=lambda x: int(x.split(',')[4]))
print("Current Justices")
for justice in justices:
    print(justice.split(',')[0], justice.split(',')[1])
