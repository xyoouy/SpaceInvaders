import pygame
from Enums import Direction
from Bullet import Bullet


class Player:
    def __init__(self, x, y):
        self.is_draw = False
        self.x = x
        self.y = y
        self.dead = False
        self.sprite = pygame.image.load("Sprites/PlayerSprite.png")
        self.rect = self.sprite.get_rect().move((x, y))

    def move(self, direction, window_width):
        if self.dead:
            return

        if self.x >= 0:
            if direction == Direction.LEFT:
                self.x -= 3
        if self.x <= window_width - self.rect[2]:
            if direction == Direction.RIGHT:
                self.x += 3

        self.rect[0] = self.x

    def draw(self, window):
        if not self.is_draw:
            window.blit(self.sprite, self.rect)

    def shoot(self, bullets):
        # if len(bullets) < 1:
        bullets.append(Bullet(self.x, self.y))
        
