import numpy as np
import pygame
import sys
import copy

# Global constants for the GUI Setup
SQUARESIZE = 100
COL_NO = 7
ROW_NO = 6


class Player:
    player_id = int # to determine player 1 or 2
    score = int # to define which player have high probability of winning at this point of the game

    def __init__(self, player_id):
        self.player_id = player_id
        self.score = 0

    def play_move(self,board,j):

        #board here is numpy array

        for i in range(6):
            if board[5-i, j] == 0:
                board[5-i, j] = self.player_id
                return




    def best_ai_move(self,board, alpha=-100,beta=100 , turn = 2, depth = 10): #recusrive
        """we check the best ai move by the following steps

            1- base conditions or leaf nodes:
                a) the board is full--->we call the metric fn and return its value
                b) we reach the allowed depth--->we call the metric fn and return its value
                c) we reach a winning or losing state--->we check whose turn this is...if it is the ai's turn(winning state) then we return to the parent node 100(or max metric) and if it's the human's turn(losing state) we return -100(or min metric)

            2- normal node checking:
                a) we check whose turn it is now
                b) we call the same fn recusrively for the oponent
                    if it is the ai's turn which called the fn ...then we will change the alpha value by taking the beta of the children and checking if they are bigger than it's alpha
                    if it is the human's turn which called the fn ...then we will change the beta value by taking the alpha of the children and checking if they are smaller than it's beta
                c) if we reach a state where beta < alpha ...then we don't continue and take the current node's alpha or beta depending on whose turn it is
                d) if none of the returns above are used we return the alpha or beta normally depending on whose turn it is

            here alpha === child_beta
                 beta === child_alpha"""
        #board here is an object

        board_copy = copy.deepcopy(board)

        #check if board is full
        if(board_copy.full()):
            p = function_younan()
            return p, 0
        #check if max depth is reached then decrementing the depth
        if depth == 0
            p = function_younan()
            return p, 0
        depth -= 1

        # child beta and alpha created...their purpose is to not change the values of the original alpha and beta
        child_beta = alpha
        child_alpha = beta

        #start the normal node's sequence
        best_play = 0
        for i in range (7):

            #check if it is possible to play in column i
            if(board_copy.possible(i)):

                #try playing in this column
                board_copy.play(turn, i)

                #check if by playing this move you or your oponent won
                if board_copy.win():
                    if turn == 2:
                        return 100 # this is not alpha nor beta...it is a metric since this is a leaf node...100 because this is a winning state
                    else:
                        return -100 # this is not alpha nor beta...it is a metric since this is a leaf node...-100 because this is a losing state
                    continue # a leaf so we don't have to continue

                #check whose turn it is to decide if we are changing alpha or beta
                if turn == 2:
                    temp = child_beta
                    child_beta, _ = self.best_ai_move(board_copy, child_beta, child_alpha, 1, depth)
                    if child_beta < temp: # this condition means that this child is worse than the prev child
                        child_beta = temp # return to prev child
                    else :
                        best_play = i # this child is better so this is the best play and the best child beta

                else :
                    temp = child_alpha
                    child_alpha, _ = self.best_ai_move(board_copy, child_beta, child_alpha, 2, depth)
                    if child_alpha > temp: # this condition means that this child is worse than the prev child
                        child_alpha = temp # return to prev child
                    else:
                        best_play = i # this child is better so this is the best play and the best child alpha

                board_copy.undo(i) # return to prev state before trying another child


                # alpha or beta pruning
                if child_beta >= child_alpha :
                     if turn == 2 :
                         return child_beta, best_play
                     else:
                         return child_alpha, best_play
        #normal return
        if turn == 2:
            return child_beta, best_play
        else:
            return child_alpha, best_play
                #compute the best position
        #call play_move with this move


    def simulate_ai_move(self,board):
        j = self.best_ai_move()
        self.play_move(self.board.board, j)






class GameBoard:

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
            if board[5-i, j] == 0:
                board[5-i, j] = player
                return

    def undo(self, j):
        for i in range(6):
            if board[5-i, j] != 0:
                board[5-i, j] = 0
                return


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
