import pygame
from Enums import BulletType


class Bullet:
    bullet_width = 3
    bullet_height = 8
    speed = 2

    def __init__(self, x, y, color, bullet_type):
        self.bullet_type = bullet_type
        self.color = color
        self.x = x + self.bullet_width
        self.y = y - self.bullet_height
        self.rect = pygame.Rect((self.x, self.y), (self.bullet_width, self.bullet_height))

    def move(self):
        if self.bullet_type == BulletType.Player:
            self.y -= self.speed
            self.rect.y = self.y
        if self.bullet_type == BulletType.Enemy:
            self.y += self.speed
            self.rect.y = self.y

    def draw(self, window):
        if self.bullet_type == BulletType.Player:
            pygame.draw.rect(window, self.color.value, self.rect)
        if self.bullet_type == BulletType.Enemy:
            pygame.draw.rect(window, self.color, self.rect)

    def check_position(self):
        if self.bullet_type == BulletType.Player:
            if self.y < 100:
                return False
        if self.bullet_type == BulletType.Enemy:
            if self.y > 800:
                return False
        return True
