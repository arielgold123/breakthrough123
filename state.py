import numpy as np
import pygame
import torch


class State:
    def __init__(self, board, player = 1):
        self.board= board
        self.player = player
        # self.legal_actions = legal_actions  
   
    def switch_player(self):
        self.player=-self.player +3

    def copy(self):
        newBoard=np.copy(self.board)
        return State(newBoard,self.player)

    def get_opponent(self):
        return -self.player +3  

    def reverse (self):
        reversed = self.copy()
        reversed.board = reversed.board * -1
        reversed.player = reversed.player * -1
        return reversed

    def toTensor (self, device = torch.device('cpu')) -> tuple:
        board_np = self.board.reshape(-1)
        board_tensor = torch.tensor(board_np, dtype=torch.float32, device=device)
        #actions_np = np.array(self.legal_actions)
        #actions_tensor = torch.from_numpy(actions_np)
        return board_tensor #actions_tensor
    
    [staticmethod]
    def tensorToState (state_tensor, player):
        
        board = state_tensor.reshape([8,8]).cpu().numpy()
        return State(board, player=player)
