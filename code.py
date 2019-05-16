import numpy as np
import pygame
import sys
import copy
import math
import random
# Global constants for the GUI Setup
SQUARESIZE = 100
COL_NO = 7
ROW_NO = 6

'''
def tempEval():
    global COUNTER
    COUNTER +=1
    val = random.randint(1, 300)
    return val
'''

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



    # returns ( score , best_play )
    def best_ai_move(self,board, alpha=- math.inf,beta=math.inf , turn = 2, depth = 1 ,current_position = 0): #recusrive
        #board here is an object
        board_copy = copy.deepcopy(board)

        # base conditions

        if(board_copy.full() and not board_copy.win()): # tie is happened at the leaf node
            return 0, None

        if (board_copy.full() and  board_copy.win()):  # one player is win
            #score = tempEval()
            score = board_copy.evaluate_state(current_position)
            return score, None

        if (depth == 0):
            #score = tempEval()
            score = board_copy.evaluate_state(current_position)
            return score, None

        # now the algorithm part

        best_play = 0

        depth -= 1

        for i in range (7):
            if(board_copy.possible(i)):
                board_copy.play(turn, i)
                '''
                if board_copy.win():
                    if turn == 2:
                        return 100
                    else:
                        return -100
                '''
                if turn == 2: # Maxmizing -> a.i turn
                    value, _ = self.best_ai_move(board_copy, alpha, beta, 1, depth, i)
                    if value > alpha:
                        alpha = value
                        best_play = i


                else : # Minimizing -> user turn
                    value, _ = self.best_ai_move(board_copy, alpha, beta, 2, depth, i)
                    if value < beta :

                        beta = value
                        best_play = i


                board_copy.undo(i)#function to be made which removes the last coin in this column

                if alpha >= beta :
                    if turn == 2 : # Beta cut off
                         return alpha, best_play

                    else:  # Alpha cut off
                        return beta, best_play

        if turn == 2: # max node return alpha
            return alpha, best_play
        else:         # min node return beta
            return beta, best_play


    def simulate_ai_move(self,board,depth = 8):
        _ , j = self.best_ai_move(board,depth= depth)
        self.play_move(board.board, j)




