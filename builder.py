class ButtonBuilder:
    """
    build buttons based on its construction details
    """

    def __init__(self, screen, pygame):
        self.screen = screen
        self.pygame = pygame
        self.x = None
        self.y = None
        self.width = None
        self.height = None
        self.background_color = None
        self.font_color = None
        self.text = None
        self.font = None

    def specify_dimensions(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def specify_colors(self, background_color, font_color):
        self.background_color = background_color
        self.font_color = font_color

    def specify_text(self, text, font):
        self.text = text
        self.font = font

    def build(self):
        button = self.pygame.Rect(self.x, self.y, self.width, self.height)
        button_text = self.font.render(self.text, True, self.font_color)
        rect = button_text.get_rect()
        rect.center = button.center
        self.pygame.draw.rect(self.screen, self.background_color, button)
        self.screen.blit(button_text, rect)
        return button


class TextInputBuilder:
    """
    build text inputs based on its construction details
    """

    def __init__(self, screen, pygame):
        self.screen = screen
        self.pygame = pygame
        self.x = None
        self.y = None
        self.width = None
        self.height = None
        self.background_color = None
        self.font_color = None
        self.text = None
        self.font = None

    def specify_dimensions(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def specify_colors(self, background_color, font_color):
        self.background_color = background_color
        self.font_color = font_color

    def specify_text(self, text, font):
        self.text = text
        self.font = font

    def build(self):
        input_rect = self.pygame.Rect(self.x, self.y, self.width, self.height)
        text_surface = self.font.render(self.text, True, self.font_color)

        input_rect.w = max(text_surface.get_width() + 5, input_rect.w)

        self.pygame.draw.rect(self.screen, self.background_color, input_rect, 2)
        self.screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))


class TitleBuilder:
    """
    build titles based on its construction details
    """

    def __init__(self, screen, pygame):
        self.screen = screen
        self.pygame = pygame
        self.x = None
        self.y = None
        self.font_color = None
        self.text = None
        self.font = None

    def specify_dimensions(self, x, y):
        self.x = x
        self.y = y

    def specify_colors(self, font_color):
        self.font_color = font_color

    def specify_text(self, text, font):
        self.text = text
        self.font = font

    def build(self):
        title = self.font.render(self.text, True, self.font_color)
        title_rect = title.get_rect()
        title_rect.center = (self.x, self.y)
        self.screen.blit(title, title_rect)


class BoardBuilder:
    """
    build titles based on its construction details
    """

    def __init__(self, screen, pygame):
        self.screen = screen
        self.pygame = pygame
        self.tile_size = None
        self.tile_origin = None
        self.board = None
        self.font_color = None
        self.font = None

    def specify_dimensions(self, tile_origin, tile_size):
        self.tile_size = tile_size
        self.tile_origin = tile_origin

    def specify_colors(self, font_color):
        self.font_color = font_color

    def specify_board(self, board, font):
        self.board = board
        self.font = font

    def build(self):
        tiles = []
        for i in range(3):
            row = []
            for j in range(3):
                rect = self.pygame.Rect(
                    self.tile_origin[0] + j * self.tile_size,
                    self.tile_origin[1] + i * self.tile_size,
                    self.tile_size, self.tile_size
                )
                self.pygame.draw.rect(self.screen, self.font_color, rect, 3)

                if self.board[i][j] != "":
                    cell = self.font.render(self.board[i][j], True, self.font_color)
                    cell_rect = cell.get_rect()
                    cell_rect.center = rect.center
                    self.screen.blit(cell, cell_rect)
                row.append(rect)
            tiles.append(row)
