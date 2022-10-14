import sys
import time

import pygame

import agent as ai
import builder

board = ai.initial_state()
manhattanDistance = ai.ManhattanDistance()
euclidianDistance = ai.EuclidianDistance()

stack = ai.AStar(board, euclidianDistance)

pygame.init()
size = width, height = 600, 400

# Colors
black = (0, 0, 0)
white = (255, 255, 255)

screen = pygame.display.set_mode(size)

# Fonts
smallFont = pygame.font.Font("OpenSans-Regular.ttf", 20)
mediumFont = pygame.font.Font("OpenSans-Regular.ttf", 28)
largeFont = pygame.font.Font("OpenSans-Regular.ttf", 40)
moveFont = pygame.font.Font("OpenSans-Regular.ttf", 60)

begin = False



while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill(black)

    # Let user start using the agent.
    if begin is False:

        # Draw title
        title = largeFont.render("8-Puzzle Agent", True, white)
        titleRect = title.get_rect()
        titleRect.center = ((width / 2), 50)
        screen.blit(title, titleRect)

        # Draw start buttons
        button_builder.specify_dimensions(60, (height / 2), width / 4, 30)
        button_builder.specify_colors(white, black)
        button_builder.specify_text("Solve DFS", smallFont)
        solve_DFS_button = button_builder.build()

        button_builder.specify_dimensions((width / 2) - 80, (height / 2), width / 4, 30)
        button_builder.specify_colors(white, black)
        button_builder.specify_text("Solve BFS", smallFont)
        solve_BFS_button = button_builder.build()

        button_builder.specify_dimensions((width / 2) + 80, (height / 2), width / 4, 30)
        button_builder.specify_colors(white, black)
        button_builder.specify_text("Solve A*", smallFont)
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
        tile_size = 80
        tile_origin = (width / 2 - (1.5 * tile_size),
                       height / 2 - (1.5 * tile_size))
        tiles = []
        for i in range(3):
            row = []
            for j in range(3):
                rect = pygame.Rect(
                    tile_origin[0] + j * tile_size,
                    tile_origin[1] + i * tile_size,
                    tile_size, tile_size
                )
                pygame.draw.rect(screen, white, rect, 3)

                if board[i][j] != ai.EMPTY:
                    cell = moveFont.render(board[i][j], True, white)
                    cellRect = cell.get_rect()
                    cellRect.center = rect.center
                    screen.blit(cell, cellRect)
                row.append(rect)
            tiles.append(row)

        the_end = ai.terminal(board)

        # Draw step button
        button_builder.specify_dimensions((width / 4), 10, width / 2, 50)
        button_builder.specify_colors(white, black)
        button_builder.specify_text("let the agent take a move", smallFont)
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
            button_builder.specify_text("Start Again", mediumFont)
            again_button = button_builder.build()

            click, _, _ = pygame.mouse.get_pressed()
            if click == 1:
                mouse = pygame.mouse.get_pos()
                if again_button.collidepoint(mouse):
                    time.sleep(0.2)
                    board = ai.initial_state()
                    begin = False

    pygame.display.flip()
