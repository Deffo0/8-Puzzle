import sys
import time
import pygame
import agent as ai
from director import Director

pygame.init()
size = width, height = 600, 400
screen = pygame.display.set_mode(size)

begin = False
stack = None
board = []
undo_stack = []
solvable = True
user_text = ""

director = Director(screen, pygame, width, height)



def start_menu():
    global screen, board, stack, begin, solvable, user_text
    # Draw title and label
    director.start_menu_title()
    director.start_menu_label()
    # Draw start buttons
    solve_dfs_button = director.dfs_button()
    solve_bfs_button = director.bfs_button()
    solve_astar_manhattan_button = director.astar_manhattan_button()
    solve_astar_euclidean_button = director.astar_euclidean_button()

    for start_menu_event in pygame.event.get():
        if start_menu_event.type == pygame.KEYDOWN:
            if start_menu_event.key == pygame.K_BACKSPACE:
                user_text = user_text[:-1]
                time.sleep(0.2)

            else:
                user_text += start_menu_event.unicode
                time.sleep(0.2)

    director.start_menu_text_input(user_text)

    # Check if algorithm buttons is clicked
    start_click, _, _ = pygame.mouse.get_pressed()
    if start_click == 1 and user_text != "":
        start_mouse = pygame.mouse.get_pos()
        if solve_dfs_button.collidepoint(start_mouse):
            board = ai.initial_state(user_text)
            start = time.time()
            stack = ai.DFS(board)
            print("running time: " + str(time.time() - start) + " seconds")
            time.sleep(0.2)
            begin = True
            solvable = True

        elif solve_bfs_button.collidepoint(start_mouse):
            board = ai.initial_state(user_text)
            start = time.time()
            stack = ai.BFS(board)
            print("running time: " + str(time.time() - start) + " seconds")
            time.sleep(0.2)
            begin = True
            solvable = True

        elif solve_astar_manhattan_button.collidepoint(start_mouse):
            board = ai.initial_state(user_text)
            manhattan_distance = ai.ManhattanDistance()
            start = time.time()
            stack = ai.AStar(board, manhattan_distance)
            print("running time: " + str(time.time() - start) + " seconds")
            time.sleep(0.2)
            begin = True
            solvable = True

        elif solve_astar_euclidean_button.collidepoint(start_mouse):
            board = ai.initial_state(user_text)
            euclidean_distance = ai.EuclidianDistance()
            start = time.time()
            stack = ai.AStar(board, euclidean_distance)
            print("running time: " + str(time.time() - start) + " seconds")
            time.sleep(0.2)
            begin = True
            solvable = True


def gameplay():
    global board, stack, begin, solvable
    # Draw game board
    director.game_board(board)
    the_end = ai.terminal(board)

    # Draw step and undo buttons
    step_button = director.step_button()
    undo_button = director.undo_button()
    # Find solution and get steps stack
    # Check for AI move
    # Check if step button is clicked
    gameplay_click, _, _ = pygame.mouse.get_pressed()
    if stack is None:
        solvable = False

    if gameplay_click == 1:
        gameplay_mouse = pygame.mouse.get_pos()
        if step_button.collidepoint(gameplay_mouse) and not the_end and len(stack):
            time.sleep(0.2)
            if board == stack[-1].grid:
                board = stack[-1].grid
                undo_stack.append(stack[-1])
                stack.pop()

            board = stack[-1].grid
            undo_stack.append(stack[-1])
            stack.pop()

        elif undo_button.collidepoint(gameplay_mouse) and len(undo_stack):
            time.sleep(0.2)
            if board == undo_stack[-1].grid:
                board = undo_stack[-1].grid
                stack.append(undo_stack[-1])
                undo_stack.pop()
                the_end = False

            board = undo_stack[-1].grid
            stack.append(undo_stack[-1])
            undo_stack.pop()
            the_end = False

    if the_end:
        again_button = director.gameplay_restart_button()

        end_click, _, _ = pygame.mouse.get_pressed()
        if end_click == 1:
            end_mouse = pygame.mouse.get_pos()
            if again_button.collidepoint(end_mouse):
                time.sleep(0.2)
                begin = False


def not_solvable():
    global screen, board, begin
    screen.fill((0, 0, 0))

    # Draw title
    director.not_solvable_title()

    # Draw restart button
    restart_button = director.not_solvable_restart_button()

    click, _, _ = pygame.mouse.get_pressed()
    if click == 1:
        mouse = pygame.mouse.get_pos()
        if restart_button.collidepoint(mouse):
            time.sleep(0.2)
            begin = False


while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill((0, 0, 0))

    # Let user start using the agent.
    if begin is False:
        start_menu()

    elif solvable:
        gameplay()

    elif not solvable:
        not_solvable()

    pygame.display.flip()
