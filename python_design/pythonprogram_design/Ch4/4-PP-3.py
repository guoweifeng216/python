
def main():
    ## Verbalize a number.
    number = int(input("Enter a positive integer: "))
    describeNumber(number)

def describeNumber(number):
    number = "{0:,d}".format(number)
    descriptors = ["", "thousand", "million", "billion", "trillion",
               "quadrillion", "quintillion", "sextillion", "septillion"]
    numOfCommas = number.count(',')
    descriptors = descriptors[:numOfCommas + 1]
    loc = 3   # in case loop doesn't get entered; that is, no commas
    for i in range(numOfCommas, 0, -1):
        loc = number.find(',')
        front = number[:loc]
        front = front.strip('0')
        if front == "":
            front = '0'
        print("{0:>3} {1:s}".format(front, descriptors[i]))
        number = number[loc + 1:]
    front = number[:loc]
    front = front.strip('0')
    if front != "":
        print("{0:>3} {1:s}".format(front, descriptors[0]))

main()    
