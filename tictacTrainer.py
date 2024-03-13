import darwin
import net
import tic

#net Parameter
conNum = 200
nodeNum = 30
stepNum = 10

#darwin Parameter
playerNum = 10



#innit

ratings = [0.0]*playerNum


darw = darwin.darwin(playerNum,conNum,nodeNum,1) 
netzA = net.net(conNum,nodeNum)
netzB = net.net(conNum,nodeNum)

#statistics
avgMovesList = [0]*playerNum



def processInput(pos):
    input = []
    for j in pos:
        if j == 1:
            input.append(1)
        if j == 2:
            input.append(-1)
        if j == 0:
            input.append(0)    
        input.append(1)
    return input     


def evaluateNet(net):
    #print("-------")
    for b in range(playerNum):
        if a != b:
            
            result = playMatch(net,b)
                
            if result[1] == net:
                #print(net)
                ratings[net]+=1
            else:
                ratings[b]+=1
            
            avgMovesList[net]+=result[0]
            
            result = playMatch(b,net)
                
            if result[1] == net:
                ratings[net]+=1
            else:
                ratings[b]+=1
            
            avgMovesList[net]+=result[0]
            
            
            

def playMatch(a,b):

    t = tic.tic()
    netzA.setFromGenoType(darw.getGenoType(a))
    netzB.setFromGenoType(darw.getGenoType(b))
    while 1:
        netzA.reset()
        netzB.reset()
        
        
        
        
        #Spieler A Zug
        pos =  t.getBoard()
        input = processInput(pos)
        output=[]
        for x in range(10):
            netzA.setNode(x,input[x])
        for x in range(stepNum):
            netzA.step()
        for x in range(9):
            output.append(netzA.getNode(x+11))
            
        move = output.index(max(output))
        
        result = t.move(move) 
        
        if result == 1:
            return t.getMoveCount(),a
        if result == 2:
            return t.getMoveCount(),b
        if result == -1:
            return t.getMoveCount(),b
        
        #Spieler B Zug
        pos =  t.getBoard()
        input = processInput(pos)
        output=[]
        for x in range(10):
            netzB.setNode(x,input[x])
        for x in range(stepNum):
            netzB.step()
        for x in range(9):
            output.append(netzB.getNode(x+11))
            
        move = output.index(max(output))
        
        result = t.move(move) 
        
        if result == 1:
            return t.getMoveCount(),b
        if result == 2:
            return t.getMoveCount(),a
        if result == -1:
            return t.getMoveCount(),a


for i in range(99999):
    ratings = [0.0]*playerNum
    avgMovesList = [0]*playerNum
    for a in range(playerNum):
        evaluateNet(a)
    #print("-----------------")
    print(sum(avgMovesList)/((18+18)*10),end="")
    
    
    #advance Generation
    print(ratings)
    for j in range(len(ratings)):
        if ratings[j] != 0:
            ratings[j]=1/ratings[j]
        else:
            ratings[j]=99999
   
    darw.advanceGeneration(ratings)
   
    #print/collect Progress
    