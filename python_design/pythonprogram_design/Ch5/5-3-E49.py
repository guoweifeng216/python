def main():
    ## Display average number of hits by the top three hitters.
    topHitters = {"Gehrig":{"atBats":8061, "hits":2721},
                  "Ruth":{"atBats":8399, "hits":2873},
                  "Williams":{"atBats":7706, "hits":2654}}
    displayAveNumberOfHits(topHitters)

def displayAveNumberOfHits(topHitters):
    hitList = []
    for hitter in topHitters:
        hitList.append(topHitters[hitter]["hits"])
    value = "{0:.1f}".format(sum(hitList) / len(hitList))   
    print("The average number of hits by")
    print("the baseball players was", value + '.')

main()
