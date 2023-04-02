import random as r
data = list()
rnc = input("row and colomn :").split(" ")
rnc[1] = int(rnc[1])
rnc[0] = int(rnc[0])

for i in range(rnc[0]):
    list0 = list()
    for t in range(rnc[1]):
        rint = r.randint(0,9)
        list0.append(rint)
    data.append(list0)
for l in data:
    print(l)