import pygame
import random

from Enums import Color


class Wall:
    def __init__(self, x, y):
        self.pixels = [
            [[0], [0], [0], [0], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [0], [0], [0], [0]],
            [[0], [0], [0], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [0], [0], [0]],
            [[0], [0], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [0], [0]],
            [[0], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [0]],
            [[1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1]],
            [[1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1]],
            [[1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1]],
            [[1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1]],
            [[1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1]],
            [[1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1]],
            [[1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1]],
            [[1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1]],
            [[1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1]],
            [[1], [1], [1], [1], [1], [1], [1], [0], [0], [0], [0], [0], [0], [1], [1], [1], [1], [1], [1], [1]],
            [[1], [1], [1], [1], [1], [1], [0], [0], [0], [0], [0], [0], [0], [0], [1], [1], [1], [1], [1], [1]],
            [[1], [1], [1], [1], [1], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [1], [1], [1], [1], [1]],
            [[1], [1], [1], [1], [1], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [1], [1], [1], [1], [1]]]
        self.color = Color.Red.value
        self.pixel_size = 3
        self.x = x
        self.y = y

    def draw(self, window):
        for row in self.pixels:
            for pixel in row:
                if pixel[0] == 1:
                    pygame.draw.rect(window, self.color, pixel[1])

    def create_pixel_rects(self):
        x = self.x
        y = self.y
        for row in self.pixels:
            for pixel in row:
                pixel.append([x, y, self.pixel_size, self.pixel_size])
                x += self.pixel_size
            y += self.pixel_size
            x = self.x

    def destroy_nearby_pixels(self, pixel_index):
        for row in self.pixels:
            for pixel in row:
                if pixel_index[0] - 3 < self.pixels.index(row) < pixel_index[0] + 3:
                    if pixel_index[1] - 2 < row.index(pixel) < pixel_index[1] + 2:
                        if random.randint(0, 4) in [0, 1, 2, 3]:
                            self.pixels[self.pixels.index(row)][row.index(pixel)][0] = 0
                    elif pixel_index[1] - 3 < row.index(pixel) < pixel_index[1] + 3:
                        if random.randint(0, 4) in [0, 1]:
                            self.pixels[self.pixels.index(row)][row.index(pixel)][0] = 0

                elif pixel_index[0] - 4 < self.pixels.index(row) < pixel_index[0] + 4:
                    if pixel_index[1] - 3 < row.index(pixel) < pixel_index[1] + 3:
                        if random.randint(0, 4) in [0, 1]:
                            self.pixels[self.pixels.index(row)][row.index(pixel)][0] = 0
