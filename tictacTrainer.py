import darwin
import net
import tic
import random
import eloSystem


#net Parameter
conNum = 200
nodeNum = 50
stepNum = 4

#darwin Parameter
playerNum = 30



#innit



t = tic.tic()
darw = darwin.darwin(playerNum,conNum,nodeNum,1) 
netzA = net.net(conNum,nodeNum)
netzB = net.net(conNum,nodeNum)


#stats

moveNumList = [0]*playerNum
gameNumList = [0]*playerNum


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


def evaluateNet():
    #print("-------")
    eloSys = eloSystem.eloSystem(playerNum)
    for i in range(50):
        for j in range(playerNum):
            opponent = random.randrange(0,playerNum)
            
            
            resultA = playMatch(j,opponent)
            eloSys.matchPlayed(j,opponent,resultA[1])
            
           #update Stats
            moveNumList[j]+=resultA[0]
            moveNumList[opponent]+=resultA[0]
            
            gameNumList[j]+=1
            gameNumList[opponent]+=1
            
            
            resultA = playMatch(opponent,j)
            eloSys.matchPlayed(opponent,j,resultA[1])
            
            #update Stats
            moveNumList[j]+=resultA[0]
            moveNumList[opponent]+=resultA[0]
            
            gameNumList[j]+=1
            gameNumList[opponent]+=1
            
            
            
    eloSys.printElos()
    return eloSys.getElos()
    
            
            

def playMatch(a,b):

    t.resetBoard()
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
            output.append(netzA.getNode(x+13))
            
        move = output.index(max(output))
        
        result = t.move(move) 
        
        if result == 1:
            return t.getMoveCount(),1
        if result == 2:
            return t.getMoveCount(),0
        if result == -1:
            return t.getMoveCount(),0
        
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
            return t.getMoveCount(),0
        if result == 2:
            return t.getMoveCount(),1
        if result == -1:
            return t.getMoveCount(),1


for i in range(99999):

    avgMoves = []
    for i in range(playerNum):
        moveNumList[i] = 0
        gameNumList[i] = 0
    
    ratings = evaluateNet()
 
    
    for i in range(playerNum):
        avgMoves.append(round(moveNumList[i]/gameNumList[i], 2))
        
    print(avgMoves)
 
    print(t.getAvgMovesPerGame())
    t.resetStats()
    
    #advance Generation
    
    
   
    darw.advanceGeneration(ratings)
   
    #print/collect Progress
    