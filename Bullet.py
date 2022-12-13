import pygame


class Bullet:
    bullet_width = 1
    bullet_height = 4
    color = (0, 255, 255)
    speed = 5

    def __init__(self, x, y):
        self.x = x + self.bullet_width
        self.y = y - self.bullet_height
        self.rect = pygame.Rect((self.x, self.y), (self.bullet_width, self.bullet_height))

    def move(self):
        self.y -= self.speed
        self.rect[1] = self.y

    def draw(self, window):
        pygame.draw.rect(window, self.color, self.rect)