class GameBoard:
    turn = (int)
    # 1 for user
    # 2 for ai
    lead = (int)

    def __init__(self,lead = 1):
        self.board = np.zeros((6,7)) # the connect 4 board is 6*7
        self.lead = lead
        self.turn = lead

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
                if(self.turn == 1):
                    self.turn = 0
                else:
                    self.turn = 1

                return

    def undo(self, j):
        for i in range(6):
            if self.board[i, j] != 0:
                self.board[i, j] = 0
                if (self.turn == 1):
                    self.turn = 0

                else:
                    self.turn = 1
                return


                ######################__________board_evaluation_function_with_some_helping_functions__________###########################################
                # helping functions

    def possible_win_chances_in_rows(self, opponent):
        if opponent:
            if self.turn == 1:
                three_in_a_row_right_win = np.array([2, 2, 2, 0])
                three_in_a_row_left_win = np.array([0, 2, 2, 2])

                three_in_a_row_middle_win1 = np.array([2, 0, 2, 2])
                three_in_a_row_middle_win2 = np.array([2, 2, 0, 2])
            else:
                three_in_a_row_right_win = np.array([1, 1, 1, 0])
                three_in_a_row_left_win = np.array([0, 1, 1, 1])

                three_in_a_row_middle_win1 = np.array([1, 0, 1, 1])
                three_in_a_row_middle_win2 = np.array([1, 1, 0, 1])
        else:
            three_in_a_row_right_win = np.array([self.turn, self.turn, self.turn, 0])
            three_in_a_row_left_win = np.array([0, self.turn, self.turn, self.turn])

            three_in_a_row_middle_win1 = np.array([self.turn, 0, self.turn, self.turn])
            three_in_a_row_middle_win2 = np.array([self.turn, self.turn, 0, self.turn])

        row_win_chances = []
        for i in range(6):
            for j in range(4):
                if ((np.array_equal(self.board[i, j: j + 4], three_in_a_row_right_win))
                    or (np.array_equal(self.board[i, j: j + 4], three_in_a_row_left_win))
                    or (np.array_equal(self.board[i, j: j + 4], three_in_a_row_middle_win1))
                    or (np.array_equal(self.board[i, j: j + 4], three_in_a_row_middle_win2))):
                    row_win_chances.append(6 - i)
        return row_win_chances

    def two_in_a_row(self, opponent):
        weak_chance = []
        if opponent:
            if self.turn == 1:
                two_in_a_row1 = np.array([0, 0, 2, 2])
                two_in_a_row2 = np.array([2, 2, 0, 0])
                two_in_a_row3 = np.array([0, 2, 0, 2])
                two_in_a_row4 = np.array([2, 0, 2, 0])
                two_in_a_row5 = np.array([0, 2, 2, 0])
            else:
                two_in_a_row1 = np.array([0, 0, 1, 1])
                two_in_a_row2 = np.array([1, 1, 0, 0])
                two_in_a_row3 = np.array([0, 1, 0, 1])
                two_in_a_row4 = np.array([1, 0, 1, 0])
                two_in_a_row5 = np.array([0, 1, 1, 0])
        else:
            two_in_a_row1 = np.array([0, 0, self.turn, self.turn])
            two_in_a_row2 = np.array([self.turn, self.turn, 0, 0])
            two_in_a_row3 = np.array([0, self.turn, 0, self.turn])
            two_in_a_row4 = np.array([self.turn, 0, self.turn, 0])
            two_in_a_row5 = np.array([0, self.turn, self.turn, 0])

        for i in range(6):
            for j in range(4):
                if ((np.array_equal(self.board[i, j: j + 4], two_in_a_row1))
                    or (np.array_equal(self.board[i, j: j + 4], two_in_a_row2))
                    or (np.array_equal(self.board[i, j: j + 4], two_in_a_row3))
                    or (np.array_equal(self.board[i, j: j + 4], two_in_a_row4))
                    or (np.array_equal(self.board[i, j: j + 4], two_in_a_row5))):
                    weak_chance.append(6 - i)
        return weak_chance

    def diagonal_strong_chance(self, opponent):  # three on a diagonal line
        if opponent:
            if self.turn == 1:
                downward_diagonal_1 = np.array([[2, 0, 0, 0],
                                                [0, 2, 0, 0],
                                                [0, 0, 2, 0],
                                                [0, 0, 0, 0]])

                downward_diagonal_2 = np.array([[0, 0, 0, 0],
                                                [0, 2, 0, 0],
                                                [0, 0, 2, 0],
                                                [0, 0, 0, 2]])

                downward_diagonal_3 = np.array([[2, 0, 0, 0],
                                                [0, 0, 0, 0],
                                                [0, 0, 2, 0],
                                                [0, 0, 0, 2]])

                downward_diagonal_4 = np.array([[2, 0, 0, 0],
                                                [0, 2, 0, 0],
                                                [0, 0, 0, 0],
                                                [0, 0, 0, 2]])

                upward_diagonal_1 = np.array([[0, 0, 0, 2],
                                              [0, 0, 2, 0],
                                              [0, 2, 0, 0],
                                              [0, 0, 0, 0]])

                upward_diagonal_2 = np.array([[0, 0, 0, 0],
                                              [0, 0, 2, 0],
                                              [0, 2, 0, 0],
                                              [2, 0, 0, 0]])

                upward_diagonal_3 = np.array([[0, 0, 0, 2],
                                              [0, 0, 0, 0],
                                              [0, 2, 0, 0],
                                              [2, 0, 0, 0]])

                upward_diagonal_4 = np.array([[0, 0, 0, 2],
                                              [0, 0, 2, 0],
                                              [0, 0, 0, 0],
                                              [2, 0, 0, 0]])

            else:
                downward_diagonal_1 = np.array([[1, 0, 0, 0],
                                                [0, 1, 0, 0],
                                                [0, 0, 1, 0],
                                                [0, 0, 0, 0]])

                downward_diagonal_2 = np.array([[0, 0, 0, 0],
                                                [0, 1, 0, 0],
                                                [0, 0, 1, 0],
                                                [0, 0, 0, 1]])

                downward_diagonal_3 = np.array([[1, 0, 0, 0],
                                                [0, 0, 0, 0],
                                                [0, 0, 1, 0],
                                                [0, 0, 0, 1]])

                downward_diagonal_4 = np.array([[1, 0, 0, 0],
                                                [0, 1, 0, 0],
                                                [0, 0, 0, 0],
                                                [0, 0, 0, 1]])

                upward_diagonal_1 = np.array([[0, 0, 0, 1],
                                              [0, 0, 1, 0],
                                              [0, 1, 0, 0],
                                              [0, 0, 0, 0]])

                upward_diagonal_2 = np.array([[0, 0, 0, 0],
                                              [0, 0, 1, 0],
                                              [0, 1, 0, 0],
                                              [1, 0, 0, 0]])

                upward_diagonal_3 = np.array([[0, 0, 0, 1],
                                              [0, 0, 0, 0],
                                              [0, 1, 0, 0],
                                              [1, 0, 0, 0]])

                upward_diagonal_4 = np.array([[0, 0, 0, 1],
                                              [0, 0, 1, 0],
                                              [0, 0, 0, 0],
                                              [1, 0, 0, 0]])

        else:
            downward_diagonal_1 = np.array([[self.turn, 0, 0, 0],
                                            [0, self.turn, 0, 0],
                                            [0, 0, self.turn, 0],
                                            [0, 0, 0, 0]])

            downward_diagonal_2 = np.array([[0, 0, 0, 0],
                                            [0, self.turn, 0, 0],
                                            [0, 0, self.turn, 0],
                                            [0, 0, 0, self.turn]])

            downward_diagonal_3 = np.array([[self.turn, 0, 0, 0],
                                            [0, 0, 0, 0],
                                            [0, 0, self.turn, 0],
                                            [0, 0, 0, self.turn]])

            downward_diagonal_4 = np.array([[self.turn, 0, 0, 0],
                                            [0, self.turn, 0, 0],
                                            [0, 0, 0, 0],
                                            [0, 0, 0, self.turn]])

            upward_diagonal_1 = np.array([[0, 0, 0, self.turn],
                                          [0, 0, self.turn, 0],
                                          [0, self.turn, 0, 0],
                                          [0, 0, 0, 0]])

            upward_diagonal_2 = np.array([[0, 0, 0, 0],
                                          [0, 0, self.turn, 0],
                                          [0, self.turn, 0, 0],
                                          [self.turn, 0, 0, 0]])

            upward_diagonal_3 = np.array([[0, 0, 0, self.turn],
                                          [0, 0, 0, 0],
                                          [0, self.turn, 0, 0],
                                          [self.turn, 0, 0, 0]])

            upward_diagonal_4 = np.array([[0, 0, 0, self.turn],
                                          [0, 0, self.turn, 0],
                                          [0, 0, 0, 0],
                                          [self.turn, 0, 0, 0]])

        template_downward_diagonal_1 = np.array([[1, 0, 0, 0],
                                                 [0, 1, 0, 0],
                                                 [0, 0, 1, 0],
                                                 [0, 0, 0, 0]])

        template_downward_diagonal_2 = np.array([[0, 0, 0, 0],
                                                 [0, 1, 0, 0],
                                                 [0, 0, 1, 0],
                                                 [0, 0, 0, 1]])

        template_downward_diagonal_3 = np.array([[1, 0, 0, 0],
                                                 [0, 0, 0, 0],
                                                 [0, 0, 1, 0],
                                                 [0, 0, 0, 1]])

        template_downward_diagonal_4 = np.array([[1, 0, 0, 0],
                                                 [0, 1, 0, 0],
                                                 [0, 0, 0, 0],
                                                 [0, 0, 0, 1]])

        template_upward_diagonal_1 = np.array([[0, 0, 0, 1],
                                               [0, 0, 1, 0],
                                               [0, 1, 0, 0],
                                               [0, 0, 0, 0]])

        template_upward_diagonal_2 = np.array([[0, 0, 0, 0],
                                               [0, 0, 1, 0],
                                               [0, 1, 0, 0],
                                               [1, 0, 0, 0]])

        template_upward_diagonal_3 = np.array([[0, 0, 0, 1],
                                               [0, 0, 0, 0],
                                               [0, 1, 0, 0],
                                               [1, 0, 0, 0]])

        template_upward_diagonal_4 = np.array([[0, 0, 0, 1],
                                               [0, 0, 1, 0],
                                               [0, 0, 0, 0],
                                               [1, 0, 0, 0]])
        diagonal_strong_chances = []
        for i in range(3):
            for j in range(4):
                kernal_downward_diagonal_1 = np.multiply(self.board[i: i + 4, j: j + 4], template_downward_diagonal_1)
                kernal_downward_diagonal_2 = np.multiply(self.board[i: i + 4, j: j + 4], template_downward_diagonal_2)
                kernal_downward_diagonal_3 = np.multiply(self.board[i: i + 4, j: j + 4], template_downward_diagonal_3)
                kernal_downward_diagonal_4 = np.multiply(self.board[i: i + 4, j: j + 4], template_downward_diagonal_4)

                kernal_upward_diagonal_1 = np.multiply(self.board[i: i + 4, j: j + 4], template_upward_diagonal_1)
                kernal_upward_diagonal_2 = np.multiply(self.board[i: i + 4, j: j + 4], template_upward_diagonal_2)
                kernal_upward_diagonal_3 = np.multiply(self.board[i: i + 4, j: j + 4], template_upward_diagonal_3)
                kernal_upward_diagonal_4 = np.multiply(self.board[i: i + 4, j: j + 4], template_upward_diagonal_4)

                if (np.array_equal(kernal_downward_diagonal_1, downward_diagonal_1)) or (
                np.array_equal(kernal_upward_diagonal_1, upward_diagonal_1)):
                    diagonal_strong_chances.append(6 - (i + 3))

                if (np.array_equal(kernal_downward_diagonal_2, downward_diagonal_2)) or (
                np.array_equal(kernal_upward_diagonal_2, upward_diagonal_2)):
                    diagonal_strong_chances.append(6 - i)

                if (np.array_equal(kernal_downward_diagonal_3, downward_diagonal_3)) or (
                np.array_equal(kernal_upward_diagonal_3, upward_diagonal_3)):
                    diagonal_strong_chances.append(6 - (i + 1))

                if (np.array_equal(kernal_downward_diagonal_4, downward_diagonal_4)) or (
                np.array_equal(kernal_upward_diagonal_4, upward_diagonal_4)):
                    diagonal_strong_chances.append(6 - (i + 2))
        return diagonal_strong_chances

    def column_chances(self, opponent):
        if opponent:
            if self.turn == 1:
                column_chance = np.array([0, 2, 2, 2])
            else:
                column_chance = np.array([0, 1, 1, 1])
        else:
            column_chance = np.array([0, self.turn, self.turn, self.turn])

        column_win_chances = []
        for i in range(3):
            for j in range(7):
                if (np.array_equal(self.board[i: i + 4, j], column_chance)):
                    column_win_chances.append(6 - i)

        return column_win_chances

    def evaluate_state(self, played_move):
        # maximum value = 100 -> absolute win with this next move
        # minimum value = -100 -> absolute lose with this next move

        win_score = math.inf
        lose_score = -math.inf
        score = 0

        three_in_a_row_for_me = self.possible_win_chances_in_rows(opponent=0)
        three_in_a_row_for_the_enemy = self.possible_win_chances_in_rows(opponent=1)

        two_in_a_row_for_me = self.two_in_a_row(opponent=0)
        two_in_a_row_for_the_enemy = self.two_in_a_row(opponent=1)

        diagonal_chances_for_me = self.diagonal_strong_chance(opponent=0)
        diagonal_chances_for_the_enemy = self.diagonal_strong_chance(opponent=1)

        vertical_chances_for_me = self.column_chances(opponent=0)
        vertical_chances_for_the_enemy = self.column_chances(opponent=1)

        if (self.win()):
            if self.turn == 2:  # AI won
                return win_score
            else:
                return lose_score

        if played_move == 3:  # board center
            score += 5

        if len(three_in_a_row_for_me) != 0:
            # print('hi 3 in a row')
            for i in three_in_a_row_for_me:
                score += 4

        if len(three_in_a_row_for_the_enemy) != 0:
            # print('enemy 3 in a row')
            for i in three_in_a_row_for_the_enemy:
                score -= 4

        if len(two_in_a_row_for_me) != 0:
            # print('hi 2 in a row')

            for i in two_in_a_row_for_me:
                score += 2

        if len(two_in_a_row_for_the_enemy) != 0:
            # print('enemy 2 in a row')

            for i in two_in_a_row_for_the_enemy:
                score -= 2

        if len(diagonal_chances_for_me) != 0:
            # print('hi diagonal chances')

            for i in diagonal_chances_for_me:
                score += 4

        if len(diagonal_chances_for_the_enemy) != 0:
            # print('enemy diagonal chances')
            for i in diagonal_chances_for_the_enemy:
                score -= 4

        if len(vertical_chances_for_me) != 0:
            # print('hi vertical')

            for i in vertical_chances_for_me:
                score += 4

        if len(vertical_chances_for_the_enemy) != 0:
            # print('enemy vertical')

            for i in vertical_chances_for_the_enemy:
                score -= 4

        return score


