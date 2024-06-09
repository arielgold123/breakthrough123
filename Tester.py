from Randomagent import Randomagent
from breakthrough import Breakthourgh
from Fix_Agent import Fix_Agent
from DQN_Agent import DQN_Agent

class Tester:
    def __init__(self, env, player1, player2) -> None:
        self.env = env
        self.player1 = player1
        self.player2 = player2
        

    def test (self, games_num):
        env = self.env
        player = self.player1
        player1_win = 0
        player2_win = 0
        games = 0
        while games < games_num:
            action = player.get_Action(state=env.state, train = False)
            env.move(action, env.state)
            player = self.switchPlayers(player)
            if env.is_end_of_game(env.state):
                _, winner = env.who_won(state= env.state)
                if winner == 1:
                    player1_win += 1
                else:
                    player2_win += 1
                env.state = env.get_init_state()
                games += 1
                player = self.player1
        return player1_win, player2_win        

    def switchPlayers(self, player):
        if player == self.player1:
            return self.player2
        else:
            return self.player1

    def __call__(self, games_num):
        return self.test(games_num)

if __name__ == '__main__':
    env = Breakthourgh()
    player1 = Randomagent(env=env, player=1)
    
    # player2 = Randomagent(env=env, player=2)
    player2 = DQN_Agent(player=1, env= env, train=False, parametes_path="Data/params_101.pth")
    test = Tester(env,player1, player2)
    print(test.test(100))
    # player1 = Randomagent(env, player=1)
    # player2 = Randomagent(env, player=2)
    # test = Tester(env,player1, player2)
    # print(test.test(100))