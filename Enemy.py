import pygame

from Bullet import Bullet
from Enums import Color, Direction, BulletType


class Enemy:
    speed = 0.25
    bullets = list()

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.shoot_timer = 0
        self.shoot_timer_length = 10
        self.dead = False
        self.color = Color.Green.value
        self.sprite = pygame.transform.scale(pygame.image.load("Sprites/Enemy.png"), (40, 50))
        self.rect = self.sprite.get_rect().move((x, y))
        self.direction = Direction.LEFT

    def move(self, window_width):
        if self.dead:
            return
        if self.x >= 0 and self.direction == Direction.LEFT:
            self.x -= self.speed
            if self.x < 0:
                self.direction = Direction.RIGHT
        if self.x <= window_width - self.rect.width and self.direction == Direction.RIGHT:
            self.x += self.speed
            if self.x > window_width - self.rect.width:
                self.direction = Direction.LEFT

        self.rect.x = self.x

    def draw(self, window):
        window.blit(self.sprite, self.rect)

    def shoot(self):
        self.shoot_timer += 0.01
        if len(self.bullets) < 5 and self.shoot_timer >= self.shoot_timer_length:
            self.bullets.append(Bullet(self.x, self.y, self.color, BulletType.Enemy))
            self.shoot_timer = 0

    def is_colliding(self, bullet):
        if bullet.bullet_type == BulletType.Enemy:
            return False

        return self.rect.colliderect(bullet.rect)


