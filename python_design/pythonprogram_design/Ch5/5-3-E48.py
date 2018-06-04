topHitters = {"Gehrig":{"atBats":8061, "hits":2721},
              "Ruth":{"atBats":8399, "hits":2873},
              "Williams":{"atBats":7706, "hits":2654}}
del topHitters[max(topHitters)]
del topHitters[min(topHitters)]
print(topHitters)
