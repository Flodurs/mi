import random
import copy


class darwin:
    def __init__(self,genoTypeNum,conNum,oldGenoTypesNum):
        print("Init darwin")
        
        
        random.seed()
        self.genoTypeNum = genoTypeNum
        self.conNum = conNum
       
        
        #Bruh stacked * with lists doesnt do what i thought it does (only do it once)
        self.genoTypes = [ [[0, 0.0, 0.0] for i in range(conNum)] for x in range(genoTypeNum)]
        
        self.oldGenoTypes = [[[[0, 0.0, 0.0]]*conNum]*genoTypeNum]*oldGenoTypesNum
        
        
        
        
        
        
        self.randomizeGenoTypes()
        
        
        
        
    
    def printGenePool(self):
        print("-----------------------")
        print(self.genoTypes)
        print("-----------------------")

    def setGenoType(self,genoTypeIndex,genoType):
        self.genoTypes[genoTypeIndex] = genoType
        
    def getGenoType(self,genoTypeIndex):
        return self.genoTypes[genoTypeIndex]
        
    def randomizeGenoTypes(self):
        for i in range(self.genoTypeNum):
            
            for j in range(self.conNum):
                #print(str(i), " : ",str(j))
                self.genoTypes[i][j][0]=random.randrange(0,self.conNum)
                self.genoTypes[i][j][0]=random.randrange(0,self.conNum)
                self.genoTypes[i][j][2]=random.randrange(-10000,10000)/5000
                
                #print(self.genoTypes[i])
        
    def mutateGenoType(self,genoTypeIndex):
        index = random.randrange(0,self.conNum)
        self.genoTypes[genoTypeIndex][index][0]=random.randrange(0,self.conNum)
        self.genoTypes[genoTypeIndex][index][1]=random.randrange(0,self.conNum)
        self.genoTypes[genoTypeIndex][index][2]=random.randrange(-10000,10000)/5000
        
        
    def randomCrossover(self):
        pass
        
    def advanceGeneration(self,fitnessList):
        #take n top performers, mutate them and replace current gene Pool with them
        #I1: Leave one unmutated
        
        #calc top performers
        topIndex = fitnessList.index(max(fitnessList))
        
        
       
        for i in range(self.genoTypeNum):
            self.genoTypes[i]=copy.deepcopy(self.genoTypes[topIndex])
            self.mutateGenoType(i)
        
        
        
        