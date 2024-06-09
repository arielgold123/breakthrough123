import pygame
from Graphics import *
from breakthrough import *
from state import *
import random as rnd



class Randomagent:

    def __init__(self, player, env : Breakthourgh) :
        self.player = player
        self.mode = 1
        self.start = None
        self.env = env

    def get_Action (self, events= None, graphics: Graphics = None, state : State = None, train = None):
        actions = self.env.get_legal_actions(state)
        return rnd.choice(actions)
