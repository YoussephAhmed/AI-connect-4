import numpy as np
import pygame
import sys


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

        for i in range(6):
            if board[5-i, j] == 0:
                board[5-i, j] = self.player_id
                return

    def smart_move(self,board):
        #compute the best position
        #call play_move with this move
        pass


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
        pass


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
        def text_objects( text, font):
            textsurface = font.render(text, True, (0, 0, 0))
            return textsurface, textsurface.get_rect()


        self.GUI_setup()
        self.draw_board()

        game_end = False



        picked = 0

        gameLevel = 0
        flagLevel = 0
        pygame.display.update()

        while (not game_end):
            # salma
            red = (200, 0, 0)
            yellow = (200, 200, 0)
            bright_red = (255, 0, 0)
            bright_yellow = (255, 255, 0)
            black =(0,0,0)
            text = pygame.font.Font("freesansbold.ttf", 20)
            textsurface1, textrect1 = text_objects("Player 1", text)
            textsurface2, textrect2 = text_objects("Player 2", text)

            textsurface3, textrect3 = text_objects("Easy", text)
            textsurface4, textrect4 = text_objects("Medium", text)
            textsurface5, textrect5 = text_objects("Hard", text)
            # check to see if the mouse is in the button coordinates

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
            flagLevel = 0
            # Hasb el chosen Level hnnady el minimax function b depth mo3yn kol m el depth yzed kol m yb2a as3ab
            if gameLevel == 0 :
                if 20 + 80 > mouse[0] > 20 and 40 + 50 > mouse[1] > 40 and click[0] == 1:
                    pygame.draw.rect(self.screen, (200, 200, 200), (20, 40, 80, 50))
                    gameLevel = 1
                    flagLevel =1
                    print("chosen level: Easy" )
                else:
                    pygame.draw.rect(self.screen, (255, 255, 255), (20, 40, 80, 50))
                if 300 + 80 > mouse[0] > 300 and 40 + 50 > mouse[1] > 40 and click[0] == 1:
                    pygame.draw.rect(self.screen, (200, 200, 200), (300, 40, 80, 50))
                    gameLevel = 2
                    flagLevel = 1
                    print("chosen level: Medium")
                else:
                    pygame.draw.rect(self.screen, (255, 255, 255), (300, 40, 80, 50))

                if 600 + 80 > mouse[0] > 600 and 40 + 50 > mouse[1] > 40 and click[0] == 1:
                    pygame.draw.rect(self.screen, (200, 200, 200), (600, 40, 80, 50))
                    gameLevel = 3
                    flagLevel = 1
                    print("chosen level: Hard")
                else:
                    pygame.draw.rect(self.screen, (255, 255, 255), (600, 40, 80, 50))

                textrect3.center = ((20 + (80 / 2)), (40 + (50 / 2)))
                self.screen.blit(textsurface3, textrect3)
                textrect4.center = ((300 + (80 / 2)), (40 + (50 / 2)))
                self.screen.blit(textsurface4, textrect4)
                textrect5.center = ((600 + (80 / 2)), (40 + (50 / 2)))
                self.screen.blit(textsurface5, textrect5)

                label = self.font.render('Pick the level of the game', 1, (255, 255, 255))
                self.screen.blit(label, (10, 5))
            if flagLevel == 1:
                pygame.draw.rect(self.screen, black, (20, 40, 80, 50))
                pygame.draw.rect(self.screen, black, (300, 40, 80, 50))
                pygame.draw.rect(self.screen, black, (600, 40, 80, 50))
                pygame.draw.rect(self.screen, black, (10, 5, 300, 50))

            if picked == 1 and gameLevel != 0:
                picked =1

                pygame.draw.rect(self.screen, (0,0,0), (200, 40, 150, 50))
                pygame.draw.rect(self.screen, (0,0,0), (400, 40, 150, 50))
                pygame.draw.rect(self.screen, (0,0,0), (10, 5, 900, 50))
            # if the x value of the mouse is greater than the x coordinate + the width of the button
            # same for the y coordinate
            # then we are in the boundaries of our red button
            elif picked == 0 and gameLevel != 0:
                label = self.font.render('Pick which player will start the game', 1, (255, 255, 255))
                self.screen.blit(label, (10, 5))
                if 250 + 100 > mouse[0] > 250 and 40 + 50 > mouse[1] > 40 and click[0] ==1:
                    pygame.draw.rect(self.screen, bright_red, (250, 40, 100, 50))
                    picked =1
                    self.turn = 1
                    #print("Clicked Red!")
                    #print("player chosen : ",playerChosen)

                else:
                    pygame.draw.rect(self.screen, red, (250, 40, 100, 50))

                if 400 + 100 > mouse[0] > 400 and 40 + 50 > mouse[1] > 40 and click[0] ==1:

                    picked = 1
                    self.turn = 2
                    #print("Clicked Yellow!")
                    #print("player chosen : ", playerChosen)
                    pygame.draw.rect(self.screen, bright_yellow, (400, 40, 100, 50))
                else:
                    pygame.draw.rect(self.screen, yellow, (400, 40, 100, 50))

                textrect1.center = ((250 + (100 / 2)), (40 + (50 / 2)))
                self.screen.blit(textsurface1, textrect1)
                textrect2.center = ((400 + (100 / 2)), (40 + (50 / 2)))
                self.screen.blit(textsurface2, textrect2)

            pygame.display.update()
            for event in pygame.event.get():
                #print("event type: ", event.type)
                if event.type == pygame.QUIT:
                    sys.exit()

                #print("picked now is: ",picked)

                if event.type == pygame.MOUSEBUTTONDOWN and picked ==1:

                    x = event.pos[0]
                    print("x pos: ",x)
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
                        self.screen.blit(label, (5, 50))
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
