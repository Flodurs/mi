import net
import random

class trainer:
    def __init__(self):
        print("Trainer init")
        
        self.nodeNum = 10
        self.conNum = 100
        
        self.n = net.net(self.nodeNum,self.conNum)
        
        
        random.seed()
        
        
        
    def randomizeCons(self):
        print("Randomizing cons")
        for x in range(self.conNum):
            self.n.setCon(x,random.randrange(0,self.nodeNum),random.randrange(0,self.nodeNum),random.randrange(-10000,10000)/10000)
    
    def setInput(self,i,value):
        self.n.setNode(i,value)
        
    def viewSim(self,stepNum):
        for x in range(stepNum):
            self.n.step()
            
    def viewNet(self):
        self.n.printCons()
        
    def mutateNet(self):
        self.n.setCon(random.randrange(0,self.conNum),random.randrange(0,self.nodeNum),random.randrange(0,self.nodeNum),random.randrange(-10000,10000)/10000)
        
        
    def trainPattern(self,steps):
        for x in range(steps):
            #reset net
            for a in range(self.nodeNum):
                self.n.setNode(a,0)
                
            self.n.setNode(0,1)
            
            # sim net
            for x in range(3):
                self.n.step()
                
            if self.n.getNode(2) > 0.5 and self.n.getNode(2) < 0.6 and self.n.getNode(8) > 0.8:
                print("Success")
                break
                
            self.mutateNet()
        
        