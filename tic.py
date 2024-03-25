import logging

class tic:
    board  = []
    # 0 1 2
    # 3 4 5
    # 6 7 8
    
    
    
    
    wins = [[0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],
            [0, 3, 6],
            [1, 4, 7],
            [2, 5, 8],
            [0, 4, 8],
            [6, 4, 2],]
    
    
    
    
    

    def __init__(self,savingEnabled):
        #print("Init Tic Tac Toe")
        self.board = [0]*9
        self.spielender = 1
        self.moveCount = 0
        self.totalMovesPlayed = 0
        self.totalGamesPlayed = 0
        self.matchString = "";
        logging.basicConfig(filename='D:/Dev/miVis/public/matches.html', filemode='w', format='<p>%(message)s<p>', level=logging.INFO)
        self.savingEnabled = savingEnabled
        
    def move(self,feld):
        
        self.moveCount+=1
        self.totalMovesPlayed+=1
        
        if self.savingEnabled == 1:
            self.matchString+=str(feld)
       
        
        if self.board[feld] != 0:
            # print(feld)
            #print("Illegal Move")
            return -1
            

        self.board[feld] = self.spielender
        # self.printBoard()
        
        if self.spielender == 1:
            self.spielender = 2
        else:
            self.spielender = 1
        
        return self.detectWin()
        
    def getBoard(self):
        return self.board
            
    def detectWin(self):
        for win in self.wins:
            if self.board[win[0]]==1 and self.board[win[1]]==1 and self.board[win[2]]==1:
                #print("Player 1 Won xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
                return 1
        for win in self.wins:
            if self.board[win[0]]==2 and self.board[win[1]]==2 and self.board[win[2]]==2:
                #print("Player 2 Won xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
                return 2
        if self.moveCount == 9:
            return 0
        return 999
        
        
    def resetBoard(self):
        self.board  = [0]*9  
        self.totalGamesPlayed+=1
        self.moveCount = 0
        self.matchString = ""
    
    def resetStats(self):
        self.totalGamesPlayed = 0
        self.totalMovesPlayed = 0
        
    def getAvgMovesPerGame(self):
        if self.totalGamesPlayed != 0:
            return self.totalMovesPlayed/self.totalGamesPlayed
        return 0
        
    def printBoard(self):
        print("-----------------")
        for j in range(9):
            
            print(self.board[j],end="")
            if (j+1)%3 == 0:
                print("")
    
    def getMoveCount(self):
        return self.moveCount
    
    def saveMatch(self):
        file = open("D:/Dev/miVis/public/matches.html", "a")
        file.write(self.matchString+"\n")
        file.close()