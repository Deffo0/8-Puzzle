"""
8 Puzzle Agent
"""
import copy
import sys
import math
from queue import PriorityQueue
import time
import heapdict

EMPTY = ""


class State():
    """
    State of puzzle
    """

    def __init__(self, grid, parent_state):
        self.grid = grid
        self.parent_state = parent_state
        self.distance = 0
        self.stringFormat = ""
        for i in range(3):
            for j in range(3):
                self.stringFormat += self.grid[i][j]


class StackFrontier:
    """
    Frontier used for DFS search
    """

    def __init__(self):
        self.frontier = []
        self.max_size = 0

    def add(self, state):
        self.frontier.append(state)
        self.max_size = max(self.max_size, len(self.frontier))

    def pop(self):
        returned_state = self.frontier[-1]
        self.frontier = self.frontier[:-1]
        return returned_state

    def not_empty(self):
        return len(self.frontier) > 0


class QueueFrontier:
    """
    Fringe used for BFS search
    """

    def __init__(self):
        self.frontier = []
        self.max_size = 0

    def add(self, state):
        self.frontier.append(state)
        self.max_size = max(self.max_size, len(self.frontier))

    def pop(self):
        returned_state = self.frontier[0]
        self.frontier = self.frontier[1:]
        return returned_state

    def not_empty(self):
        return len(self.frontier) > 0


