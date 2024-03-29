import pygame
from Enums import Direction, Color, BulletType
from Bullet import Bullet


class Player:
    speed = 1.25
    scale = 3
    respawn_time = 10

    def __init__(self, x, y):
        self.is_draw = False
        self.dead = False
        self.respawn_timer = 0
        self.bullets = list()
        self.lives = 2
        self.start_x = x
        self.x = x
        self.y = y
        self.sprite = pygame.transform.scale(
            pygame.image.load("Sprites/PlayerSprite.png"), (13 * self.scale, 8 * self.scale))
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

        if len(self.bullets) < 1:
            self.bullets.append(Bullet(self.x, self.y, Color.Cyan, BulletType.Player))

    def is_colliding_bullet(self, bullet):
        if self.dead:
            return

        if not bullet.bullet_type == BulletType.Player:
            self.dead = self.rect.colliderect(bullet.rect)

        return self.dead

    def is_colliding_enemy(self, enemy):
        if self.rect.colliderect(enemy.rect):
            self.dead = True
            self.lives = -1
            return True
        return False

    def respawn(self):
        if self.respawn_time < self.respawn_timer or self.lives < 0:
            return
        if self.dead:
            self.respawn_timer += 0.1
        if self.respawn_time < self.respawn_timer:
            print(self.lives)
            self.x = self.start_x
            self.rect.x = self.x
            self.respawn_timer = 0
            self.lives -= 1
            self.dead = False
