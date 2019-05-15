import numpy as np
import pygame
import sys
import copy
import math
# Global constants for the GUI Setup
SQUARESIZE = 100
COL_NO = 7
ROW_NO = 6


class Player:
    player_id = int # to determine player 1 or 2

    # 1 -> user
    # 2 -> ai


    def __init__(self, player_id):
        self.player_id = player_id

    def play_move(self,board,j):

        #board here is numpy array

        for i in range(6):
            if board[5-i, j] == 0:
                board[5-i, j] = self.player_id
                return



    # returns ( score , best_j )
    def best_ai_move(self,board, alpha=- math.inf,beta=math.inf , turn = 2, depth = 10): #recusrive

        #board here is an object
        board_copy = copy.deepcopy(board)
        if(board_copy.full() and not board_copy.win()): # tie is happened at the leave node
            score = 0
            return score, None

        else




        if depth == 0
            p = function_younan()
            return p, 0
        depth -= 1

        # alpha_new = alpha
        # beta_new = beta
        a = alpha
        b = beta


        best_play = 0
        for i in range (7):

            if(board_copy.possible(i)):
                board_copy.play(turn, i)
                if board_copy.win():
                    if turn == 2:
                        return 100
                    else:
                        return -100
                    continue
                if turn == 2:
                    a, _ = self.best_ai_move(board_copy, a, b, 1, depth)
                    if a < alpha:
                        a = alpha
                    else :
                        best_play = i

                else :
                    b, _ = self.best_ai_move(board_copy, a, b, 2, depth)
                    if b > beta:
                        b = beta
                    else:
                        best_play = i

                board_copy.undo(i)#function to be made which removes the last coin in this column
                if a >= b :
                     if turn == 2 :
                         return b, best_play
                     else:
                         return a, best_play

        if turn == 2:
            return b, best_play
        else:
            return a, best_play
                #compute the best position
        #call play_move with this move


    def simulate_ai_move(self,board):
        j = self.best_ai_move()
        self.play_move(board.board, j)




class GameBoard:
    turn = (int)
    # 1 for user
    # 2 for ai

    def __init__(self):
        self.board = np.zeros((6,7)) # the connect 4 board is 6*7


    def full(self):
        for i in range(6):
            for j in range(7):
                if self.board[i, j] == 0:
                    return 0
        return 1

    def win(self):

        #check if there is a row of the same colour
        row_1 = np.array([1, 1, 1, 1])
        row_2 = np.array([2, 2, 2, 2])

        for i in range(6):
            for j in range(4):
                if (np.array_equal(self.board[i, j : j+4], row_1)) or (np.array_equal(self.board[i, j : j+4], row_2)):
                    return 1

        #check if there is a column of the same colour
        for i in range(3):
            for j in range(7):
                if (np.array_equal(self.board[i : i + 4, j], row_1)) or (np.array_equal(self.board[i : i + 4, j], row_2)):
                    return 1


        #check if there is a diagonal  [[1, 0, 0, 0] of the same colour
        #                               [0, 1, 0, 0]
        #                               [0, 0, 1, 0]
        #                               [0, 0, 0, 1]
        downward_diagonal_1 = np.array([[1, 0, 0, 0],[0, 1, 0, 0],[0, 0, 1, 0],[0, 0, 0, 1]])
        downward_diagonal_2 = np.array([[2, 0, 0, 0],[0, 2, 0, 0],[0, 0, 2, 0],[0, 0, 0, 2]])
        for i in range(3):
            for j in range(4):
                self.board_copy = np.multiply(self.board[i : i + 4, j : j+4],downward_diagonal_1)
                if (np.array_equal(self.board_copy, downward_diagonal_1)) or (np.array_equal(self.board_copy, downward_diagonal_2)):
                    return 1

        #check if there is a diagonal  [[0, 0, 0, 1] of the same colour
        #                               [0, 0, 1, 0]
        #                               [0, 1, 0, 0]
        #                               [1, 0, 0, 0]
        upward_diagonal_1 = np.array([[0, 0, 0, 1],[0, 0, 1, 0],[0, 1, 0, 0],[1, 0, 0, 0]])
        upward_diagonal_2 = np.array([[0, 0, 0, 2],[0, 0, 2, 0],[0, 2, 0, 0],[2, 0, 0, 0]])
        for i in range(3):
            for j in range(4):
                self.board_copy = np.multiply(self.board[i : i + 4, j : j+4],upward_diagonal_1)
                if (np.array_equal(self.board_copy, upward_diagonal_1)) or (np.array_equal(self.board_copy, upward_diagonal_2)):
                    return 1
        return 0

    def possible(self, j):
        for i in range(6):
            if self.board[i,j] == 0:
                return 1
        return 0

    def play(self, player, j):
        for i in range(6):
            if self.board[5-i, j] == 0:
                self.board[5-i, j] = player
                return

    def undo(self, j):
        for i in range(6):
            if self.board[5-i, j] != 0:
                self.board[5-i, j] = 0
                return


                ######################__________board_evaluation_function_with_some_helping_functions__________###########################################
                # helping functions

    def there_is_three_in_a_row(self, board):
        row_1 = np.array([self.turn, self.turn, self.turn])
        for i in range(6):
            for j in range(3):
                if (np.array_equal(board[i, j: j + 3], row_1)):
                    return 1

        return 0

    def there_is_two_in_a_row(self, board, opponent):
        if opponent:
            if self.turn == 1:
                row_1 = np.array([2, 2])
            else:
                row_1 = np.array([1, 1])
        else:
            row_1 = np.array([self.turn, self.turn, ])

        for i in range(6):
            for j in range(4):
                if (np.array_equal(board[i, j: j + 2], row_1)):
                    return 1

        return 0

    def there_is_opponent_win_chance(self, board):


        #if self.player_id == 1:
        if self.turn == 1:
            row_1 = np.array([2, 2])
        else:
            row_1 = np.array([1, 1])

        for i in range(6):
            for j in range(3):
                if (np.array_equal(board[i, j: j + 3], row_1)):
                    return 1
        return 0

    def evaluate_state(self, board, next_move):
        # maximum value = 100 -> absolute win with this next move
        # minimum value = -100 -> absolute lose with this next move

        win_score = 100
        lose_score = 100
        score = 0
        new_board = GameBoard()
        new_board.board = np.copy(board)

        if (new_board.possible(next_move)):
            self.play(new_board.board, next_move)

        if (new_board.win()):
            return win_score

        if next_move == 3:  # board center
            score += 4

        if self.there_is_two_in_a_row(new_board.board, opponent=0):
            score += 3

        if self.there_is_three_in_a_row(new_board.board):
            score += 5

        if self.there_is_two_in_a_row(new_board.board, opponent=1):
            score -= 5

        if self.there_is_opponent_win_chance(new_board.board):
            return lose_score

        return score


