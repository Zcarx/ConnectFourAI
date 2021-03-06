# imports game.py
# calls playerfunction
# displays gamedata
from game import game
from _Players.RandomPlayer import RandomPlayer
import numpy as np
import time

# Instanciation of the Game
gameInstance = game(7,6)

# instanciation of the Players depending on the PlayerClass
Pp1 = RandomPlayer( 1)
Pm1 = RandomPlayer(-1)

#Game params
waittime = 0 #time between each move of the players

# the loop for playing the game until somebody won or the limit is reached
for x in range(0, 3*7*):
    
    c = Pp1.chooseCol(gameInstance) #the positive Player chooses his column
    i, win = gameInstance.playAction(Pp1.getId(), c) # the positive Player plays
    if(win):
        print('The positive Player won the game')
        break
    time.sleep(waittime)
    
    
    c = Pn1.chooseCol(gameInstance) #the negative Player chooses his column
    i, win = gameInstance.playAction(Pn1.getId(), c) # the negative Player plays
    if(win):
        print('The negative Player won the game')
        break
    time.sleep(waittime) 
# end for