def main():
    ## Makeup of Supreme Court in 1980.
    infile = open("Justices.txt", 'r')
    justices = [line for line in infile
                if (int(line.split(',')[4]) < 1980)
                and (int(line.split(',')[5]) >= 1980)]
    justices.sort(key = lambda x: int(x.split(',')[4]))
    print("{0:20} {1}".format("Justice", "Appointing President"))
    for justice in justices:
        print("{0:20} {1}".format(justice.split(',')[0] + " " +
        justice.split(',')[1], justice.split(',')[2]))

main()        
   
list=[line for line in infile if line.split(',')[3]==input_status]
for i in range(len(list)):
    list[i][4]=eval(list[i][4])
    list[i][5] = eval(list[i][5])
list.sort(lambda list:list[5]-list[4],reverse=True)