import numpy as np

class net:
    
    def __init__(self,nodeNum,conNum):
        print("Net init")
        self.nodeNum = nodeNum
        self.nodes = np.zeros(self.nodeNum, dtype = float)
        self.cons = np.zeros((conNum,3))
        self.conPointer = 0
        
        
    def setNode(self,i,value):
        #print("setNode")
        self.nodes[i]=value
        
    def reset(self):
        for n in self.nodes:
            n = 0.0
        
    def getNode(self,i):
        return self.nodes[i]
        
    def step(self):
        #print("step")
        
        nodeBuf = np.zeros(self.nodeNum, dtype = float)
        #summing
        
        for a in range(len(self.cons)):
            nodeBuf[int(self.cons[a,1])]+=self.nodes[int(self.cons[a,0])]*self.cons[a,2]
            
        for a in range(len(self.nodes)):
            nodeBuf[a]=self.activationFunc(nodeBuf[a])
        
        for a in range(len(self.nodes)):
            self.nodes[a] = nodeBuf[a]
            
        #self.printNodes()
            
            
        
    def setCon(self,i,a,b,weight):
        #print("setCon")
        self.cons[i,0]=a
        self.cons[i,1]=b
        self.cons[i,2]=weight
        
        
    def activationFunc(self,x):
        return np.tanh(x)
        # return x
        
    def printCons(self):
        print(self.cons)
        
    def printNodes(self):
        print("----------------------\n")
        for x in range(self.nodeNum):
            print("Node " + str(x) + ":" +str(self.nodes[x]))
            

    

        
    
    
        
    