"""
Tic Tac Toe Player
"""

import copy

X = "X"
O = "O"
EMPTY = None

def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

def player(board):
    count = sum(row.count(EMPTY) for row in board)
    if count % 2 == 1:
        return X
    else:
        return O

def actions(board):
    result = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                result.add((i, j))
    return result

def result(board, action):
    if board[action[0]][action[1]] is not EMPTY:
        raise Exception("Invalid action")
    if action[0] not in range(3) or action[1] not in range(3):
        raise Exception("Invalid move")
    new_board = copy.deepcopy(board)
    new_board[action[0]][action[1]] = player(board)
    return new_board

def winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != EMPTY:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != EMPTY:
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[1][1]
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[1][1]
    return None

def terminal(board):
    return winner(board) is not None or sum(row.count(EMPTY) for row in board) == 0

def utility(board):
    w = winner(board)
    if w == X:
        return 1
    elif w == O:
        return -1
    else:
        return 0

def minimax(board):
    if terminal(board):
        return None
    if player(board) == X:
        return max_value(board)[1]
    else:
        return min_value(board)[1]

def max_value(board):
    if terminal(board):
        return (utility(board), None)

    best_value = -float('inf')
    best_move = None
    for move in actions(board):
        (v, _) = min_value(result(board, move))
        if v > best_value:
            best_value = v
            best_move = move
    return (best_value, best_move)

def min_value(board):
    if terminal(board):
        return (utility(board), None)

    best_value = float('inf')
    best_move = None
    for move in actions(board):
        (v, _) = max_value(result(board, move))
        if v < best_value:
            best_value = v
            best_move = move
    return (best_value, best_move)