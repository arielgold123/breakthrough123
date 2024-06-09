
import numpy as np
from state import State
from Graphics import *


class Breakthourgh:
    def __init__(self, state:State = None) -> None:
        if state == None:
            self.state = self.get_init_state()
        else:
            self.state = state

    def get_init_state(self):
        board = np.array([[2, 2, 2, 2, 2, 2, 2, 2],
                      [2, 2, 2, 2, 2, 2, 2, 2],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [
                          1, 1, 1, 1, 1, 1, 1, 1],
                      [1, 1, 1, 1, 1, 1, 1, 1]])

        return State (board)

    def is_free(self, row_col: tuple[int, int], state: State):
        row, col = row_col
        return state.board[row, col] != 0

    def is_inside(self, row_col, state: State):
        row, col = row_col
        board_row, board_col = state.board.shape
        return 0 <= row < board_row and 0 <= col < board_col

    def is_eat(self, start_row_col: tuple[int, int], dir_row_col: tuple[int, int], state: State):
        start_row, start_col = start_row_col
        dir_row, dir_col = dir_row_col
        if state.board[dir_row_col] != state.get_opponent():
            return False
       
        #row_enemy = int(abs(dir_row - start_row))
        #col_enemy = int(abs(dir_col - start_col))
        if  abs(dir_row - start_row) == 1 and abs(dir_col - start_col) == 1 :          
            return True
        return False

    def eat(self, start_row_col: tuple[int, int], dir_row_col: tuple[int, int], state: State):
        # start_row, start_col = start_row_col
        # dir_row, dir_col = dir_row_col
        # row_enemy = int(abs(dir_row + start_row)/2)
        # col_enemy = int(abs(dir_col + start_col)/2)
        # state.board[row_enemy][col_enemy] = 0
        # state.board[start_row][start_col] = 0
        # state.board[dir_row][dir_col] = state.player
        state.board[dir_row_col]=state.player
        state.board[start_row_col]=0

    def flip_piece(self, row_col, state: State):
        row, col = row_col
        if state.board[row][col] == 1:
            state.board[row][col] = 2
        else:
            state.board[row][col] = 1  

    def move(self, action, state: State):
        start_row_col, dir_row_col = action
        start_row, start_col = start_row_col
        dir_row, dir_col = dir_row_col
        if self.is_legal_move(start_row_col, dir_row_col, state):
            if self.is_eat(start_row_col, dir_row_col, state):
                self.eat(start_row_col, dir_row_col, state)
                state.switch_player()
                return True
            state.board[dir_row][dir_col] = state.player
            state.board[start_row][start_col] = 0
            state.switch_player()
            return True
        return False

    def is_legal_move(self, start_row_col: tuple[int, int], dir_row_col: tuple[int, int], state: State):
        start_row, start_col = start_row_col
        dir_row, dir_col = dir_row_col
        if state.board[start_row_col] != state.player:
            return False
        if dir_row > 7 or dir_col > 7 or dir_row<0 or dir_col<0:
            return False
        if state.board[dir_row][dir_col] != state.player and self.is_not_reverse(start_row_col, dir_row_col, state):
            if self.is_eat(start_row_col, dir_row_col, state):
                 return True
            if abs(dir_row - start_row) == 1 and  (abs(dir_col - start_col) == 1 or abs(dir_col - start_col) == 0) and state.board[dir_row][dir_col] == 0:
                return True
        return False
   
    def is_not_reverse (self, start_row_col, dir_row_col, state: State):
        start_row, start_col = start_row_col
        dir_row, dir_col = dir_row_col
        if state.player == 1 and dir_row < start_row:
            return True
        if state.player == 2 and dir_row > start_row:
            return True
        return False
   
    def get_legal_actions(self, state: State):
        legal_action = []
        rows, cols = 8, 8 #state.board.shape
        for row in range(rows):
            for col in range(cols):
                if state.player == 2:
                    if self.is_legal_move((row,col),(row+1, col) ,state):
                         legal_action.append(((row,col),(row+1, col)))
                    if self.is_legal_move((row,col),(row+1, col+1) ,state):
                          legal_action.append(((row,col), (row+1, col+1)))  
                    if self.is_legal_move((row,col),(row+1, col-1) ,state):
                          legal_action.append(((row,col), (row+1, col-1)))      
                if state.player == 1:
                    if self.is_legal_move((row,col),(row-1, col) ,state):
                         legal_action.append(((row,col),(row-1, col)))
                    if self.is_legal_move((row,col),(row-1, col+1) ,state):
                          legal_action.append(((row,col), (row-1, col+1)))  
                    if self.is_legal_move((row,col),(row-1, col-1) ,state):
                          legal_action.append(((row,col), (row-1, col-1)))            




        return legal_action

    def is_end_of_game(self, state: State):
        board = state.board
        for cell in board[7]:
            if cell == 2:
                return True
       
        for cell in board[0]:
            if cell == 1:
                return True
       
        return False
    def who_won(self, state: State):
        board = state.board
        for cell in board[7]:
            if cell == 2:
                return (True,2)
       
        for cell in board[0]:
            if cell == 1:
                return (True,1)
       
        return (False,0)
          
    def get_next_state(self, action, state):
        next_state = state.copy()
        self.move(action, next_state)
        return next_state
   
    def legal_Choose (self, pos, state):
        return state.board[pos] == state.player

    def get_all_next_states (self, state: State) -> tuple:
        legal_actions = state.legal_actions
        next_states = []
        for action in legal_actions:
            next_states.append(self.get_next_state(action, state))
        return next_states, legal_actions

    def reward (self, state : State, action = None) -> tuple:
        if action:
            next_state = self.get_next_state(action, state)
        else:
            next_state = state
        win, player = self.who_won(next_state)
        if player == 1:
            player = 1
        elif player == 2:
            player = -1
        else:
            player = 0
        return  player, win
    












