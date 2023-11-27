import net
import random
import copy
import tic

class ladder:

    def __init__(self,):
        
        
        random.seed()
        print("Init ladder")
        
        
        
        
        self.nodeNum = 60
        self.conNum = 100
        self.agentNum = 10
        
        
        self.ratings = [0.0] * self.agentNum
        
        self.nets = []
        for i in range(self.agentNum):
            self.nets.append(net.net(self.nodeNum,self.conNum))
        
    #play nxn matches and adjust elo    
    def playTournament(self):
        self.ratings = [0.0] * self.agentNum
        for a in range(self.agentNum):
            for b in range(self.agentNum):
                if a != b:
                    if self.playMatch(a,b) == a:
                        self.ratings[a]+=0.2
                        # self.ratings[b]-=0.1
                    else:
                        self.ratings[b]+=0.2
                        # self.ratings[a]-=0.1
                    
        
            
        #print(self.ratings)
        
        
    
    def playMatch(self, playerA,playerB):
        
        #print("Initiating match: " , str(playerA) , "vs" , str(playerB))
        self.nets[playerA].reset()
        self.nets[playerB].reset()
        t = tic.tic()
        while 1:
            #Player A
            #put pos into net
            pos =  t.getBoard()
            out=[]
            for x in range(len(t.getBoard())):
                self.nets[playerA].setNode(x,pos[x]/2)
            
            
            #step
            for x in range(20):
                self.nets[playerA].step()
                
            #retrieve output 
            for x in range(len(t.getBoard())):
                out.append(self.nets[playerA].getNode(x))
                
            move = out.index(max(out))
            result = t.move(move) 
            if result == 1:
                return playerA
            if result == 2:
                return playerB
            if result == -1:
                return playerB
            
            #---------------------------------------------------------------
            #Player B
            #put pos into net
            print("BBBBBBB")
            pos =  t.getBoard()
            out=[]
            for x in range(len(t.getBoard())):
                self.nets[playerB].setNode(x,pos[x]/2)
            
            
            #step
            for x in range(20):
                self.nets[playerB].step()
                
            #retrieve output 
            for x in range(len(t.getBoard())):
                out.append(self.nets[playerB].getNode(x))
                
            move = out.index(max(out))
            result = t.move(move)
            if result == 1:
                return playerA
            if result == 2:
                return playerB
            if result == -1:
                return playerA
        
    def spreadTheWisdom(self):
        bestAgentIndex = self.ratings.index(max(self.ratings))
        bestAgent = copy.deepcopy(self.nets[bestAgentIndex])
        
        
        #print("Top Agent: ", str(bestAgentIndex), " score: ",str(max(self.ratings)) )
        for i in range(self.agentNum):
            self.nets[i]=copy.deepcopy(bestAgent)
        
        for i in range(self.agentNum-1):
            for j in range(1):
                self.mutateNet(i)
            
    
    
    def mutateNet(self,net):
        self.nets[net].setCon(random.randrange(0,self.conNum),random.randrange(0,self.nodeNum),random.randrange(0,self.nodeNum),random.randrange(-10000,10000)/10000)