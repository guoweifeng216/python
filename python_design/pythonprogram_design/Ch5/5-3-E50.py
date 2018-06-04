topHitters = {"Gehrig":{"atBats":8061, "hits":2721},
              "Ruth":{"atBats":8399, "hits":2873},
              "Williams":{"atBats":7706, "hits":2654}}
hitList = []
for hitter in topHitters:
    hitList.append(topHitters[hitter]["hits"])
print("The most hits by one of the")
print("baseball players was ", max(hitList), '.', sep="")

