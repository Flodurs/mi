

class tic:
    board  = [0]*9  
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
    
    
    spielender = 1
    

    def __init__(self):
        #print("Init Tic Tac Toe")
        pass
        
    def move(self,feld):
        
        
        if self.spielender == 1:
            self.spielender = 2
        else:
            self.spielender = 1
        
        if self.board[feld] != 0:
            return -1

        self.board[feld] = self.spielender
        self.printBoard()
        
        return self.detectWin()
        
    def getBoard(self):
        return self.board
            
    def detectWin(self):
        for win in self.wins:
            if self.board[win[0]]==1 and self.board[win[1]]==1 and self.board[win[2]]==1:
                print("Player 1 Won")
                return 1
        for win in self.wins:
            if self.board[win[0]]==2 and self.board[win[1]]==2 and self.board[win[2]]==2:
                print("Player 2 Won")
                return 2
        return 0
        
    def resetBoard(self):
        self.board  = [0]*9  
        
    def printBoard(self):
        print("-----------------")
        for j in range(9):
            
            print(self.board[j],end="")
            if (j+1)%3 == 0:
                print("")
        
    