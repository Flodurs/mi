import darwin
from matplotlib import pyplot as plt
d = darwin.darwin(50,5,5)
foft = []
fbest = []
for x in range(999):
    fl = []
    for i in range(50):
        fl.append(d.getGenoType(i)[0][2])
    d.advanceGeneration(fl)
    #print(fl)
    foft.append(fl)
    
for i in foft:
    fbest.append(max(i))

print(foft)
plt.plot(fbest)
plt.show()