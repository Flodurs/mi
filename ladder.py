import net
import random
import copy
import tic

class ladder:

    def __init__(self,):
        
        
        random.seed()
        print("Init ladder")
        
        
        self.gen = 0
        
        
        self.nodeNum = 30
        self.conNum = 100
        self.agentNum = 20
        
        
        self.ratings = [0.0] * self.agentNum
        
        self.nets = []
        for i in range(self.agentNum):
            self.nets.append(net.net(self.nodeNum,self.conNum))
            
            
        self.movesPlayed = 0
        self.matchesPlayed = 0
        
    #play nxn matches and adjust elo    
    def playTournament(self):
        self.gen+=1
        if self.matchesPlayed != 0:
            print("Avg Moves per Game: ", str(self.movesPlayed/self.matchesPlayed))
        self.movesPlayed = 0
        self.matchesPlayed = 0
        print("Generation: ", self.gen,"-----------------------------------------------------------------")
        self.ratings = [0.0] * self.agentNum
        
        for a in range(self.agentNum):
            
            for b in range(self.agentNum):
                if a != b:
                    self.matchesPlayed+=1
                    result = self.playMatch(a,b)
                    self.movesPlayed+=result[0]
                    if result[1] == a:
                        self.ratings[a]+=1
                        # self.ratings[b]-=0.1
                        # print(" A won")
                    else:
                        self.ratings[b]+=1
                        # print(" B won")
                        # self.ratings[a]-=0.1
                    
        
            
        #print(self.ratings)
        # for n in range(self.agentNum):
            # self.nets[n].printNetHash()
        
        
    
    def playMatch(self, playerA,playerB):
        
        # print("Initiating match: " , str(playerA) , "vs" , str(playerB))
        
        t = tic.tic()
        while 1:
            self.nets[playerA].reset()
            self.nets[playerB].reset()
            # print("AAAAAAAA")
            #Player A
            #put pos into net
            pos =  t.getBoard()
            out=[]
            for x in range(len(t.getBoard())):
                self.nets[playerA].setNode(x+10,pos[x]/2)
            
            
            #step
            for x in range(20):
                self.nets[playerA].step()
                
            #retrieve output 
            for x in range(len(t.getBoard())):
                out.append(self.nets[playerA].getNode(x))
                
            move = out.index(max(out))
           
            result = t.move(move) 
            # print("Result: ", str(result))
            if result == 1:
                return t.getMoveCount(),playerA
            if result == 2:
                return t.getMoveCount(),playerB
            if result == -1:
                return t.getMoveCount(),playerB
            
            #---------------------------------------------------------------
            #Player B
            #put pos into net
            # print("BBBBBBB")
            pos =  t.getBoard()
            out=[]
            for x in range(len(t.getBoard())):
                self.nets[playerB].setNode(x+10,pos[x]/2)
            
            
            #step
            for x in range(20):
                self.nets[playerB].step()
                
            #retrieve output 
            for x in range(len(t.getBoard())):
                out.append(self.nets[playerB].getNode(x))
                
            move = out.index(max(out))
            
            result = t.move(move)
            if result == 1:
                return t.getMoveCount(),playerA
            if result == 2:
                return t.getMoveCount(),playerB
            if result == -1:
                return t.getMoveCount(),playerA
        
    def spreadTheWisdom(self):
        bestAgentIndex = self.ratings.index(max(self.ratings))
        bestAgent = copy.deepcopy(self.nets[bestAgentIndex])
        
        
        print("Top Agent: ", str(bestAgentIndex), " score: ",str(max(self.ratings)) )
        for i in range(self.agentNum):
            self.nets[i]=copy.deepcopy(bestAgent)
        
        for i in range(self.agentNum-1):
            for j in range(1):
                self.mutateNet(i)
                
            
    
    
    def mutateNet(self,net):
        self.nets[net].setCon(random.randrange(0,self.conNum),random.randrange(0,self.nodeNum),random.randrange(0,self.nodeNum),random.randrange(-10000,10000)/10000)
        #print("Mutating: ", str(net))