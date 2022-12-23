import pygame
import sys

from Enums import Color
from Text import Text


class Menu:
    def __init__(self):
        pygame.init()
        self.window_width = 670
        self.window_height = 900
        self.window = pygame.display.set_mode((self.window_width, self.window_height))
        self.clock = pygame.time.Clock()
        self.font_type = "pixelated.ttf"
        self.texts = []
        self.images = []
        self.game_over = False
        self.game_over_texts = [
            Text("YOU SUCK", self.window_width / 2 + 7, self.window_height / 2 - 100, (255, 0, 0), (0, 0, 0),
                 self.font_type, 120),
            Text("PRESS ENTER TO GO BACK TO THE MENU", self.window_width / 2, self.window_height / 2 + 50, (255, 0, 0),
                 (0, 0, 0), self.font_type, 40)
        ]

    def draw_menu_window(self):
        self.window.fill(Color.Black.value)

        if not self.game_over:
            for text in self.texts:
                text.draw(self.window)
            for image in self.images:
                self.window.blit(image[0], image[1])
        else:
            self.game_over_texts[0].draw(self.window)
            self.game_over_texts[1].draw(self.window)

        pygame.display.update()

    def check_for_inputs(self, function):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if not self.game_over:
                        function()
                    else:
                        self.game_over = False
                if event.key == pygame.K_ESCAPE:
                    sys.exit()

    def add_text(self, text):
        self.texts.append(text)

    def add_image(self, image_name, x, y):
        arr = []
        obj1 = pygame.transform.scale(pygame.image.load(image_name), (11 * 4, 8 * 4))
        obj2 = obj1.get_rect().move(x - (11 / 2) * 4, y - (8 / 2) * 4)
        arr.append(obj1)
        arr.append(obj2)
        self.images.append(arr)

    def menu_loop(self, function):
        pygame.display.set_caption("Space Invaders")

        self.add_text(Text(f"SCORE: 0", 120, 60, Color.Cyan.value, Color.Black.value, self.font_type, 45))
        self.add_text(
            Text("PRESS ENTER TO PLAY", self.window_width / 2, 180, Color.Red.value, Color.Black.value, self.font_type, 40))
        self.add_text(Text("SPACE INVADERS", self.window_width / 2, 300, Color.Green.value, Color.Black.value, self.font_type, 80))
        self.add_text(
            Text("*SCORE ADVANCE TABLE*", self.window_width / 2, 440, Color.Cyan.value, Color.Black.value, self.font_type, 40))

        self.add_image("Sprites/Enemy2pos1Red.png", self.window_width / 2 - 111, 490)
        self.add_image("Sprites/Enemy1pos1Pink.png", self.window_width / 2 - 111, 540)
        self.add_image("Sprites/Enemy3pos1Green.png", self.window_width / 2 - 111, 590)

        self.add_text(Text("= 30 POINTS", self.window_width / 2 + 22, 490, Color.Red.value, Color.Black.value, self.font_type, 40))
        self.add_text(
            Text("= 20 POINTS", self.window_width / 2 + 22, 540, Color.Pink.value, Color.Black.value, self.font_type, 40))
        self.add_text(Text("= 10 POINTS", self.window_width / 2 + 22, 590, Color.Green.value, Color.Black.value, self.font_type, 40))

        self.add_text(Text("*COUTINHO CORPORATION*", self.window_width / 2, 750, "cyan", Color.Black.value, self.font_type, 40))

        while True:
            self.draw_menu_window()
            self.check_for_inputs(function)

            self.clock.tick(120)