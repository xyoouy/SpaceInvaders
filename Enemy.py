import pygame
from Enums import Color, Direction


class Enemy:
    speed = 0.5

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.dead = False
        self.color = Color.Green.value
        self.sprite = pygame.image.load("Sprites/Enemy.png")
        self.rect = self.sprite.get_rect().move((x, y))
        self.direction = Direction.LEFT

    def move(self, window_width):
        if self.dead:
            return
        if self.x >= 0 and self.direction == Direction.LEFT:
            self.x -= self.speed
            if self.x < 0:
                print(self.x)
                self.direction = Direction.RIGHT
        if self.x <= window_width - self.rect.width and self.direction == Direction.RIGHT:
            self.x += self.speed
            if self.x > window_width - self.rect.width:
                print(self.x)
                self.direction = Direction.LEFT

        self.rect.x = self.x

    def draw(self, window):
        window.blit(self.sprite, self.rect)

