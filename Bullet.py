import pygame


class Bullet:
    bullet_width = 3
    bullet_height = 12
    speed = 5

    def __init__(self, x, y, color):
        self.color = color
        self.x = x + self.bullet_width
        self.y = y - self.bullet_height
        self.rect = pygame.Rect((self.x, self.y), (self.bullet_width, self.bullet_height))

    def move(self):
        self.y -= self.speed
        self.rect.y = self.y

    def draw(self, window):
        pygame.draw.rect(window, self.color.value, self.rect)