############################################################################################################################




class Game:
    width = (int)
    height = (int)
    size = (int, int)
    radius = int()

    def __init__(self):
        self.turn = 1
        self.board = GameBoard()
        self.player_1 = Player(player_id=1)
        self.player_2 = Player(player_id=2)


    def GUI_setup(self):
        pygame.init()

        self.width = COL_NO * SQUARESIZE
        self.height = (ROW_NO + 1) * SQUARESIZE
        self.size = (self.width,self.height)
        self.radius = int(SQUARESIZE/2 - 10)
        self.font = pygame.font.SysFont("monospace", 30)
        self.screen = pygame.display.set_mode(self.size)


    def draw_board(self):

        for c in range(COL_NO):
            for r in range(ROW_NO):
                pygame.draw.rect(self.screen,(100,0,200) , (c*SQUARESIZE , r * SQUARESIZE + SQUARESIZE , SQUARESIZE, SQUARESIZE) )
                if self.board.board[r][c] == 0:
                    pygame.draw.circle(self.screen, (0, 0, 0),
                                       (int(c * SQUARESIZE + SQUARESIZE / 2), int((r+1) * SQUARESIZE + SQUARESIZE / 2)),
                                       self.radius)


                elif self.board.board[r][c] == 1:  # Red
                    pygame.draw.circle(self.screen, (255, 0, 0),
                                       (int(c * SQUARESIZE + SQUARESIZE / 2) +1, int((r+1) * SQUARESIZE + SQUARESIZE / 2)+1),
                                       self.radius)

                elif self.board.board[r][c] == 2: # Yellow
                    pygame.draw.circle(self.screen, (255, 255, 0),
                                       (int(c * SQUARESIZE + SQUARESIZE / 2) +1, int((r+1) * SQUARESIZE + SQUARESIZE / 2)+1),
                                       self.radius)


                pygame.display.update()



    def simulate_game(self): # the loop of playing

        self.GUI_setup()
        self.draw_board()

        game_end = False

        label = self.font.render('player 1 turn', 1, (255, 0, 0))
        self.screen.blit(label, (40, 50))
        pygame.display.update()

        while (not game_end):

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()


                if event.type == pygame.MOUSEBUTTONDOWN:

                    x = event.pos[0]
                    place = int(x/SQUARESIZE)


                    if self.board.possible(place):

                        if(self.turn == 1):
                            self.player_1.play_move(self.board.board,place)
                            self.turn = 2
                            label = self.font.render('player ' + str(self.turn) + ' turn', 1, (255, 255, 0))


                        else:
                            self.player_2.play_move(self.board.board, place)
                            self.turn = 1
                            label = self.font.render('player ' + str(self.turn) + ' turn', 1, (255, 0, 0))


                        self.draw_board()
                        self.screen.fill(pygame.Color("black"), (40, 50, 300, 50))
                        self.screen.blit(label, (40, 50))
                        pygame.display.update()

                    if (self.board.full() or self.board.win()):
                        game_end = True
                        if (self.board.win()):

                            if(self.turn == 2): # Player 1 Wins

                                label = self.font.render('***** player 1 wins *****', 1,
                                                         (255, 0, 0))
                                self.screen.blit(label, (40, 10))

                            elif(self.turn == 1): # Player 2 Wins

                                label = self.font.render('***** player 2 wins *****', 1,
                                                         (255,255, 0))
                                self.screen.blit(label, (40, 10))


                        else:
                            label = self.font.render('***** TIE ! *****' , 1, (255,255,255))
                            self.screen.blit(label,(40,10))



                        #wait 7 seconds before exist
                        pygame.display.update()
                        pygame.time.wait(7000)

hi = Game()
hi.simulate_game()
