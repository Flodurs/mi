import numpy as np
import random


class net:
    
    def __init__(self,nodeNum,conNum):
        print("Net init")
        random.seed()
        self.nodeNum = nodeNum
        self.nodes = [0.0]*nodeNum
        self.cons = [[0, 0, 0.0] for i in range(conNum)]
        self.conPointer = 0
        for c in range(conNum):
            self.setCon(c,random.randrange(0,self.nodeNum),random.randrange(0,self.nodeNum),random.randrange(-10000,10000)/10000)
        
    def setNode(self,i,value):
        #print("setNode")
        self.nodes[i]=value
        
    def reset(self):
        for n in range(len(self.nodes)):
            self.nodes[n] = 0.0
        
    def getNode(self,i):
        return self.nodes[i]
        
    def step(self):
        #print("step")
        
        nodeBuf = [0.0]*self.nodeNum
        #summing
        
        for a in range(len(self.cons)):
            nodeBuf[int(self.cons[a][1])]+=self.nodes[int(self.cons[a][0])]*self.cons[a][2]
            
        for a in range(len(self.nodes)):
            nodeBuf[a]=self.activationFunc(nodeBuf[a])
        
        for a in range(len(self.nodes)):
            self.nodes[a] = nodeBuf[a]
            
        #self.printNodes()
            
            
        
    def setCon(self,i,a,b,weight):
        #print("setCon")
        self.cons[i][0]=a
        self.cons[i][1]=b
        self.cons[i][2]=weight
        
        
    def activationFunc(self,x):
        return np.tanh(x)
        #return x
        
    def printCons(self):
        print("-----------------------")
        print(self.cons)
        print("-----------------------")
        
    def printNodes(self):
        print("----------------------\n")
        for x in range(self.nodeNum):
            print("Node " + str(x) + ":" +str(self.nodes[x]))
            
    def printNetHash(self):
        print("Hash: ",str(np.sum(self.cons)))
        
    def setFromGenoType(self, genoType):
        
        for i in range(len(self.cons)):
            # print("-----------------------")
            #print(genoType[i][0])
            self.cons[i][0]=genoType[i][0]
            self.cons[i][1]=genoType[i][1]
            self.cons[i][2]=genoType[i][2]
            # print(self.cons[i])
    
            

    

        
    
    
        
    