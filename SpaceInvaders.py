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
    while True:
        window.fill((0, 0, 0))

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            player.move(Direction.LEFT, WINDOW_WIDTH)
        elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            player.move(Direction.RIGHT, WINDOW_WIDTH)

        player.draw(window)

        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                sys.exit()

        pygame.display.update()


game_loop()
