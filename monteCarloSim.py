import tic
import random


t = tic.tic()
random.seed()
gameNum = 0
moveNum = 0

while 1:
    gameNum+=1
    if gameNum != 0:
        print(moveNum/gameNum)
    while 1:
        moveNum+=1
        if t.move(random.randrange(0,9)) !=0:
            t.resetBoard()
            
            break