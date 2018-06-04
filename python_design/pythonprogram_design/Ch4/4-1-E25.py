def maximum(list1):
    largestNumber = list1[0]
    for number in list1:
        if number > largestNumber:
            largestNumber = number
    return largestNumber
