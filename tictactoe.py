"""
Tic Tac Toe Player
"""
import copy
import math

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
    moves = 0
    for i in board:
        for j in i:
            if j != EMPTY: moves+=1
    if moves % 2 == 0: return X
    return O


def actions(board):
    available_actions = set()
    for i in range (len(board)):
        for j in range (len(board[0])):
            if board[i][j] == EMPTY: available_actions.add((i, j))
    return available_actions

def result(board, action):
    new_board = copy.deepcopy(board)

    y = action[0]
    x = action[1]

    if new_board[y][x] == EMPTY:
        new_board[y][x] = player(board)
        return new_board
    raise ValueError


def winner(board):
    for i in range (len(board)):
        if board[i][0] == board[i][1] == board[i][2]:
            if board[i][0] != EMPTY:
                return board[i][0]

    for i in range (len(board[0])):
        if board[0][i] == board[1][i] == board[2][i]:
            if board[0][i] != EMPTY:
                return board[0][i]

    if board[1][1] != EMPTY:
        if board[0][0] == board[1][1] == board[2][2]: return board[0][0]
        if board[0][2] == board[1][1] == board[2][0]: return board[0][2]

    return None

def terminal(board):
    if winner(board) is not None: return True

    for i in board:
        for j in i:
            if j == EMPTY: return False

    return True


def utility(board):
    if winner(board) == X: return 1
    if winner(board) == O: return -1
    return 0


def minimax(board):
    if terminal(board): return None

    best_move = None

    if player(board) == X:
        best_score = -2
        for action in actions(board):
            score = minimal(result(board, action))
            if score > best_score:
                best_move = action
                best_score = score

    if player(board) == O:
        best_score = 2
        for action in actions(board):
            score = maximal(result(board, action))
            if score < best_score:
                best_move = action
                best_score = score

    return best_move

def minimal(board):
    if terminal(board): return utility(board)
    value = 2

    for action in actions(board): value = min(value, maximal(result(board, action)))
    return value

def maximal(board):
    if terminal(board): return utility(board)
    value = -2

    for action in actions(board): value = max(value, minimal(result(board, action)))
    return value