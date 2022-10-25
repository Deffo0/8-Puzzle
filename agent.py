"""
8 Puzzle Agent
"""
import copy
import math
import sys
import time
from queue import PriorityQueue

import heapdict

EMPTY = ""


def getGrid(state : str): 
    grid = []
    ctr = 0
    for i in range(3):
        grid.append(list())
        for j in range(3):
            grid[i].append(state[ctr])
            ctr += 1
    return grid


class State():
    """
    State of puzzle
    """

    def __init__(self, state : str, grid):
        self.grid = grid
        self.stringState = state
        self.distance = math.inf
    

def getStringFormat(grid):
    stringFormat = ""
    for i in range(3):
        for j in range(3):
            stringFormat += grid[i][j]
    return stringFormat

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


#done
def get_empty_tile(state: str):
    grid = getGrid(state)
    for i in range(0, 3):
        for j in range(0, 3):
            if grid[i][j] == "0":
                return i, j
    return -1, -1


def empty_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


#done
def moveBlank(grid, x1, y1, x2, y2):
    stringFormat = ""
    temp = grid[x2][y2]
    grid[x2][y2] = '0'
    grid[x1][y1] = temp
    stringFormat = getStringFormat(grid)
    temp = grid[x1][y1]
    grid[x1][y1] = "0"
    grid[x2][y2] = temp
    return stringFormat

#done
def getNextStates(state : str):
    """
    Returns set of all possible actions (i, j) available on the board and the zero.
    """
    states = []
    grid = getGrid(state)
    i, j = get_empty_tile(state)
    if allowed_action(i - 1, j):
        states.append(moveBlank(grid, i, j, i - 1, j))
    if allowed_action(i + 1, j):
        states.append(moveBlank(grid, i, j, i + 1, j))
    if allowed_action(i, j - 1):
        states.append(moveBlank(grid, i, j, i, j - 1))
    if allowed_action(i, j + 1):
        states.append(moveBlank(grid, i, j, i, j + 1))
    return states


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


#done
def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    return board == "012345678"



#done
def detect_action(state, parent_state):
    """
        return: action used to move from a parent state to the given state
    """
    row_of_state, col_of_state = get_empty_tile(state)
    row_of_parent_state, col_of_parent_state = get_empty_tile(parent_state)
    if row_of_state == row_of_parent_state:
        return "Right" if col_of_parent_state < col_of_state else "Left"
    return "Down" if row_of_parent_state < row_of_state else "Up"


#done
def back_track(state : str, parent_map : dict):
    """
    :param state: Winner (final) state of the puzzle
    :return: Stack containing the parent chain starting from final state ending at initial state
    """

    current_state = state
        
    stack, stack_of_actions = [], []
    stack.append(State(current_state, getGrid(current_state)))

    while(current_state != parent_map[current_state]):
        stack_of_actions.append(detect_action(current_state, parent_map[current_state]))
        stack.append(State(parent_map[current_state], getGrid(parent_map[current_state])))
        current_state = parent_map[current_state]

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



def allowed_action(i, j):
    """

    :param i: X Coordinate of the cell to be swapped with empty cell
    :param j: X Coordinate of the cell to be swapped with empty cell
    :return: true if the cell is within the constraints of the puzzle
    """
    return 0 <= i < 3 and 0 <= j < 3


#done
class ManhattanDistance:

    def distance(self, index: str, x2, y2):
        if int(index) == 0:
            return 0
        x1 = int(int(index) / 3)
        y1 = int(index) % 3
        return abs(x1 - x2) + abs(y1 - y2)

    def calculate(self, state: str):
        grid = getGrid(state)
        sum = 0
        for i in range(3):
            for j in range(3):
                sum += self.distance(grid[i][j], i, j)
        return sum


