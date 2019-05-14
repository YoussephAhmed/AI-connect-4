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

    # board = np.zeros((6,7)) # the connect 4 board is 6*7
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
            # print('row'+str(i))
            for j in range(4):
                # print(' cols'+str(j)+str(j+1)+str(j+2)+str(j+3))
                if (np.array_equal(self.board[i, j : j+4], row_1)) or (np.array_equal(self.board[i, j : j+4], row_2)):
                    return 1

        #check if there is a colomn of the same colour
        for i in range(3):
            # print('row'+str(i)+str(i+1)+str(i+2)+str(i+3))
            for j in range(7):
                # print(' cols'+str(j))
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
                # print('rows'+str(i)+str(i+1)+str(i+2)+str(i+3)+' cols'+str(j)+str(j+1)+str(j+2)+str(j+3))
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
                # print('rows'+str(i)+str(i+1)+str(i+2)+str(i+3)+' cols'+str(j+3)+str(j+2)+str(j+1)+str(j))
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









class Game:

    # turn = 1
    # 1 for player 1
    # 2 for computer
    #
    # board =  GameBoard()
    #
    # player_1 = Player()
    # computer = Player()

    def __init__(self):
        self.turn = 1
        self.board = GameBoard()
        player_1 = Player()
        computer = Player()


    def simulate_game(self): # the loop of playing

        game_end = False

        while (not game_end):

<<<<<<< HEAD
=======
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()


                if event.type == pygame.MOUSEBUTTONDOWN:

                    x = event.pos[0]
                    place = int(x/SQUARESIZE)


                    if self.board.possible(place):
                        self.board.play(self.turn, place)
                        self.draw_board()

                        #label = self.font.render('player ' + str(self.turn) + ' turn', 1, (0, 0, 0))
                        #self.screen.blit(label, (40, 50)) # clear the output screen

                        #Clear the output after every move
                        self.screen.fill(pygame.Color("black"), (40,50,300,50))



                        # flip the turns here
                        if self.turn == 1:
                            self.turn = 2
                            label = self.font.render('player ' + str(self.turn) + ' turn', 1, (255, 255, 0))

                        else:
                            self.turn = 1
                            label = self.font.render('player ' + str(self.turn) + ' turn', 1, (255, 0, 0))

>>>>>>> 26f3ce8fde4580bfef06e3a73c1349895d9adb70


            temp = input("player " + str(self.turn) + " choose a colomn: ")
            
            place = int(temp) - 1
            if place > 6 or place < 0:
                print('invalid move, try a number between 1 and 7')
                continue


            if self.board.possible(place):
                self.board.play(self.turn, place)


            print(self.board.board)

            if( self.board.full() or self.board.win()):
                game_end = True
                if (self.board.win()):
                    print('*****player '+str(self.turn)+' wins *****')

            if self.turn == 1:
                self.turn = 2
            else:
                self.turn = 1




hi = Game()
hi.simulate_game()
