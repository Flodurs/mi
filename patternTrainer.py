import trainer

import os
import darwin
import net

from matplotlib import pyplot as plt
import matplotlib.animation as animation
from statistics import mean 


fbest = []




fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)









size = 20
d = darwin.darwin(size,10,20,5)



n = net.net(20,10)


pattern = [[0,0,1,1],[1,0,1,-1],[1,0,0,0]] #node 0-2 input node 4 output




def calcError(geno):
    
    n.setFromGenoType(d.getGenoType(geno))
    
    error = []
    for p in range(len(pattern)):    
        n.reset()
        n.setNode(0,pattern[p][0])
        n.setNode(1,pattern[p][1])
        n.setNode(2,pattern[p][2])
        for i in range(5):
            n.step()
        error.append((pattern[p][3]-n.getNode(4))**2)
    
    return mean(error)

for time in range(100000):
    if time%499 == 0:
        ax1.plot(fbest)
        plt.draw()
        plt.pause(0.001)
        print("All time lowest error: " +str(d.getAllTimeBestFit()))

    fl = []
    
    for j in range(size):
        fl.append(calcError(j))
        
        
     
        
        
    
   
    d.advanceGeneration(fl)
   
    fbest.append(min(fl))


#perform best

n.setFromGenoType(d.getAllTimeBest())

        
for p in range(len(pattern)):    
        print("Pattern " + str(p))
        print(pattern[p])
        n.reset()
        n.setNode(0,pattern[p][0])
        n.setNode(1,pattern[p][1])
        n.setNode(2,pattern[p][2])
        for i in range(5):
            n.step()
        print(n.getNode(4))


plt.show()