#done
class EuclidianDistance:

    def distance(self, index: str, x2, y2):
        if int(index) == 0:
            return 0
        x1 = int(int(index) / 3)
        y1 = int(index) % 3
        return math.sqrt(((x1 - x2) ** 2 + (y1 - y2) ** 2))

    def calculate(self, state: str):
        grid = getGrid(state)
        sum = 0
        for i in range(3):
            for j in range(3):
                sum += self.distance(grid[i][j], i, j)
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
    parent_map = dict()
    state_dist_dic = dict()
    init_state = getStringFormat(board)
    parent_map[init_state] = init_state
    state_dist_dic[init_state] = 0
    frontier.add(init_state)
    frontier_set.add(init_state)
    max_depth = 0
    while frontier.not_empty():
        state = frontier.pop()
        max_depth = max(state_dist_dic[state], max_depth)

        frontier_set.remove(state)
        visited_states.add(state)

        if terminal(state):
            print_state_and_its_parent(state, parent_map[state])
            stack, cost_and_depth, actions_to_solve = back_track(state, parent_map)
            return stack, cost_and_depth, actions_to_solve, len(visited_states), frontier.max_size, len(
                frontier.frontier), max_depth, (time.time() - start)

        next_states = getNextStates(state)
        for next_state in next_states:

            if (not (next_state in visited_states)) and (not (next_state in frontier_set)):
                state_dist_dic[next_state] = state_dist_dic[state] + 1
                parent_map[next_state] = state
                frontier.add(next_state)
                frontier_set.add(next_state)

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
    parent_map = dict()
    state_dist_dic = dict()
    init_state = getStringFormat(board)
    parent_map[init_state] = init_state
    state_dist_dic[init_state] = 0
    frontier.add(init_state)
    frontier_set.add(init_state)
    max_depth = 0
    while frontier.not_empty():
        state = frontier.pop()
        max_depth = max(state_dist_dic[state], max_depth)
        frontier_set.remove(state)
        visited_states.add(state)

        if terminal(state):
            print_state_and_its_parent(state, parent_map[state])
            stack, cost_and_depth, actions_to_solve = back_track(state, parent_map)
            return stack, cost_and_depth, actions_to_solve, len(visited_states), frontier.max_size, len(
                frontier.frontier), max_depth, (time.time() - start)

        next_states = getNextStates(state)

        for next_state in next_states:
            if (not (next_state in visited_states)) and (not (next_state in frontier_set)):
                state_dist_dic[next_state] = state_dist_dic[state] + 1
                parent_map[next_state] = state
                frontier.add(next_state)
                frontier_set.add(next_state)

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
    state_dist_dic = dict()
    parent_map = dict()
    init_state = getStringFormat(board)
    parent_map[init_state] = init_state
    state_dist_dic[init_state] = 0
    frontier[init_state] = calculateHeruistic(init_state, function)
    frontier_set.add(init_state)
    max_fringe_size = 0
    while len(frontier) > 0:
        state, cost = frontier.popitem()
        dist = state_dist_dic[state]
        frontier_set.remove(state)
        visited_states.add(state)

        if terminal(state):
            print_state_and_its_parent(state, parent_map[state])
            stack, cost_and_depth, actions_to_solve = back_track(state, parent_map)
            return stack, cost_and_depth, actions_to_solve, len(visited_states), max_fringe_size, len(frontier), (
                        time.time() - start)

        next_states = getNextStates(state)
        for next_state in next_states:
            heuristic = calculateHeruistic(next_state, function)
            if (not (next_state in visited_states)) and (not (next_state in frontier_set)):
                parent_map[next_state] = state
                state_dist_dic[next_state] = dist + 1
                frontier[next_state] = state_dist_dic[next_state] + heuristic
                frontier_set.add(next_state)
                max_fringe_size = max(max_fringe_size, len(frontier))
            elif (next_state in frontier_set):
                if dist + 1 < state_dist_dic[next_state]:
                    parent_map[next_state] = state
                    state_dist_dic[next_state] = dist + 1
                    frontier[next_state] = state_dist_dic[next_state] + heuristic

    return None, math.inf, None, len(visited_states), max_fringe_size, len(frontier), (time.time() - start)


def print_state_and_its_parent(state, parent_state):
    print(f"Goal State: {state}")
    print(f"Pre-Goal State: {parent_state}")


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


