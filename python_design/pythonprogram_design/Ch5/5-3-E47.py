def main():
    ## Display batting averages of top hitters.
    topHitters = {"Gehrig":{"atBats":8061, "hits":2721},
                  "Ruth":{"atBats":8399, "hits":2873},
                  "Williams":{"atBats":7706, "hits":2654}}
    displayBattingAverage(topHitters)
        
def displayBattingAverage(topHitters):
    for hitter in topHitters:
        print("{0:10} {1:.3f}".format(hitter,
               topHitters[hitter]["hits"] / topHitters[hitter]["atBats"]))

main()
