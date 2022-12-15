import pygame
import sys
from Player import Player
from Enums import Direction, Color
from Enemy import Enemy

pygame.init()


class Game:
    WINDOW_WIDTH = 600
    WINDOW_HEIGHT = 900
    FPS = 300

    def __init__(self):
        self.clock = pygame.time.Clock()
        self.window = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        pygame.display.set_caption("Space Invaders")
        self.player = Player(300, 780)
        self.enemy_list = [Enemy(400, 200), Enemy(300, 150)]
        self.player.draw(self.window)
        for enemy in self.enemy_list:
            enemy.draw(self.window)
        pygame.display.update()

    def Run(self):
        while True:
            self.window.fill(Color.Black.value)
            self.clock.tick(self.FPS)

            keys = pygame.key.get_pressed()

            if keys[pygame.K_a] or keys[pygame.K_LEFT]:
                self.player.move(Direction.LEFT, self.WINDOW_WIDTH)
            elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:
                self.player.move(Direction.RIGHT, self.WINDOW_WIDTH)

            for enemy in self.enemy_list:
                enemy.move(self.WINDOW_WIDTH)
                enemy.draw(self.window)

            self.player.draw(self.window)

            for enemy in self.enemy_list:
                enemy.shoot()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.player.shoot()

            self.check_colliding()

            self.check_bullets()

            pygame.display.update()

    def check_bullets(self):
        for bullet in self.player.bullets:
            if not bullet.check_position():
                self.player.bullets.remove(bullet)
                continue
            bullet.move()
            bullet.draw(self.window)

        for enemy in self.enemy_list:
            for bullet in enemy.bullets:
                if not bullet.check_position():
                    enemy.bullets.remove(bullet)
                    continue
                bullet.move()
                bullet.draw(self.window)

    def check_colliding(self):
        for enemy in self.enemy_list:
            for bullet in self.player.bullets:
                if enemy.is_colliding(bullet):
                    self.enemy_list.remove(enemy)
                    self.player.bullets.remove(bullet)
            for bullet in enemy.bullets:
                self.player.is_colliding(bullet)




game = Game()

game.Run()
