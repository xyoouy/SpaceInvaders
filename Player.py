import pygame
from Enums import Direction, Color, BulletType
from Bullet import Bullet


class Player:
    speed = 1
    is_draw = False
    dead = False
    bullets = list()

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.sprite = pygame.transform.scale(pygame.image.load("Sprites/PlayerSprite.png"), (50, 50))
        self.rect = self.sprite.get_rect().move((x, y))

    def move(self, direction, window_width):
        if self.dead:
            return

        if self.x > 0:
            if direction == Direction.LEFT:
                self.x -= self.speed
        if self.x < window_width - self.rect.width:
            if direction == Direction.RIGHT:
                self.x += self.speed
        self.rect.x = self.x

    def draw(self, window):
        if not self.dead:
            window.blit(self.sprite, self.rect)

    def shoot(self):
        if self.dead:
            return

        if len(self.bullets) < 5:
            self.bullets.append(Bullet(self.x, self.y, Color.Cyan, BulletType.Player))

    def is_colliding(self, bullet):
        if self.dead:
            return

        if not bullet.bullet_type == BulletType.Player:
            self.dead = self.rect.colliderect(bullet.rect)

        return self.dead

