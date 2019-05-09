import numpy as np

class Player:
    name = str
    score = int # to define which player have high probability of winning at this point of the game


    def __init__(self, name="Player"):
        self.name = name
        self.score = 0

    def play_move(self,board,position):
        pass


class GameBoard:

    board = np.zeros((6,7)) # the connect 4 board is 6*7

    def full(self):
        pass

    def win(self):
        pass




class Game:

    turn = bool
    # 0 for player 1
    # 1 for computer

    board = GameBoard()

    player_1 = Player()
    computer = Player()

    def __init__(self, turn = 0):
        self.turn = turn


    def simulate_game(self): # the loop of playing

        game_end = False

        while (not game_end):

            if( board.full() or board.win()):
                game_end = True







