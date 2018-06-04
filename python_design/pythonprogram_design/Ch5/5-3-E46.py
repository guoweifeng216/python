def determineRank(years):
    rank = {1:"Freshman", 2:"Sophmore", 3:"Junior"}
    return rank.get(years, "Senior")