def empty_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def initial_state(user_text):
    """
    Returns starting state of the board.
    """
    matrix = []
    row = []
    ctr = 0
    if len(user_text) > 9:
        sys.exit(0)
    for num in list(user_text):
        if ctr == 3:
            ctr = 0
            matrix.append(row)
            row = []
        row.append(num)
        ctr += 1
    matrix.append(row)
    return matrix


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board and the zero.
    """
    possible_moves = set()
    zero = tuple()
    for i in range(0, 3):
        for j in range(0, 3):
            if board[i][j] == '0':
                zero = (i, j)
                if allowed_action(i - 1, j):
                    possible_moves.add((i - 1, j))
                if allowed_action(i + 1, j):
                    possible_moves.add((i + 1, j))
                if allowed_action(i, j - 1):
                    possible_moves.add((i, j - 1))
                if allowed_action(i, j + 1):
                    possible_moves.add((i, j + 1))
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

    if new_board[zero[0]][zero[1]] != '0':
        raise Exception
    else:
        temp = new_board[action[0]][action[1]]
        new_board[action[0]][action[1]] = new_board[zero[0]][zero[1]]
        new_board[zero[0]][zero[1]] = temp

        return new_board


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if (board[0][0] == "0" and board[0][1] == "1" and board[0][2] == "2"
            and board[1][0] == "3" and board[1][1] == "4" and board[1][2] == "5"
            and board[2][0] == "6" and board[2][1] == "7" and board[2][2] == "8"):

        return True
    else:
        return False


def get_empty_tile(state: State):
    for i in range(0, 3):
        for j in range(0, 3):
            if state.grid[i][j] == "0":
                return i, j
    return -1, -1


def detect_action(state):
    """
        return: action used to move from a parent state to the given state
    """
    row_of_state, col_of_state = get_empty_tile(state)
    row_of_parent_state, col_of_parent_state = get_empty_tile(state.parent_state)
    if row_of_state == row_of_parent_state:
        return "Right" if col_of_parent_state < col_of_state else "Left"
    return "Down" if row_of_parent_state < row_of_state else "Up"


def back_track(state):
    """
    :param state: Winner (final) state of the puzzle
    :return: Stack containing the parent chain starting from final state ending at initial state
    """
    stack, stack_of_actions = [], []
    stack.append(state)
    parent = state.parent_state
    while parent is not None:
        stack_of_actions.append(detect_action(state))
        stack.append(parent)
        state = parent
        parent = parent.parent_state
    stack_of_actions.reverse()
    return stack, str(len(stack) - 1), stack_of_actions


def good_print(grid):
    """
    :param grid: Grid of the puzzle
    prints the grid
    """
    for row in grid:
        for element in row:
            print(element, end=" ")
        print("\n", end="")
    print("\n", end="")


def isPresent(state, list_of_states):
    """
    :param state: State of the puzzle
    :param list_of_states: List to be searched in
    :return: true if the state already exists in the list
    """
    print(any(l.grid == state.grid for l in list_of_states))
    return any(l.grid == state.grid for l in list_of_states)


def allowed_action(i, j):
    """

    :param i: X Coordinate of the cell to be swapped with empty cell
    :param j: X Coordinate of the cell to be swapped with empty cell
    :return: true if the cell is within the constraints of the puzzle
    """
    return 0 <= i < 3 and 0 <= j < 3


class ManhattanDistance:

    def distance(self, index: str, x2, y2):
        if int(index) == 0:
            return 0
        x1 = int(int(index) / 3)
        y1 = int(index) % 3
        return abs(x1 - x2) + abs(y1 - y2)

    def calculate(self, state: State):
        sum = 0
        for i in range(3):
            for j in range(3):
                sum += self.distance(state.grid[i][j], i, j)
        return sum


class EuclidianDistance:

    def distance(self, index: str, x2, y2):
        if int(index) == 0:
            return 0
        x1 = int(int(index) / 3)
        y1 = int(index) % 3
        return math.sqrt(((x1 - x2) ** 2 + (y1 - y2) ** 2))

    def calculate(self, state: State):
        sum = 0
        for i in range(3):
            for j in range(3):
                sum += self.distance(state.grid[i][j], i, j)
        return sum


def calculateHeruistic(state: State, function):
    return function.calculate(state)


def DFS(board):
    """
    :param board: starting state grid of the puzzle
    :return Searches for the way to solve the puzzle
    and returns stack of states leading to the solution
    starting at final state (Goal) and ending at initial_state
    """
    start = time.time()
    frontier = StackFrontier()
    visited_states = set()
    frontier_set = set()
    init_state = State(board, None)
    frontier.add(init_state)
    frontier_set.add(init_state.stringFormat)
    max_depth = 0
    while frontier.not_empty():
        state = frontier.pop()
        max_depth = max(max_depth, state.distance)
        frontier_set.remove(state.stringFormat)
        visited_states.add(state.stringFormat)

        if terminal(state.grid):
            print_state_and_its_parent(state)
            stack, cost_and_depth, actions_to_solve = back_track(state)
            return stack, cost_and_depth, actions_to_solve, len(visited_states), frontier.max_size, len(
                frontier.frontier), max_depth, (time.time() - start)

        set_of_actions, zero = actions(state.grid)
        for action in set_of_actions:
            next_state = State(result(state.grid, action, zero), state)
            next_state.distance = state.distance + 1
            if (not (next_state.stringFormat in visited_states)) and (not (next_state.stringFormat in frontier_set)):
                frontier.add(next_state)
                frontier_set.add(next_state.stringFormat)

    return None, math.inf, None, len(visited_states), frontier.max_size, len(frontier.frontier), max_depth, (
                time.time() - start)


def BFS(board):
    """
    :param board: starting state grid of the puzzle
    :return Searches for the way to solve the puzzle
    and returns stack of states leading to the solution
    starting at final state (Goal) and ending at initial_state
    """
    start = time.time()
    frontier = QueueFrontier()
    visited_states = set()
    frontier_set = set()
    init_state = State(board, None)
    frontier.add(init_state)
    frontier_set.add(init_state.stringFormat)
    max_depth = 0
    while frontier.not_empty():
        state = frontier.pop()
        max_depth = max(state.distance, max_depth)
        frontier_set.remove(state.stringFormat)
        visited_states.add(state.stringFormat)

        if terminal(state.grid):
            print_state_and_its_parent(state)
            stack, cost_and_depth, actions_to_solve = back_track(state)
            return stack, cost_and_depth, actions_to_solve, len(visited_states), frontier.max_size, len(
                frontier.frontier), max_depth, (time.time() - start)

        set_of_actions, zero = actions(state.grid)
        for action in set_of_actions:
            next_state = State(result(state.grid, action, zero), state)
            next_state.distance = state.distance + 1
            if (not (next_state.stringFormat in visited_states)) and (not (next_state.stringFormat in frontier_set)):
                frontier.add(next_state)
                frontier_set.add(next_state.stringFormat)
    return None, math.inf, None, len(visited_states), frontier.max_size, len(frontier.frontier), max_depth, (
                time.time() - start)


def AStar(board, function):
    """
    Returns the next action for the current state on the board.
    """
    start = time.time()
    frontier = heapdict.heapdict()
    visited_states = set()
    frontier_set = set()
    init_state = State(board, None)
    frontier[init_state] = calculateHeruistic(init_state, function)
    frontier_set.add(init_state.stringFormat)
    max_fringe_size = 0
    while len(frontier) > 0:
        state, dist2 = frontier.popitem()
        dist = state.distance
        frontier_set.remove(state.stringFormat)
        visited_states.add(state.stringFormat)

        if terminal(state.grid):
            print_state_and_its_parent(state)
            stack, cost_and_depth, actions_to_solve = back_track(state)
            return stack, cost_and_depth, actions_to_solve, len(visited_states), max_fringe_size, len(frontier), (
                        time.time() - start)

        set_of_actions, zero = actions(state.grid)
        for action in set_of_actions:
            next_state = State(result(state.grid, action, zero), state)
            if dist + 1 < next_state.distance:
                next_state.parent_state = state
                next_state.distance = dist + 1
            if (not (next_state.stringFormat in visited_states)) and (not (next_state.stringFormat in frontier_set)):
                heuristic = calculateHeruistic(next_state, function)
                frontier[next_state] = next_state.distance + heuristic
                frontier_set.add(next_state.stringFormat)
                max_fringe_size = max(max_fringe_size, len(frontier))
    return None, math.inf, None, len(visited_states), max_fringe_size, len(frontier), (time.time() - start)


def print_state_and_its_parent(state):
    print(f"Goal State: {state.grid}")
    print(f"Pre-Goal State: {state.parent_state.grid}")


def print_Res_fs(cost_and_depth, actions_to_solve, explored, fringe_max_size, fringe_size, max_depth, run_time):
    print(f"Actions to do: {actions_to_solve}")
    print(f"cost-to-goal: {cost_and_depth}")
    print(f"depth-to-goal: {cost_and_depth}")
    print(f"nodes explored: {explored}")
    print(f"Max. fringe size: {fringe_max_size}")
    print(f"Fringe size: {fringe_size}")
    print(f"Max. depth: {max_depth}")
    print(f"running time: {run_time} seconds")


def print_Res_astar(cost_and_depth, actions_to_solve, explored, fringe_max_size, fringe_size, run_time):
    print(f"Actions to do: {actions_to_solve}")
    print(f"cost-to-goal: {cost_and_depth}")
    print(f"depth-to-goal: {cost_and_depth}")
    print(f"nodes explored: {explored}")
    print(f"Max. fringe size: {fringe_max_size}")
    print(f"Fringe size: {fringe_size}")
    print(f"running time: {run_time} seconds")
