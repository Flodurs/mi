import darwin
import net
import tic
import random
import eloSystem
import logging


#net Parameter
conNum = 400
nodeNum = 50
stepNum = 10

#darwin Parameter
playerNum = 30


#logging


logging.basicConfig(filename='D:/Dev/miVis/public/training.html', filemode='w', format='<p>%(message)s<p>', level=logging.INFO)




#innit



t = tic.tic(1)
darw = darwin.darwin(playerNum,conNum,nodeNum,100) 
netzA = net.net(nodeNum,conNum)
netzB = net.net(nodeNum,conNum)


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
    for i in range(10):
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
    #print("--------")
    while 1:
        netzA.reset()
        netzB.reset()
        
        
        
        
        #Spieler A Zug
        pos =  t.getBoard()
        input = processInput(pos)
        output=[]
        #print(input)
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
        if result == 0:
            return t.getMoveCount(),0.5
        
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
            return t.getMoveCount(),1
        if result == 2:
            return t.getMoveCount(),0
        if result == -1:
            return t.getMoveCount(),1
        if result == 0:
            return t.getMoveCount(),0.5
            
def playAndSafeSampleMatches(agent,amount):
    for i in range(amount):
        opponent = random.randrange(0,playerNum)
        resultA = playMatch(agent,opponent)
        t.saveMatch()
        resultA = playMatch(opponent,agent)
        t.saveMatch()
        


for i in range(99999):

    avgMoves = []
    for i in range(playerNum):
        moveNumList[i] = 0
        gameNumList[i] = 0
    
    ratings = evaluateNet()
 
    
    for i in range(playerNum):
        avgMoves.append(round(moveNumList[i]/gameNumList[i], 2))
        
    print(avgMoves)
    print(ratings)
    logging.info(ratings)
    logging.info(avgMoves)
    logging.info("-------------------------------------------------------------------------------------------")
    print(t.getAvgMovesPerGame())
    t.resetStats()
    
    
    playAndSafeSampleMatches(ratings.index(max(ratings)),10)
    
    #advance Generation
    
    darw.advanceGeneration(ratings)
   
    