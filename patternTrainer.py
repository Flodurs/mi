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









size = 100
inputNum = 3
outputNum = 2
conNum = 30
nodeNum = 10


d = darwin.darwin(size,nodeNum,conNum,5)



n = net.net(conNum,nodeNum)


pattern = [[0,0,1,1,1],[1,0,1,-1,1],[1,0,0,0,1],[1,1,1,1,-1,1],[-1,0,0,0,0]] 




def calcError(geno):
    
    n.setFromGenoType(d.getGenoType(geno))
    
    error = []
    for p in range(len(pattern)):    
        n.reset()
       
        for i in range(inputNum):
            n.setNode(i,pattern[p][i])
        for i in range(5):
            n.step()
            
        for i in range(1,outputNum+1):
            error.append((pattern[p][-i]-n.getNode(-i))**2)
    
    return mean(error)

for time in range(10000):
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
           
          
           
        for i in range(inputNum):
            n.setNode(i,pattern[p][i])
        for i in range(5):
            n.step()
                
        for i in range(1,outputNum+1):
            print(n.getNode(-i))
    


plt.show()



