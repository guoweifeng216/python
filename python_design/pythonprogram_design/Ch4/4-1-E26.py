def howMany(s1, s2):
    ## Count the number of nonoverlapping occurrances of s2 in s1
    if s2 != "":
        n = 0   # number of nonoverlapping occurrances
        i = 0
        while i < len(s1):
            if s1[i:].startswith(s2):
                n += 1
                i = i + len(s2)
            else:
                i += 1     
        return n
    else:
        return len(s1) + 1

