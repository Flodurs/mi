import random
import copy
import statistics
import numpy as np
import os


class darwin:
    def __init__(self,genoTypeNum,conNum,nodeNum,oldGenoTypeNum):
        print("Init darwin")
        
        
        random.seed()
        self.genoTypeNum = genoTypeNum
        self.oldGenoTypeNum = oldGenoTypeNum
        self.conNum = conNum
        self.nodeNum = nodeNum
       
        
        #Bruh stacked * with lists doesnt do what i thought it does (only do it once)
        self.genoTypes = [ [[0, 0, 0.0] for i in range(conNum)] for x in range(genoTypeNum)]
        
        self.oldGenoTypes = [ [[0, 0, 0.0] for i in range(conNum)] for x in range(oldGenoTypeNum)]
        self.oldGenoTypePointer = 0;
        
        
        self.allTimeBest = [[0, 0, 0.0] for i in range(conNum)]
        self.allTimeBestFit = 9999
        
        self.generation = 0
        
        self.firstWindowFlag = 0
        
        
        self.randomizeGenoTypes()
        
        import os
        if os.path.exists("D:/Dev/miVis/public/matches.html"):
            os.remove("D:/Dev/miVis/public/matches.html")
        
        
        
        
    def storeOldGenoType(self,genoTypeIndex):
        for j in range(self.conNum):
            self.oldGenoTypes[self.oldGenoTypePointer][j][0]=self.genoTypes[genoTypeIndex][j][0]
            self.oldGenoTypes[self.oldGenoTypePointer][j][1]=self.genoTypes[genoTypeIndex][j][1]
            self.oldGenoTypes[self.oldGenoTypePointer][j][2]=self.genoTypes[genoTypeIndex][j][2]
            
        self.oldGenoTypePointer+=1
        if self.oldGenoTypePointer >= self.oldGenoTypeNum:
            self.firstWindowFlag = 1
            self.oldGenoTypePointer = 0
        
        
    def insertOldGenoTypeIntoPop(self,targetGenoTypeIndex):
        randomOldIndex = 0;
        if self.firstWindowFlag == 1:
            randomOldIndex = random.randrange(0,self.oldGenoTypeNum)
        else:
            if self.oldGenoTypePointer != 0:
                randomOldIndex = random.randrange(0,self.oldGenoTypePointer)
       
        for j in range(self.conNum):
            self.genoTypes[targetGenoTypeIndex][j][0]=self.oldGenoTypes[randomOldIndex][j][0]
            self.genoTypes[targetGenoTypeIndex][j][1]=self.oldGenoTypes[randomOldIndex][j][1]
            self.genoTypes[targetGenoTypeIndex][j][2]=self.oldGenoTypes[randomOldIndex][j][2]
    
    
        
    def getAllTimeBest(self):
        return self.allTimeBest
        
    def getAllTimeBestFit(self):
        return self.allTimeBestFit
    
    def printGenePool(self):
        print("-----------------------")
        for i in range(self.genoTypeNum):
            print(self.genoTypes[i])
        print("-----------------------")

    def setGenoType(self,genoTypeIndex,genoType):
        self.genoTypes[genoTypeIndex] = genoType
        
    def getGenoType(self,genoTypeIndex):
        return self.genoTypes[genoTypeIndex]
        
    def randomizeGenoTypes(self):
        for i in range(self.genoTypeNum):
            
            for j in range(self.conNum):
                #print(str(i), " : ",str(j))
                self.genoTypes[i][j][0]=random.randrange(0,self.nodeNum)
                self.genoTypes[i][j][1]=random.randrange(0,self.nodeNum)
                self.genoTypes[i][j][2]=random.randrange(-10000,10000)/5000
                
                #print(self.genoTypes[i])
        
    def mutateGenoType(self,genoTypeIndex,mutationRate):
        
        while random.randrange(0,1000) < mutationRate:
            index = random.randrange(0,self.conNum)
            if random.randrange(0,3)==1:
                self.genoTypes[genoTypeIndex][index][0]=random.randrange(0,self.nodeNum)
                self.genoTypes[genoTypeIndex][index][1]=random.randrange(0,self.nodeNum)
            self.genoTypes[genoTypeIndex][index][2]+=random.randrange(-1000,1000)/5000
        
        
    def randomCrossover(self):
        pass
        
    def advanceGeneration(self,fitnessList):
        
        self.generation += 1
        
        
        #calc average Fitness
        meanFit = statistics.mean(fitnessList)
        print(meanFit)
        
        
        
        
        
        
     
        maxFit = max(fitnessList)
        
        indicesSort = np.argsort(fitnessList)
        
        
        
        
        
      
        
       
        
        
        if self.generation%5 == 0:
            self.storeOldGenoType(indicesSort[-1])
        
        
        
        #split   
        for i in range(10):
            for j in range(self.conNum):
                self.genoTypes[indicesSort[i]][j][0]=self.genoTypes[indicesSort[-(i+1)]][j][0]
                self.genoTypes[indicesSort[i]][j][1]=self.genoTypes[indicesSort[-(i+1)]][j][1]
                self.genoTypes[indicesSort[i]][j][2]=self.genoTypes[indicesSort[-(i+1)]][j][2]
        #mutate    
        for i in range(self.genoTypeNum):
            self.mutateGenoType(i,700)    
        
        #insert old genotypes
        for i in range(10):
            self.insertOldGenoTypeIntoPop(indicesSort[10+i])
        
            
        
        
       
        
        