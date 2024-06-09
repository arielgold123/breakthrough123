from breakthrough import Breakthourgh
from state import State
MAXSCORE = 10000000000000000000000000000000000000000000000000

class AlphaBetaAgent:

    def __init__(self, player, depth = 4, environment: Breakthourgh = None):
        self.player = player
        if self.player == 1:
            self.opponent = 2
        else:
            self.opponent = 1
        self.depth = depth
        self.environment : Breakthourgh = environment

    def eval(self, state:State):
        board = state.board
        player_num = state.player
        score = 0
        opposite_player_num = 3 - player_num  
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
    

    def get_Action(self, event, graphics, state: State):
        visited = set()
        value, bestAction = self.minMax(state, visited)
        return bestAction

    def minMax(self, state:State, visited:[]):
        depth = 0
        alpha = -MAXSCORE
        beta = MAXSCORE
        return self.max_value(state, visited, depth, alpha, beta)
        
    def max_value (self, state:State, visited:[], depth, alpha, beta):
        
        value = -MAXSCORE

        # stop state
        if depth == self.depth or self.environment.is_end_of_game(state):
            value = self.eval(state)
            return value, None
         
        # start recursion
        bestAction = None
        legal_actions = self.environment.get_legal_actions(state)
        for action in legal_actions:
            newState = self.environment.get_next_state(action, state)
            if newState not in visited:
                visited.add(newState)
                newValue, newAction = self.min_value(newState, visited,  depth + 1, alpha, beta)
                if newValue > value:
                    value = newValue
                    bestAction = action
                    alpha = max(alpha, value)
                if value >= beta:
                    return value, bestAction
                    

        return value, bestAction 

    def min_value (self, state:State, visited:[], depth, alpha, beta):
        
        value = MAXSCORE

        # stop state
        if depth == self.depth or self.environment.is_end_of_game(state):
            value = self.eval(state)
            return value, None
        
        # start recursion
        bestAction = None
        legal_actions = self.environment.get_legal_actions(state)
        for action in legal_actions:
            newState = self.environment.get_next_state(action, state)
            if newState not in visited:
                visited.add(newState)
                newValue, newAction = self.max_value(newState, visited,  depth + 1, alpha, beta)
                if newValue < value:
                    value = newValue
                    bestAction = action
                    beta = min(beta, value)
                if value <= alpha:
                    return value, bestAction

        return value, bestAction 
