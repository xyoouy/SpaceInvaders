import pygame
import sys

from Menu import Menu
from Player import Player
from Enums import Direction, Color
from Enemy import Enemy
from Text import Text
from Wall import Wall

pygame.init()


class Game:
    WINDOW_WIDTH = 670
    WINDOW_HEIGHT = 900
    FPS = 120

    def __init__(self):
        self.walls = None
        self.clock = pygame.time.Clock()
        self.score = 0
        self.enemies = None
        self.level = 1
        self.window = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        self.player = Player(322, 780)
        pygame.display.set_caption("Space Invaders")
        self.texts = list()
        self.texts.append(
            Text(f"LIVES: {self.player.lives}", 60, 876, Color.Cyan.value, Color.Black.value, "pixelated.ttf", 28))
        self.texts.append(
            Text(f"SCORE: {self.score}", 120, 60, Color.Cyan.value, Color.Black.value, "pixelated.ttf", 45))
        self.texts.append(
            Text(f"LEVEL: {self.level}", 550, 60, Color.k.value, Color.Black.value, "pixelated.ttf", 45))
        self.count = None
        self.start_count = None
        self.menu = Menu()
        self.menu.menu_loop(self.Run)

    def Run(self):
        self.setup_level()

        while True:
            self.window.fill(Color.Black.value)
            self.clock.tick(self.FPS)

            if self.count == 0:
                self.create_new_level()

            self.player.respawn()

            self.check_colliding()
            self.check_player_bullets()

            self.player_behavior()
            self.enemy_behavior()

            self.draw_all()
            self.game_over()

            pygame.display.update()

    def check_player_bullets(self):
        for bullet in self.player.bullets:
            if self.player_bullet_colliding_wall(bullet):
                continue
            bullet.move()

    def check_colliding(self):
        for column_index in range(len(self.enemies)):
            for enemy_index in range(len(self.enemies[column_index])):
                if self.player.is_colliding_enemy(self.enemies[column_index][enemy_index]):
                    return
                if self.enemies[column_index][enemy_index].y in range(650, 750):
                    self.enemy_colliding_wall(column_index, enemy_index)
                for bullet in self.player.bullets:

                    if self.enemies[column_index][enemy_index].is_colliding(bullet):
                        self.enemies[column_index][enemy_index].dead = True
                        self.count -= 1
                        self.update_score(self.enemies[column_index][enemy_index].color)
                        self.player.bullets.remove(bullet)
                        self.assign_shooter(column_index, enemy_index)
                        continue
                    if not bullet.check_position():
                        self.player.bullets.remove(bullet)
                        continue

                for enemy_bullet in self.enemies[column_index][enemy_index].bullets:
                    if self.enemy_bullet_colliding_wall(column_index, enemy_index, enemy_bullet):
                        continue

                    if self.player.is_colliding_bullet(enemy_bullet):
                        self.enemies[column_index][enemy_index].bullets.remove(enemy_bullet)
                        continue
                    for player_bullet in self.player.bullets:
                        if not enemy_bullet.check_position():
                            self.enemies[column_index][enemy_index].bullets.remove(enemy_bullet)

                        if player_bullet.is_colliding(enemy_bullet):
                            self.enemies[column_index][enemy_index].bullets.remove(enemy_bullet)
                            self.player.bullets.remove(player_bullet)
                            break

    def assign_shooter(self, i, j):
        if j == 0 or not self.enemies[i][j].is_shooter:
            return
        self.enemies[i][j - 1].is_shooter = True

    def enemy_bullet_colliding_wall(self, i, j, bullet):
        for wall in self.walls:
            for row in wall.pixels:
                for pixel in row:
                    if pixel[0] == 1 and bullet.rect.colliderect(pixel[1]):
                        index = [wall.pixels.index(row), row.index(pixel)]
                        self.enemies[i][j].bullets.remove(bullet)
                        wall.destroy_nearby_pixels(index)
                        pixel[0] = 0
                        return True
        return False

    def player_bullet_colliding_wall(self, bullet):
        for wall in self.walls:
            for row in wall.pixels:
                for pixel in row:
                    if pixel[0] == 1 and bullet.rect.colliderect(pixel[1]):
                        index = [wall.pixels.index(row), row.index(pixel)]
                        self.player.bullets.remove(bullet)
                        wall.destroy_nearby_pixels(index)
                        pixel[0] = 0
                        return True
        return False

    def enemy_colliding_wall(self, i, j):
        for wall in self.walls:
            for row in wall.pixels:
                for pixel in row:
                    if pixel[0] == 1 and self.enemies[i][j].rect.colliderect(pixel[1]):
                        index = [wall.pixels.index(row), row.index(pixel)]
                        wall.destroy_nearby_pixels(index)
                        pixel[0] = 0

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
                if event.key == pygame.K_ESCAPE:
                    self.restart()
                    self.menu.menu_loop(self.Run)

    def enemy_behavior(self):
        move_down = False

        for column in self.enemies:
            for enemy in column:
                for enemy_bullet in enemy.bullets:
                    enemy_bullet.move()
                enemy.move(self.WINDOW_WIDTH, self.count / self.start_count)
                enemy.shoot()

                if enemy.is_move_down(self.WINDOW_WIDTH):
                    move_down = True

        if move_down:
            for column in self.enemies:
                for enemy in column:
                    enemy.switch_direction()

    def setup_level(self):
        self.create_enemies(11, 5)
        self.create_walls()

        self.draw_all()

    def restart(self):
        self.level = 1
        self.create_enemies(11, 5)
        self.create_walls()
        self.score = 0
        self.player = Player(322, 780)

    def create_new_level(self):
        self.level += 1
        self.create_enemies(11, 5)
        self.create_walls()

    def create_enemies(self, column_count, row_count):
        x = 50
        self.enemies = [[0 for _ in range(row_count)] for _ in range(column_count)]
        self.count = column_count * row_count
        self.start_count = column_count * row_count

        for column_index in range(column_count):
            x += 45
            y = 230
            for element in range(row_count):
                y += 45
                if element == 0:
                    self.enemies[column_index][element] = Enemy(x, y, 2, False, self.level)
                elif 0 < element < 3:
                    self.enemies[column_index][element] = Enemy(x, y, 1, False, self.level)
                elif element == 4:
                    self.enemies[column_index][element] = Enemy(x, y, 3, True, self.level)
                else:
                    self.enemies[column_index][element] = Enemy(x, y, 3, False, self.level)

    def game_over(self):
        if self.player.lives < 0:
            self.restart()
            self.menu.menu_loop(self.Run)

    def draw_all(self):
        self.player.draw(self.window)

        for bullet in self.player.bullets:
            bullet.draw(self.window)

        for column in self.enemies:
            for enemy in column:
                enemy.draw(self.window)
                for bullet in enemy.bullets:
                    bullet.draw(self.window)

        for wall in self.walls:
            wall.draw(self.window)

        for text in self.texts:
            self.texts[0].update_text(f"LIVES: {self.player.lives}")
            self.texts[1].update_text(f"SCORE: {self.score}")
            self.texts[2].update_text(f"LEVEL: {self.level}")
            text.draw(self.window)

        pygame.display.update()

    def update_score(self, color):
        if color == Color.Red:
            self.score += 30
        elif color == Color.Pink:
            self.score += 20
        elif color == Color.Yellow:
            self.score += 20
        elif color == Color.Cyan:
            self.score += 10
        elif color == Color.Green:
            self.score += 10
        print(self.score)

    def create_walls(self):
        y = 700
        space_between_walls = self.WINDOW_WIDTH / 5
        self.walls = list()

        for i in range(4):
            self.walls.append(Wall(space_between_walls * (i + 1) - 17 * 3 / 2, y))

        for wall in self.walls:
            wall.create_pixel_rects()


game = Game()

game.Run()
