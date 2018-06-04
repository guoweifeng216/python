NE={"CT":3.6,"ME":1.3,"MA":6.5,"NH":1.5,"RI":1.1,"VT":0.6}
print(NE["MA"])
print(len(NE))
print(list(NE))
print(list(NE.values()))
print(list(NE.items()))
print("NH" in NE)
print(NE.get("PA","absent"))
print(NE.get("RI","absent"))
print(max(NE))
print(min(NE))
print("***************************")
NE["ME"] +=.2
print(round(NE["ME"]))
del NE["ME"]
print(len(NE))
NE.update({"CT":3.7,"ME":2})
print(NE["ME"])
# NE.clear()
print(NE)
for x in NE.keys():
    print(x)

for x in sorted(NE):
    print(x)

total=0

for x in NE.values():
    total +=x
print("{0:.1f}".format(total))
total=0
for x in NE:
    total +=NE[x]
print("{0:.1f}".format(total))

new_england=NE
# del new_england["VT"]
print(len(NE))

new_england=dict(NE)
del new_england["VT"]
print(len(NE))