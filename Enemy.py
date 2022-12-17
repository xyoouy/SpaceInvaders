import random

import pygame
from datetime import datetime
from Bullet import Bullet
from Enums import Color, Direction, BulletType


class Enemy:
    speed = 7.5
    bullets = list()
    scale = 3
    shoot_timer = 0
    current_sprite = 1
    dead = False
    direction = Direction.LEFT
    move_timer = 0

    move_timer_length = 1

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.shoot_timer_length = random.randint(2, 6)

        self.color = Color.Green.value
        self.sprite = pygame.transform.scale(pygame.image.load(f"Sprites/Enemy{self.current_sprite}green.png"),
                                             (11 * self.scale, 8 * self.scale))
        self.rect = self.sprite.get_rect().move((x, y))

    def move(self, window_width):
        if self.dead:
            return
        if abs(self.move_timer_length - self.move_timer) >= 0.01:
            self.move_timer += 0.013
            return

        if self.x >= 0 and self.direction == Direction.LEFT:
            self.x -= self.speed
            if self.x < 0:
                self.direction = Direction.RIGHT
        if self.x <= window_width - self.rect.width and self.direction == Direction.RIGHT:
            self.x += self.speed
            if self.x > window_width - self.rect.width:
                self.direction = Direction.LEFT

        self.current_sprite = (self.current_sprite + 1) % 2
        self.sprite = pygame.transform.scale(pygame.image.load(f"Sprites/Enemy{self.current_sprite}green.png"),
                                             (11 * self.scale, 8 * self.scale))

        self.move_timer = 0
        self.rect.x = self.x

    def draw(self, window):
        window.blit(self.sprite, self.rect)

    def shoot(self):
        self.shoot_timer += 0.01
        if len(self.bullets) < 5 and self.shoot_timer >= self.shoot_timer_length:
            self.bullets.append(Bullet(self.x, self.y + 10 * self.scale, self.color, BulletType.Enemy))
            self.shoot_timer = 0
            self.shoot_timer_length = random.randint(2, 6)

    def is_colliding(self, bullet):
        if self.dead:
            return

        if not bullet.bullet_type == BulletType.Enemy:
            self.dead = self.rect.colliderect(bullet.rect)

        return self.dead


