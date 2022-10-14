import sys
import time

import pygame

import agent as ai
import builder

pygame.init()
size = width, height = 600, 400

# Colors
black = (0, 0, 0)
white = (255, 255, 255)

screen = pygame.display.set_mode(size)

# Fonts
small_font = pygame.font.Font("OpenSans-Regular.ttf", 20)
medium_font = pygame.font.Font("OpenSans-Regular.ttf", 28)
large_font = pygame.font.Font("OpenSans-Regular.ttf", 40)
cell_font = pygame.font.Font("OpenSans-Regular.ttf", 60)

begin = False
stack = None
board = ai.initial_state()
button_builder = builder.ButtonBuilder(screen, pygame)
title_builder = builder.TitleBuilder(screen, pygame)
board_builder = builder.BoardBuilder(screen, pygame)

manhattanDistance = ai.ManhattanDistance()
euclidianDistance = ai.EuclidianDistance()

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill(black)

    # Let user start using the agent.
    if begin is False:

        # Draw title
        title_builder.specify_dimensions((width / 2), 50)
        title_builder.specify_colors(white)
        title_builder.specify_text("8-Puzzle Agent", large_font)
        title_builder.build()

        # Draw start buttons
        button_builder.specify_dimensions(60, (height / 2), width / 4, 30)
        button_builder.specify_colors(white, black)
        button_builder.specify_text("Solve DFS", small_font)
        solve_DFS_button = button_builder.build()

        button_builder.specify_dimensions((width / 2) - 80, (height / 2), width / 4, 30)
        button_builder.specify_colors(white, black)
        button_builder.specify_text("Solve BFS", small_font)
        solve_BFS_button = button_builder.build()

        button_builder.specify_dimensions((width / 2) + 80, (height / 2), width / 4, 30)
        button_builder.specify_colors(white, black)
        button_builder.specify_text("Solve A*", small_font)
        solve_astar_button = button_builder.build()

        # Check if button is clicked
        click, _, _ = pygame.mouse.get_pressed()
        if click == 1:
            mouse = pygame.mouse.get_pos()
            if solve_DFS_button.collidepoint(mouse):
                stack = ai.DFS(board)
                time.sleep(0.2)
                begin = True

            elif solve_BFS_button.collidepoint(mouse):
                stack = ai.BFS(board)
                time.sleep(0.2)
                begin = True

            elif solve_astar_button.collidepoint(mouse):
                stack = ai.AStar(board, manhattanDistance)
                time.sleep(0.2)
                begin = True
    else:
        # Draw game board
        board_builder.specify_dimensions((width / 2 - (1.5 * 80), height / 2 - (1.5 * 80)), 80)
        board_builder.specify_colors(white)
        board_builder.specify_board(board, cell_font)
        board_builder.build()

        the_end = ai.terminal(board)

        # Draw step button
        button_builder.specify_dimensions((width / 4), 10, width / 2, 50)
        button_builder.specify_colors(white, black)
        button_builder.specify_text("let the agent take a move", small_font)
        step_button = button_builder.build()

        # Find solution and get steps stack
        # Check for AI move
        # Check if step button is clicked
        click, _, _ = pygame.mouse.get_pressed()
        if click == 1:
            mouse = pygame.mouse.get_pos()
            if step_button.collidepoint(mouse) and not the_end:
                # if stack == None :
                # To be implemented
                # display a message saying no solution to this puzzle
                time.sleep(0.5)
                board = stack[-1].grid
                stack.pop()
        if the_end:
            button_builder.specify_dimensions(width / 3, height - 65, width / 3, 50)
            button_builder.specify_colors(white, black)
            button_builder.specify_text("Start Again", medium_font)
            again_button = button_builder.build()

            click, _, _ = pygame.mouse.get_pressed()
            if click == 1:
                mouse = pygame.mouse.get_pos()
                if again_button.collidepoint(mouse):
                    time.sleep(0.2)
                    board = ai.initial_state()
                    begin = False

    pygame.display.flip()