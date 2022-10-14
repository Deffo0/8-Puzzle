class ButtonBuilder():
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
