import random
import copy
import statistics
import numpy as np

class darwin:
    def __init__(self,genoTypeNum,conNum,nodeNum,oldGenoTypeNum):
        print("Init darwin")
        
        
        random.seed()
        self.genoTypeNum = genoTypeNum
        self.conNum = conNum
        self.nodeNum = nodeNum
       
        
        #Bruh stacked * with lists doesnt do what i thought it does (only do it once)
        self.genoTypes = [ [[0, 0, 0.0] for i in range(conNum)] for x in range(genoTypeNum)]
        
        self.oldGenoTypes = [ [[0, 0, 0.0] for i in range(conNum)] for x in range(oldGenoTypeNum)]
        self.oldGenoTypePointer = 0;
        
        
        self.allTimeBest = [[0, 0, 0.0] for i in range(conNum)]
        self.allTimeBestFit = 9999
        
        
        self.randomizeGenoTypes()
        
    def storeOldGenoType(genoTypeIndex):
        pass
        
    def insertOldGenoTypesIntoPop(amount,location):
        pass
    
    
        
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
        #take n top performers, mutate them and replace current gene Pool with them
        #I1: Leave one unmutated
        
        #calc top performers
        
        
        #calc average Fitness
        meanFit = statistics.mean(fitnessList)
        print(meanFit)
        
        
        
        
        
        
        topIndex = fitnessList.index(max(fitnessList))
        maxFit = max(fitnessList)
        
        indicesSort = np.argsort(fitnessList)
        
        
        
        
        
        # print("-----------------\nAG:")
        # print(topIndex)
        # print(fitnessList)
        
        #store all time best
        if min(fitnessList) < self.allTimeBestFit :
            self.allTimeBestFit = min(fitnessList)
            for j in range(self.conNum):
                self.allTimeBest[j][0]=self.genoTypes[topIndex][j][0]
                self.allTimeBest[j][1]=self.genoTypes[topIndex][j][1]
                self.allTimeBest[j][2]=self.genoTypes[topIndex][j][2]
        
        
        
        
            
        for i in range(6):
            for j in range(self.conNum):
                self.genoTypes[indicesSort[i]][j][0]=self.genoTypes[indicesSort[-(i+1)]][j][0]
                self.genoTypes[indicesSort[i]][j][1]=self.genoTypes[indicesSort[-(i+1)]][j][1]
                self.genoTypes[indicesSort[i]][j][2]=self.genoTypes[indicesSort[-(i+1)]][j][2]
            
        for i in range(self.genoTypeNum):
            self.mutateGenoType(i,900)    
            
        
        
       
        
        