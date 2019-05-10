import numpy as np

#checking array
board = np.array([[0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 2, 0, 0],
                [0, 1, 0, 2, 0, 0, 0],
                [0, 1, 2, 1, 0, 0, 0],
                [0, 0, 0, 1, 0, 0, 0],
                [0, 0, 0, 0, 1, 0, 0]])

#checking function
def check():

    #check if there is a row of the same colour
    row_1 = np.array([1, 1, 1, 1])
    row_2 = np.array([2, 2, 2, 2])

    for i in range(6):
        # print('row'+str(i))
        for j in range(4):
            # print(' cols'+str(j)+str(j+1)+str(j+2)+str(j+3))
            if (np.array_equal(board[i, j : j+4], row_1)) or (np.array_equal(board[i, j : j+4], row_2)):
                return 1

    #check if there is a colomn of the same colour
    for i in range(3):
        # print('row'+str(i)+str(i+1)+str(i+2)+str(i+3))
        for j in range(7):
            # print(' cols'+str(j))
            if (np.array_equal(board[i : i + 4, j], row_1)) or (np.array_equal(board[i : i + 4, j], row_2)):
                return 1


    #check if there is a diagonal  [[1, 0, 0, 0] of the same colour
    #                               [0, 1, 0, 0]
    #                               [0, 0, 1, 0]
    #                               [0, 0, 0, 1]
    downward_diagonal_1 = np.array([[1, 0, 0, 0],[0, 1, 0, 0],[0, 0, 1, 0],[0, 0, 0, 1]])
    downward_diagonal_2 = np.array([[2, 0, 0, 0],[0, 2, 0, 0],[0, 0, 2, 0],[0, 0, 0, 2]])
    for i in range(3):
        for j in range(4):
            board_copy = np.multiply(board[i : i + 4, j : j+4],downward_diagonal_1)
            # print('rows'+str(i)+str(i+1)+str(i+2)+str(i+3)+' cols'+str(j)+str(j+1)+str(j+2)+str(j+3))
            if (np.array_equal(board_copy, downward_diagonal_1)) or (np.array_equal(board_copy, downward_diagonal_2)):
                return 1

    #check if there is a diagonal  [[0, 0, 0, 1] of the same colour
    #                               [0, 0, 1, 0]
    #                               [0, 1, 0, 0]
    #                               [1, 0, 0, 0]
    upward_diagonal_1 = np.array([[0, 0, 0, 1],[0, 0, 1, 0],[0, 1, 0, 0],[1, 0, 0, 0]])
    upward_diagonal_2 = np.array([[0, 0, 0, 2],[0, 0, 2, 0],[0, 2, 0, 0],[2, 0, 0, 0]])
    for i in range(3):
        for j in range(4):
            board_copy = np.multiply(board[i : i + 4, j : j+4],upward_diagonal_1)
            # print('rows'+str(i)+str(i+1)+str(i+2)+str(i+3)+' cols'+str(j+3)+str(j+2)+str(j+1)+str(j))
            if (np.array_equal(board_copy, upward_diagonal_1)) or (np.array_equal(board_copy, upward_diagonal_2)):
                return 1


    return 0
print(check())
