# _*_coding:utf-8_*_
def main():
    ## Determine day of week for a date.
    infile = open("Calendar2015.txt", 'r',encoding="utf-8")
    date = input("Enter a date in 2015: ")
    for line in infile:
        temp = line.split(',')
        print(temp)
        if temp[0] == date:
            print(date, "falls on a",  temp[1].rstrip())
            break

main()    
