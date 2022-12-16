import pygame
import sys
from Player import Player
from Enums import Direction, Color
from Enemy import Enemy

pygame.init()


class Game:
    WINDOW_WIDTH = 670
    WINDOW_HEIGHT = 900
    FPS = 120

    def Run(self):
        self.setup_game()

        while True:
            self.window.fill(Color.Black.value)
            self.clock.tick(self.FPS)

            self.player_behavior()
            self.enemy_behavior()
            self.player.respawn()

            self.check_colliding()
            self.check_bullets()

            pygame.display.update()

    def check_bullets(self):
        for bullet in self.player.bullets:
            if not bullet.check_position():
                self.player.bullets.remove(bullet)
            bullet.move()
            bullet.draw(self.window)

        for enemy in self.enemies:
            for bullet in enemy.bullets:
                if not bullet.check_position():
                    enemy.bullets.remove(bullet)
                bullet.move()
                bullet.draw(self.window)

    def check_colliding(self):
        for enemy in self.enemies:
            for bullet in self.player.bullets:
                if enemy.is_colliding(bullet):
                    self.enemies.remove(enemy)
                    self.player.bullets.remove(bullet)
            for enemy_bullet in enemy.bullets:
                if self.player.is_colliding(enemy_bullet):
                    enemy.bullets.remove(enemy_bullet)
                for player_bullet in self.player.bullets:
                    if player_bullet.is_colliding(enemy_bullet):
                        enemy.bullets.remove(enemy_bullet)
                        self.player.bullets.remove(player_bullet)
                        break

    def player_behavior(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.player.move(Direction.LEFT, self.WINDOW_WIDTH)
        elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.player.move(Direction.RIGHT, self.WINDOW_WIDTH)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.player.shoot()

        self.player.draw(self.window)

    def enemy_behavior(self):

        for enemy in self.enemies:
            enemy.move(self.WINDOW_WIDTH)
            enemy.draw(self.window)

        for enemy in self.enemies:
            enemy.shoot()

    def setup_game(self):
        self.clock = pygame.time.Clock()
        self.window = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        pygame.display.set_caption("Space Invaders")
        self.player = Player(300, 780)
        self.enemies = [Enemy(400, 200), Enemy(300, 150)]
        self.player.draw(self.window)
        for enemy in self.enemies:
            enemy.draw(self.window)
        pygame.display.update()


game = Game()

game.Run()
