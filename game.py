import pygame
from Graphics import *
from breakthrough import *
from humanagent import *
from state import *
import numpy as np
import random
from Randomagent import *
from MinMaxagent import *
import time
from AlphaBetaagent import *
from DQN_Agent import *

envi = Breakthourgh()

player1 = Human_Agent(2, envi)
#player2 = Human_Agent(2, envi)
#player1 = Randomagent(1, envi)
#player1 = DQN_Agent(1, envi,  train= False, parametes_path="Data/params_3.pth")
#player2 = DQN_Agent(2, envi, train = False ,parametes_path="Data/params_100.pth")
#player2 = Randomagent(2,envi)
#player2= Randomagent(2, envi)
#temp = AlphaBetaAgent(1, envi)
player2 = MinMax(1, envi)
#player1 = MinMax(1,envi)
# player2 = AlphaBetaAgent(player = 2, environment=envi)

def main():
   
    pygame.init()
    envi = Breakthourgh()
    graphics = Graphics()

    running = True
    while running:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
               running = False
            if envi.is_end_of_game(envi.state):
                print("player" + str(envi.state.player) + " won!")
                running = False
                break
           
        action = player1.get_Action(events=events, graphics=graphics, state=envi.state)
       
        if action:
            if envi.is_end_of_game(envi.state):
                print("player" + str(3 - envi.state.player) + " won!")
                running = False
                break
            envi.move(action , envi.state)
            pygame.time.delay(1000)
            print (action, envi.state.player)
            #change_player(player1)
           
            action = player2.get_Action(events, graphics, envi.state)
            if action:
                envi.move(action, envi.state)
                if envi.is_end_of_game(envi.state):
                    print("player" + str(envi.state.player) + " won!")
                    running = False
                    break
               
                print (action, envi.state.player)
            #print(temp.eval( envi.state))
        graphics.draw_board(envi.state)
        graphics.update()

    pygame.quit()
















def change_player (player):
    if player.player == 1:
        player = player2
    else:
        player = player1
























if __name__ == "__main__":
    main()
