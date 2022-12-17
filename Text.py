import pygame


class Text:
    def __init__(self, message, x, y, color, background_color, font_type, font_size):
        self.x = x
        self.y = y
        self.color = color
        self.background_color = background_color
        self.font_size = font_size
        self.font_type = font_type
        self.font = pygame.font.Font(self.font_type, self.font_size)
        self.text = self.font.render(message, True, self.color, self.background_color)
        self.textRect = self.text.get_rect()
        self.textRect.center = (self.x, self.y)

    def draw(self, window):
        window.blit(self.text, self.textRect)

    def update_text(self, new_message):
        self.text = self.font.render(new_message, True, self.color, self.background_color)
