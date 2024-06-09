import pygame
from Graphics import *
from breakthrough import *
from state import *

class Human_Agent:

    def __init__(self, player, env : Breakthourgh) :
        self.player = player
        self.mode = 1
        self.start = None
        self.env = env

    def get_Action (self, events= None, graphics: Graphics = None, state : State = None):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row_col = graphics.calc_row_col(pos)
                print (row_col)
               
                if self.mode == 1:
                    if self.env.legal_Choose(state = state, pos = row_col):
                        self.start = row_col
                       
                        print("legal choose", self.start)
                        self.mode = 2
                    else:
                       
                        print("illegal")
                    return None
                else:
                    if self.env.is_legal_move (self.start, row_col, state):
                        # self.env.move((self.start ,row_col), state)
                        self.mode = 1
                        return (self.start), (row_col)
           
        return None








