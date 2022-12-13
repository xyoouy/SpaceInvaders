import pygame
import sys
from Player import Player
from Enums import Direction, Color

pygame.init()


class Game:
    WINDOW_WIDTH = 600
    WINDOW_HEIGHT = 900
    FPS = 75

    def __init__(self):
        self.clock = pygame.time.Clock()
        self.window = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        pygame.display.set_caption("Space Invaders")
        self.player = Player(300, 780)
        self.player.draw(self.window)
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

            self.player.draw(self.window)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.player.shoot()

            self.check_bullets()

            pygame.display.update()

    def check_bullets(self):
        for bullet in self.player.bullets:
            if bullet.y < 100:
                self.player.bullets.remove(bullet)

        for bullet in self.player.bullets:
            bullet.move()
            bullet.draw(self.window)


game = Game()

game.Run()
