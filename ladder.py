import net
import random

class ladder:

    def __init__(self,):
        
        
        random.seed()
        print("Init ladder")
        
        
        self.nodeNum = 10
        self.conNum = 100
        self.agentNum = 10
        
        
        self.ratings = [0.0] * self.agentNum
        
        self.nets = []
        for i in range(self.agentNum):
            self.nets.append(net.net(self.nodeNum,self.conNum))
        
    #play nxn matches and adjust elo    
    def playTournament(self):
    
        for a in range(self.agentNum):
            for b in range(self.agentNum):
                if a != b:
                    self.playMatch(a,b)
                    
        for i in range(self.agentNum):
            self.nets[i].mutateNet()
            
    
    
    def playMatch(self, playerA,playerB):
        
        print("Initiating match: " , str(playerA) , "vs" , str(playerB))
        self.nets[playerA].reset()
        self.nets[playerA].setNode(0,1.0)
        
        self.nets[playerB].reset()
        self.nets[playerB].setNode(0,1.0)
        
        for it in range(10):
            self.nets[playerA].step()
            self.nets[playerB].step()
        
        if self.nets[playerA].getNode(2) > self.nets[playerB].getNode(2):
            print("Player A won")
            return playerA
        print("Player B won")
        return playerB
            
    
    
    
    
    
    def mutateNet(self):
        self.n.setCon(random.randrange(0,self.conNum),random.randrange(0,self.nodeNum),random.randrange(0,self.nodeNum),random.randrange(-10000,10000)/10000)