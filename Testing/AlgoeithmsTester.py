import sys
sys.path.append("../")
import unittest
import random
import agent
from Testing.Checker import is_solvable
import Testing.file_writer


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        x = ['0', "1", '2', '3', '4', '5', '6', '7', '8']
        board, row, lin_board = [], [], []
        for i in range(0, 9):
            item = random.choice(x)
            x.remove(item)
            row.append(item)
            if i % 3 == 2:
                board.append(row)
                row = []
            lin_board.append(item)
        self.state = agent.State(board, None)
        self.my_lin_board = lin_board

    def test_dfs(self):
        stack, cost_and_depth, actions_to_solve, explored, fringe_max_size, fringe_size, max_depth, run_time = agent.DFS(self.state.grid)
        value = not (stack is None)
        expected = is_solvable(self.my_lin_board)
        file_writer.write_to_file_fs(self.state.grid, cost_and_depth, actions_to_solve, explored, fringe_max_size, fringe_size, max_depth, run_time, expected)("./Tests/dfs_tests.txt")
        self.assertEqual(value, expected)  # add assertion here

    def test_bfs(self):
        stack, cost_and_depth, actions_to_solve, explored, fringe_max_size, fringe_size, max_depth, run_time = agent.BFS(self.state.grid)
        value = not (stack is None)
        expected = is_solvable(self.my_lin_board)
        file_writer.write_to_file_fs(self.state.grid, cost_and_depth, actions_to_solve, explored, fringe_max_size, fringe_size, max_depth, run_time, expected)("./Tests/bfs_tests.txt")
        self.assertEqual(value, expected)  # add assertion here

    def test_a_star_manhattan(self):
        stack, cost_and_depth, actions_to_solve, explored, max_fringe_size, fringe_size, run_time = agent.AStar(self.state.grid, agent.ManhattanDistance())
        value = not (stack is None)
        expected = is_solvable(self.my_lin_board)
        file_writer.write_to_file_star(self.state.grid, cost_and_depth, actions_to_solve, explored, max_fringe_size, fringe_size, run_time, expected)("./Tests/a_star_manhattan_tests.txt")
        self.assertEqual(value, expected)

    def test_a_star_euclidean(self):
        stack, cost_and_depth, actions_to_solve, explored, max_fringe_size, fringe_size, run_time = agent.AStar(self.state.grid, agent.EuclidianDistance())
        value = not (stack is None)
        expected = is_solvable(self.my_lin_board)
        file_writer.write_to_file_star(self.state.grid, cost_and_depth, actions_to_solve, explored, max_fringe_size,
                                       fringe_size, run_time, expected)("./Tests/a_star_euclidean_tests.txt")

        self.assertEqual(value, expected)



