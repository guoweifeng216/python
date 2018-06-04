def findItemsInEither(list1, list2):
    set1 = set(list1).union(list2)
    return list(set1)
