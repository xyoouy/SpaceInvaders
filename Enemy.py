import random

import pygame
from Bullet import Bullet
from Enums import Color, Direction, BulletType


class Enemy:
    speed = 7.5
    scale = 3
    direction = Direction.LEFT
    move_timer_length = 1

    def __init__(self, x, y, enemy_type, is_shooter):
        self.bullets = list()
        self.shoot_timer = 0
        self.move_timer = 0
        self.dead = False
        self.current_sprite = 1
        self.is_shooter = is_shooter
        self.type = enemy_type
        self.x = x
        self.y = y
        self.shoot_timer_length = random.randint(7, 15) + self.x % 3

        self.color = Color.Green
        self.sprite = pygame.transform.scale(
            pygame.image.load(f"Sprites/Enemy{self.type}pos{self.current_sprite}{self.color.name}.png"),
            (11 * self.scale, 8 * self.scale))
        self.rect = self.sprite.get_rect().move((x, y))

    def move(self, window_width, coef):
        if self.dead:
            return
        if self.move_timer - self.move_timer_length * coef**0.85 < 0.01:
            self.move_timer += 0.015
            return

        if self.x >= 30 and self.direction == Direction.LEFT:
            self.x -= self.speed
        if self.x <= window_width - self.rect.width - 30 and self.direction == Direction.RIGHT:
            self.x += self.speed

        self.current_sprite += 1
        self.move_timer = 0
        self.rect.x = self.x

    def switch_direction(self):
        if self.dead:
            return
        self.y += 45
        if self.direction == Direction.LEFT:
            self.direction = Direction.RIGHT
        else:
            self.direction = Direction.LEFT

        self.rect.y = self.y

    def is_move_down(self, window_width):
        if self.dead:
            return
        if self.direction == Direction.RIGHT and self.x >= window_width - self.rect.width - 30:
            return True
        if self.direction == Direction.LEFT and self.x <= 30:
            return True
        return False

    def draw(self, window):
        if self.dead:
            return
        if self.rect.y == 295 - 20 or self.rect.y == 340 - 20:
            self.color = Color.Green
        elif self.rect.y == 385 - 20 or self.rect.y == 430 - 20:
            self.color = Color.Cyan
        elif self.rect.y == 475 - 20 or self.rect.y == 520 - 20:
            self.color = Color.Pink
        elif self.rect.y == 565 - 20 or self.rect.y == 610 - 20:
            self.color = Color.Yellow
        elif self.rect.y >= 655 - 20:
            self.color = Color.Red

        if self.current_sprite > 2:
            self.current_sprite = 1

        self.sprite = pygame.transform.scale(
            pygame.image.load(f"Sprites/Enemy{self.type}pos{self.current_sprite}{self.color.name}.png"),
            (11 * self.scale, 8 * self.scale))

        window.blit(self.sprite, self.rect)

    def shoot(self):
        if not self.is_shooter or self.dead:
            return

        self.shoot_timer += 0.01
        if len(self.bullets) < 1 and self.shoot_timer >= self.shoot_timer_length:
            self.bullets.append(Bullet(self.x, self.y + 10 * self.scale, self.color.value, BulletType.Enemy))
            self.shoot_timer = 0
            self.shoot_timer_length = random.randint(7, 15)

    def is_colliding(self, bullet):
        if self.dead:
            return

        if not bullet.bullet_type == BulletType.Enemy:
            self.dead = self.rect.colliderect(bullet.rect)

        return self.dead