############################################################################################################################



class Game:
    width = (int)
    height = (int)
    size = (int, int)
    radius = int()

    def __init__(self):
        self.turn = 0
        self.board = GameBoard()
        self.player_1 = Player(player_id=1)
        self.player_2 = Player(player_id=2)


    def GUI_setup(self):
        pygame.init()

        self.width = COL_NO * SQUARESIZE
        self.height = (ROW_NO + 1) * SQUARESIZE
        self.size = (self.width,self.height)
        self.radius = int(SQUARESIZE/2 - 10)
        self.font = pygame.font.SysFont("monospace", 20)
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

        #Salmaa
        def text_objects( text, font):
            textsurface = font.render(text, True, (0, 0, 0))
            return textsurface, textsurface.get_rect()


        self.GUI_setup()
        self.draw_board()

        picked = 0

        gameLevel = 0
        flagLevel = 0
        modeSelected = 0
        flagMode = 0
        red = (200, 0, 0)
        yellow = (200, 200, 0)
        bright_red = (255, 0, 0)
        bright_yellow = (255, 255, 0)
        black = (0, 0, 0)
        text = pygame.font.Font("freesansbold.ttf", 20)
        textsurface1, textrect1 = text_objects("Player 1", text)
        textsurface2, textrect2 = text_objects("AI", text)

        textsurface3, textrect3 = text_objects("Easy", text)
        textsurface4, textrect4 = text_objects("Medium", text)
        textsurface5, textrect5 = text_objects("Hard", text)

        textsurface6, textrect6 = text_objects("Regular", text)
        textsurface7, textrect7 = text_objects("Verbose", text)

        game_end = False

        label = self.font.render('player 1 turn', 1, (255, 0, 0))
        #self.screen.blit(label, (40, 50))
        pygame.display.update()

        while (not game_end):
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            pygame.display.update()


            if gameLevel == 1 :
                gameLevel =1
                flagLevel = 1
            elif gameLevel ==2:
                gameLevel =2
                flagLevel =1
            elif gameLevel ==3:
                gameLevel = 3
                flagLevel =1

            if modeSelected ==1:
                modeSelected =1
            elif modeSelected ==2:
                modeSelected =2


            flagLevel = 0
            flagMode = 0

            # Hasb el chosen Level hnnady el minimax function b depth mo3yn kol m el depth yzed kol m yb2a as3ab
            if modeSelected == 0:
                if 10 + 100 > mouse[0] > 10 and 40 + 50 > mouse[1] > 40 :
                    pygame.draw.rect(self.screen, (200, 200, 200), (10, 40, 100, 50))
                    if click[0] == 1 :
                        modeSelected = 1
                        flagMode = 1
                        print("regular mode selected")
                else:
                    pygame.draw.rect(self.screen, (255, 255, 255), (10, 40, 100, 50))

                if 130 + 100 > mouse[0] > 130 and 40 + 50 > mouse[1] > 40 :
                    pygame.draw.rect(self.screen, (200, 200, 200), (130, 40, 100, 50))
                    if click[0] == 1:
                        modeSelected = 2
                        flagMode = 1
                        # hena b2a hntala3 el info el 2al 3aleha
                        print("verbose mode selected")
                else:
                    pygame.draw.rect(self.screen, (255, 255, 255), (130, 40, 100, 50))

                textrect6.center = ((10 + (100 / 2)), (40 + (50 / 2)))
                self.screen.blit(textsurface6, textrect6)
                textrect7.center = ((130 + (100 / 2)), (40 + (50 / 2)))
                self.screen.blit(textsurface7, textrect7)

                label = self.font.render('Pick the mode of the game', 1, (255, 255, 255))
                self.screen.blit(label, (10, 5))
            if flagMode == 1:
                pygame.draw.rect(self.screen, black, (10, 40, 100, 50))
                pygame.draw.rect(self.screen, black, (130, 40, 100, 50))
                pygame.draw.rect(self.screen, black, (10, 5, 500, 50))
            if gameLevel == 0 and modeSelected != 0:
                if 240 + 80 > mouse[0] > 240 and 40 + 50 > mouse[1] > 40 :
                    pygame.draw.rect(self.screen, (200, 200, 200), (240, 40, 80, 50))
                    if click[0] == 1:
                        gameLevel = 1
                        flagLevel = 1
                        print("chosen level: Easy")
                else:
                    pygame.draw.rect(self.screen, (255, 255, 255), (240, 40, 80, 50))
                if 330 + 80 > mouse[0] > 330 and 40 + 50 > mouse[1] > 40 :
                    pygame.draw.rect(self.screen, (200, 200, 200), (330, 40, 80, 50))
                    if click[0] == 1:
                        gameLevel = 2
                        flagLevel = 1
                        print("chosen level: Medium")
                else:
                    pygame.draw.rect(self.screen, (255, 255, 255), (330, 40, 80, 50))

                if 420 + 80 > mouse[0] > 420 and 40 + 50 > mouse[1] > 40 :
                    pygame.draw.rect(self.screen, (200, 200, 200), (420, 40, 80, 50))
                    if click[0] == 1:
                        gameLevel = 3
                        flagLevel = 1
                        print("chosen level: Hard")
                else:
                    pygame.draw.rect(self.screen, (255, 255, 255), (420, 40, 80, 50))

                textrect3.center = ((240 + (80 / 2)), (40 + (50 / 2)))
                self.screen.blit(textsurface3, textrect3)
                textrect4.center = ((330 + (80 / 2)), (40 + (50 / 2)))
                self.screen.blit(textsurface4, textrect4)
                textrect5.center = ((420 + (80 / 2)), (40 + (50 / 2)))
                self.screen.blit(textsurface5, textrect5)

                label = self.font.render('Pick the level of the game', 1, (255, 255, 255))
                self.screen.blit(label, (10, 5))
            if flagLevel == 1 and modeSelected != 0:
                pygame.draw.rect(self.screen, black, (240, 40, 80, 50))
                pygame.draw.rect(self.screen, black, (330, 40, 80, 50))
                pygame.draw.rect(self.screen, black, (420, 40, 80, 50))
                pygame.draw.rect(self.screen, black, (10, 5, 500, 50))
            if picked == 1 and gameLevel != 0 and modeSelected != 0:
                picked = 1

                pygame.draw.rect(self.screen, (0, 0, 0), (510, 40, 80, 50))
                pygame.draw.rect(self.screen, (0, 0, 0), (600, 40, 50, 50))
                pygame.draw.rect(self.screen, (0, 0, 0), (10, 5, 900, 50))
            elif picked == 0 and gameLevel != 0 and modeSelected != 0:
                label = self.font.render('Pick which player will start the game', 1, (255, 255, 255))
                self.screen.blit(label, (10, 5))
                if 510 + 80 > mouse[0] > 510 and 40 + 50 > mouse[1] > 40 :
                    pygame.draw.rect(self.screen, bright_red, (510, 40, 80, 50))
                    if  click[0] == 1:
                        picked = 1
                        self.board.turn = 1
                    # print("Clicked Red!")
                    # print("player chosen : ",playerChosen)

                else:
                    pygame.draw.rect(self.screen, red, (510, 40, 80, 50))

                if 600 + 50 > mouse[0] > 600 and 40 + 50 > mouse[1] > 40 :
                    pygame.draw.rect(self.screen, bright_yellow, (600, 40, 50, 50))
                    if  click[0] == 1:
                        picked = 1
                        self.board.turn = 2
                        # print("Clicked Yellow!")
                    # print("player chosen : ", playerChosen)

                else:
                    pygame.draw.rect(self.screen, yellow, (600, 40, 50, 50))

                textrect1.center = ((510 + (80 / 2)), (40 + (50 / 2)))
                self.screen.blit(textsurface1, textrect1)
                textrect2.center = ((600 + (50 / 2)), (40 + (50 / 2)))
                self.screen.blit(textsurface2, textrect2)

            pygame.display.update()


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()


                if event.type == pygame.MOUSEBUTTONDOWN and picked ==1:

                    x = event.pos[0]
                    place = int(x/SQUARESIZE)

                    if self.board.possible(place):

                        if(self.board.turn == 1):
                            self.player_1.play_move(self.board.board,place)
                            self.board.turn = 2
                            label = self.font.render('player ' + str(self.board.turn) + ' turn', 1, (255, 255, 0))


                        else:
                            self.player_2.simulate_ai_move(self.board, depth = 2)
                        #   self.player_2.play_move(self.board.board, place)
                            self.board.turn = 1
                            label = self.font.render('player ' + str(self.board.turn) + ' turn', 1, (255, 0, 0))


                        self.draw_board()
                        self.screen.fill(pygame.Color("black"), (40, 50, 300, 50))
                        self.screen.blit(label, (40, 50))
                        pygame.display.update()

                    if (self.board.full() or self.board.win()):
                        game_end = True
                        if (self.board.win()):

                            if(self.board.turn == 2): # Player 1 Wins

                                label = self.font.render('***** player 1 wins *****', 1,
                                                         (255, 0, 0))
                                self.screen.blit(label, (40, 10))

                            elif(self.board.turn == 1): # Player 2 Wins

                                label = self.font.render('***** player 2 wins *****', 1,
                                                         (255,255, 0))
                                self.screen.blit(label, (40, 10))


                        else:
                            label = self.font.render('***** TIE ! *****' , 1, (255,255,255))
                            self.screen.blit(label,(40,10))



                        #wait 7 seconds before exist
                        pygame.display.update()
                        pygame.time.wait(3000)
hi = Game()
hi.simulate_game()

