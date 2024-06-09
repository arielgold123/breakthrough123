import pygame
from Graphics import *
from breakthrough import *
from state import *


class MinMax:
   
    def __init__(self, player, env : Breakthourgh, depth : int = 3) :
        self.player = player
        self.mode = 1
        self.start = None
        self.env = env
        self.depth= depth


    def eval(self, state:State):
        board = state.board
        player_num = state.player
        score = 0
        opposite_player_num = 3 - player_num  # Assuming player_num is always 1 or 2
        x = 0
        if player_num == 2:
            for row in board:
                for cell in row:
                    if cell == player_num:
                        score += ((x + 1)**3)
                    elif cell == opposite_player_num:
                        score -= ((8 - x)**3)
                x += 1
               
               
               
           
        else:
            for row in board:
                for cell in row:
                    if cell == player_num:
                        score += ((8 - x)**3)
                    elif cell == opposite_player_num:
                        score -= ((x + 1)**3)
                x += 1


        return score
   


    def get_Action(self, event, graphics, gameState):
        reached = set()
        value, bestAction = self.minMax(gameState, reached, 0)
        return bestAction




    def minMax(self, gameState, reached:set, depth):
        if self.player == gameState.player:
            value = -1000
        else:
            value = 1000


        # stop state
        if depth == self.depth or self.env.is_end_of_game(gameState):
            value = self.eval(gameState)
            return value, None
       
        # start recursion
        bestAction = None
        legal_actions = self.env.get_legal_actions(gameState)
        for action in legal_actions:
            newGameState = self.env.get_next_state(action, gameState)
            if newGameState not in reached:
                reached.add(newGameState)
                if self.player == gameState.player:         # maxNode - agent
                    newValue, newAction = self.minMax(newGameState, reached,  depth + 1)
                    if newValue > value:
                        value = newValue
                        bestAction = action
                else:                       # minNode - opponent
                    newValue, newAction = self.minMax(newGameState, reached,  depth + 1)
                    if newValue < value:
                        value = newValue
                        bestAction = action


        return value, bestAction


   


