"""
8 Puzzle Agent
"""
import copy
import math

EMPTY = ""


def empty_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def initial_state():
    """
    Returns starting state of the board.
    """
    return [["1", "2", "5"],
            ["3", "4", EMPTY],
            ["6", "7", "8"]]


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board and the zero.
    """
    possible_moves = set()
    zero = tuple()
    for i in range(0, 3):
        for j in range(0, 3):
            if board[i][j] == EMPTY:
                zero = (i, j)
                possible_moves.add((i + 1, j))
                possible_moves.add((i - 1, j))
                possible_moves.add((i, j + 1))
                possible_moves.add((i, j - 1))
                break
    if len(possible_moves) == 0:
        return None
    else:
        return possible_moves, zero


def result(board, action, zero):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    new_board = empty_state()
    for i in range(0, 3):
        for j in range(0, 3):
            new_board[i][j] = copy.deepcopy(board[i][j])

    if new_board[action[0]][action[1]] != EMPTY:
        raise Exception
    else:
        temp = new_board[action[0]][action[1]]
        new_board[action[0]][action[1]] = new_board[zero[0]][zero[1]]
        new_board[zero[0]][zero[1]] = temp

        return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if (board[0][0] == "" and board[0][1] == "1" and board[0][2] == "2"
            and board[1][0] == "3" and board[1][1] == "4" and board[1][2] == "5"
            and board[2][0] == "6" and board[2][1] == "7" and board[2][2] == "8"):
        return True
    else:
        return False


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board):
        return True
    else:
        return False


def DFS(board):
    """
    Returns the next action for the current state on the board.
    """
    return None


def BFS(board, predecessor_v):
    """
    Returns the next action for the current state on the board.
    """
    return None


def AStar(board, predecessor_v):
    """
    Returns the next action for the current state on the board.
    """

    return None
