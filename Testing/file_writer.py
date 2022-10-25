import os


def write_to_file_fs(grid, cost_and_depth, actions_to_solve, explored, fringe_max_size, fringe_size, max_depth,
                     run_time, expected):
    def get_file_name(path_name):
        file = open(os.path.join(os.path.dirname(__file__), path_name), 'a')
        file.writelines(
            [f"{grid} \n", f"Actions to do: {actions_to_solve}\n", f"cost-to-goal: {cost_and_depth}\n",
             f"depth-to-goal: {cost_and_depth} \n",
             f"nodes explored: {explored}\n", f"Max. fringe size: {fringe_max_size} \n",
             f"Fringe size: {fringe_size} \n",
             f"Max. depth: {max_depth} \n", f"running time: {run_time} seconds \n",
             "solvable" if expected else "unsolvable", "\n\n"])
        file.close()

    return get_file_name


def write_to_file_star(grid, cost_and_depth, actions_to_solve, explored, fringe_max_size, fringe_size, run_time,
                       expected):
    def get_file_name(path_name):
        file = open(os.path.join(os.path.dirname(__file__), path_name), 'a')
        file.writelines(
            [f"{grid} \n", f"Actions to do: {actions_to_solve}\n", f"cost-to-goal: {cost_and_depth}\n",
             f"depth-to-goal: {cost_and_depth} \n",
             f"nodes explored: {explored}\n", f"Max. fringe size: {fringe_max_size} \n",
             f"Fringe size: {fringe_size} \n",
             f"running time: {run_time} seconds \n",
             "solvable" if expected else "unsolvable", "\n\n"])
        file.close()

    return get_file_name
