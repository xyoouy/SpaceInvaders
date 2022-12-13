import pygame
import sys
from Player import Player
from Enums import Direction

pygame.init()

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 900

clock = pygame.time.Clock()

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Space Invaders")

player = Player(322, 780)
player.draw(window)
pygame.display.update()


def game_loop():
    global clock
    global window
    global WINDOW_WIDTH
    global player

    bullets = []
    while True:
        window.fill((0, 0, 0))
        clock.tick(60)

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            player.move(Direction.LEFT, WINDOW_WIDTH)
        elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            player.move(Direction.RIGHT, WINDOW_WIDTH)


        player.draw(window)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.shoot(bullets)

        for bullet in bullets:
            bullet.move()
            bullet.draw(window)

        pygame.display.update()


game_loop()
