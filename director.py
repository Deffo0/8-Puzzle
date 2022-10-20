import pygame
from builder import *


class Director:

    def __init__(self, screen, pygame, width, height):
        self.button_builder = ButtonBuilder(screen, pygame)
        self.title_builder = TitleBuilder(screen, pygame)
        self.text_input_builder = TextInputBuilder(screen, pygame)
        self.board_builder = BoardBuilder(screen, pygame)
        self.small_font = pygame.font.Font("FuzzyBubbles-Regular.ttf", 20)
        self.tiny_font = pygame.font.Font("FuzzyBubbles-Regular.ttf", 14)
        self.medium_font = pygame.font.Font("FuzzyBubbles-Regular.ttf", 28)
        self.large_font = pygame.font.Font("FuzzyBubbles-Regular.ttf", 40)
        self.cell_font = pygame.font.Font("FuzzyBubbles-Regular.ttf", 60)
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.gold = (253, 169, 19)
        self.sun = (253, 169, 19)
        self.width = width
        self.height = height

    def start_menu_title(self):
        self.title_builder.specify_dimensions((self.width / 2), 50)
        self.title_builder.specify_colors(self.gold)
        self.title_builder.specify_text("8-Puzzle Agent", self.large_font)
        self.title_builder.build()

    def start_menu_label(self):
        self.title_builder.specify_dimensions((self.width / 2), 125)
        self.title_builder.specify_colors(self.gold)
        self.title_builder.specify_text("Enter the initial state of the puzzle:", self.small_font)
        self.title_builder.build()

    def start_menu_text_input(self, user_text):
        self.text_input_builder.specify_dimensions(120, (self.height / 2) - 50, 350, 25)
        self.text_input_builder.specify_colors(self.sun, self.white)
        self.text_input_builder.specify_text(user_text, self.tiny_font)
        self.text_input_builder.build()

    def dfs_button(self):
        self.button_builder.specify_dimensions(120, (self.height / 2), self.width / 4, 30)
        self.button_builder.specify_colors(self.gold, self.black)
        self.button_builder.specify_text("Solve DFS", self.small_font)
        return self.button_builder.build()

    def bfs_button(self):
        self.button_builder.specify_dimensions(330, (self.height / 2), self.width / 4, 30)
        self.button_builder.specify_colors(self.gold, self.black)
        self.button_builder.specify_text("Solve BFS", self.small_font)
        return self.button_builder.build()

    def astar_manhattan_button(self):
        self.button_builder.specify_dimensions(120, (self.height / 2) + 40, self.width / 2 + 60, 30)
        self.button_builder.specify_colors(self.gold, self.black)
        self.button_builder.specify_text("Solve A* with manhattan heuristics", self.small_font)
        return self.button_builder.build()

    def astar_euclidean_button(self):
        self.button_builder.specify_dimensions(120, (self.height / 2) + 80, self.width / 2 + 60, 30)
        self.button_builder.specify_colors(self.gold, self.black)
        self.button_builder.specify_text("Solve A* with euclidean heuristics", self.small_font)
        return self.button_builder.build()

    def game_board(self, board):
        self.board_builder.specify_dimensions((self.width / 2 - (1.5 * 80), self.height / 2 - (1.5 * 80)), 80)
        self.board_builder.specify_colors(self.gold)
        self.board_builder.specify_board(board, self.cell_font)
        self.board_builder.build()

    def step_button(self):
        self.button_builder.specify_dimensions((self.width / 4), 10, self.width / 2, 50)
        self.button_builder.specify_colors(self.gold, self.black)
        self.button_builder.specify_text("let the agent take a move", self.small_font)
        return self.button_builder.build()

    def undo_button(self):
        self.button_builder.specify_dimensions((self.width - 100), 120, 60, 30)
        self.button_builder.specify_colors(self.gold, self.black)
        self.button_builder.specify_text("undo", self.small_font)
        return self.button_builder.build()

    def gameplay_restart_button(self):
        self.button_builder.specify_dimensions(self.width / 3, self.height - 65, self.width / 3, 40)
        self.button_builder.specify_colors(self.gold, self.black)
        self.button_builder.specify_text("restart", self.medium_font)
        return self.button_builder.build()

    def not_solvable_title(self):
        self.title_builder.specify_dimensions((self.width / 2), (self.height / 2))
        self.title_builder.specify_colors(self.gold)
        self.title_builder.specify_text("Not solvable puzzle:(", self.large_font)
        self.title_builder.build()

    def not_solvable_restart_button(self):
        self.button_builder.specify_dimensions(self.width / 3, self.height - 150, self.width / 3, 40)
        self.button_builder.specify_colors(self.gold, self.black)
        self.button_builder.specify_text("restart", self.medium_font)
        return self.button_builder.build()
