import pygame
import sys
import time

import agent as ai

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
board = ai.initial_state()
stack = ai.DFS(board)

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

        # Draw start button
        startButton = pygame.Rect((width / 2) - 65, (height / 2), width / 4, 50)
        start = mediumFont.render("Start", True, black)
        startRect = start.get_rect()
        startRect.center = startButton.center
        pygame.draw.rect(screen, white, startButton)
        screen.blit(start, startRect)

        # Check if button is clicked
        click, _, _ = pygame.mouse.get_pressed()
        if click == 1:
            mouse = pygame.mouse.get_pos()
            if startButton.collidepoint(mouse):
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
                    move = moveFont.render(board[i][j], True, white)
                    moveRect = move.get_rect()
                    moveRect.center = rect.center
                    screen.blit(move, moveRect)
                row.append(rect)
            tiles.append(row)

        the_end = ai.terminal(board)

        # Draw step button
        stepButton = pygame.Rect((width / 4), (height - 60), width / 2, 50)
        step = smallFont.render("let the agent take a move", True, black)
        stepRect = step.get_rect()
        stepRect.center = stepButton.center
        pygame.draw.rect(screen, white, stepButton)
        screen.blit(step, stepRect)

        # Find solution and get steps stack
        # Check for AI move
        # Check if step button is clicked
        click, _, _ = pygame.mouse.get_pressed()
        if click == 1:
            mouse = pygame.mouse.get_pos()
            if stepButton.collidepoint(mouse) and not the_end:
                #if stack == None :
                #To be implemented
                #display a message saying no solution to this puzzle
                time.sleep(0.5)
                board = stack[-1].grid
                stack.pop()
        if the_end:
            againButton = pygame.Rect(width / 3, height - 65, width / 3, 50)
            again = mediumFont.render("Start Again", True, black)
            againRect = again.get_rect()
            againRect.center = againButton.center
            pygame.draw.rect(screen, white, againButton)
            screen.blit(again, againRect)
            click, _, _ = pygame.mouse.get_pressed()
            if click == 1:
                mouse = pygame.mouse.get_pos()
                if againButton.collidepoint(mouse):
                    time.sleep(0.2)
                    board = ai.initial_state()
                    begin = False

    pygame.display.flip()
