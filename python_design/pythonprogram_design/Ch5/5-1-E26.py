def findItemsinBoth(list1, list2)
    s = set(list1).intersection(set(list2))
    return list(s)
