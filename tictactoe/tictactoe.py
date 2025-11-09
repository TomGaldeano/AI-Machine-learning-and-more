"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None
def new_board(board):
    board_copy = initial_state()
    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                board_copy[i][j] = X
            if board[i][j] == O:
                board_copy[i][j] = O
    return board_copy

def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    number_moves = 9
    for i in board:
        number_moves -= i.count(None)
    if number_moves%2 == 1:
        return O
    else:
        return X
    

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = []
    for i in range(3):
        for j in range(3):
            if not board[i][j]:
                possible_actions.append((i,j))
    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    board[action[0]][action[1]] = player(board)
    return board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if board[0].count(X) == 3 or board[1].count(X) == 3 or board[2].count(X) == 3:
        return X
    elif board[0].count(O) == 3 or board[1].count(O) == 3 or board[2].count(O) == 3:
        return O
    elif board[0][0] == board[1][0] == board[2][0] != None:
        if board[0][0] == X:
            return X
        else:
            return O
    elif board[0][1] == board[1][1] == board[2][1] != None:
        if board[0][1] == X:
            return X
        else:
            return O
    elif board[0][2] == board[1][2] == board[2][2] != None:
        if board[0][0] == X:
            return X
        else:
            return O
    elif board[0][0] == board[1][1] == board[2][2] != None:
        if board[0][0] == X:
            return X
        else:
            return O
    elif board[0][2] == board[1][1] == board[2][0] != None:
        if board[0][2] == X:
            return X
        else:
            return O


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if board[0].count(None) == board[1].count(None) == board[2].count(None) == 0:
        return True  
    elif board[0].count(X) == 3 or board[1].count(X) == 3 or board[2].count(X) == 3:
        return True
    elif board[0].count(O) == 3 or board[1].count(O) == 3 or board[2].count(O) == 3:
        return True
    elif board[0][0] == board[1][0] == board[2][0] != None:
        return True
    elif board[0][1] == board[1][1] == board[2][1] != None:
        return True
    elif board[0][2] == board[1][2] == board[2][2] != None:
        return True
    elif board[0][0] == board[1][1] == board[2][2] != None:
        return True
    elif board[0][2] == board[1][1] == board[2][0] != None:
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    a = winner(board)
    if a == X:
        return 10
    elif a == O:
        return -10
    else:
        return 0


def max_value(board):
    if terminal(board):
        return utility(board)
    v = -1000
    for action in actions(board):
        board_copy = new_board(board)
        v = max(v,min_value(result(board_copy,action)))
    return v

def min_value(board):
    if terminal(board):
        return utility(board)
    v = 1000
    for action in actions(board):
        board_copy = new_board(board)
        v = min(v,max_value(result(board_copy,action)))
    return v



def minimax_gpt(board, depth, is_maximizing):
    score = utility(board)
    if score == 10:
        return score - depth
    if score == -10:
        return score + depth
    if terminal(board):
        return 0
    if is_maximizing:
        best = -float("inf")
        for i in range(3):
            for j in range(3):
                if board[i][j] == None:
                    board[i][j] = 'X'
                    best = max(best, minimax_gpt(board, depth + 1, not is_maximizing))
                    board[i][j] = None
        return best
    else:
        best = float("inf")
        for i in range(3):
            for j in range(3):
                if board[i][j] == None:
                    board[i][j] = 'O'
                    best = min(best, minimax_gpt(board, depth + 1, not is_maximizing))
                    board[i][j] = None
        return best


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if player(board) == X:
        best_move = (-1, -1)
        best_val = -float("inf")
        for i in range(3):
            for j in range(3):
                if board[i][j] == None:
                    board[i][j] = player(board)
                    move_val = minimax_gpt(board, 0, False)
                    board[i][j] = None
                    if move_val > best_val:
                        best_move = (i, j)
                        best_val = move_val
    else:
        best_move = (-1, -1)
        best_val = float("inf")
        for i in range(3):
            for j in range(3):
                if board[i][j] == None:
                    board[i][j] = player(board)
                    move_val = minimax_gpt(board, 1, True)
                    board[i][j] = None
                    if move_val < best_val:
                        best_move = (i, j)
                        best_val = move_val



    return best_move
