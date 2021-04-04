import os
import pygame
from finger import Finger
from menu import Menu
from functions import *


class Game:
    def __init__(self):
        pygame.init()

        self._WIN_WIDTH, self._WIN_HEIGHT = 800, 600
        self._WIN = pygame.display.set_mode((self._WIN_WIDTH, self._WIN_HEIGHT))
        pygame.display.set_caption("MagicJars")
        pygame.mouse.set_visible(False)

        self._IMG_SIDE = 128
        self._JAR_IMG = pygame.image.load(os.path.join('assets', 'img', 'jar.png'))
        pygame.display.set_icon(self._JAR_IMG)

        self._KEY_IMG = pygame.image.load(os.path.join('assets', 'img', 'key.png'))
        self._SNAKE_IMG = pygame.image.load(os.path.join('assets', 'img', 'snake.png'))

        self._LABEL_FONT = pygame.font.Font(None, 36)
        self._BIG_FONT = pygame.font.Font(None, 120)

        self._KEY_SOUND = pygame.mixer.Sound(os.path.join('assets', 'sfx', 'key_picked.wav'))
        self._SNAKE_SOUND = pygame.mixer.Sound(os.path.join('assets', 'sfx', 'snake_picked.wav'))
        self._GAME_OVER_SOUND = pygame.mixer.Sound(os.path.join('assets', 'sfx', 'game_over.wav'))

        self._BLACK = (0, 0, 0)
        self._WHITE = (255, 255, 255)
        self._ALL_PART_COLORS = (
            (128, 64, 64),
            (128, 0, 0),
            (64, 0, 0),
            (64, 0, 64)
        )

        self._WIN_LABEL = self._BIG_FONT.render("You win!", True, self._WHITE)
        self._GAME_OVER_LABEL = self._BIG_FONT.render("Game Over", True, self._WHITE)

        self._CLOCK = pygame.time.Clock()
        self._FPS = 60

        self._NUMBER_OF_JARS = 5
        self._NUMBER_OF_PARTS = 4
        self._NUMBER_OF_ROUNDS = 3
        self._KEY = 'key'
        self._SNAKE = 'snake'

        self._lives = 3
        self._current_part = 1
        self._current_round = 1

        self._key_drawn = False
        self._snake_drawn = False

        self._jars = custom_array(self._NUMBER_OF_JARS, self._KEY, self._SNAKE, self._current_part)
        self._finger = Finger(self._WIN, self._IMG_SIDE, self._NUMBER_OF_JARS)

        self._timer = 0
        self._has_won = False
        self._game_over = False

    @staticmethod
    def quit_game():
        pygame.quit()
        quit()

    def check_events(self, menu):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit_game()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    menu.move_up()
                elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    menu.move_down()
                elif event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                    menu.play_selected_sound()
                    if menu.get_pressed_item() == 0:
                        self.launch()
                    elif menu.get_pressed_item() == 1:
                        self.endless_mode()
                    elif menu.get_pressed_item() == 2:
                        self.quit_game()

    def run(self):
        menu = Menu(self._WIN)
        while True:
            self.check_events(menu)

            self._WIN.fill(self._ALL_PART_COLORS[0])
            menu.draw(self._WIN)

            pygame.display.update()
            self._CLOCK.tick(15)

    def check_game_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit_game()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self._finger.move_left()
                elif event.key == pygame.K_RIGHT:
                    self._finger.move_right()
                elif event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                    for i in range(self._NUMBER_OF_JARS):
                        self._finger.can_move = False
                        if self._finger.selected_item == i:
                            if self._jars[i] == self._KEY:
                                self._KEY_SOUND.play()
                                self._key_drawn = True
                                break
                            else:
                                self._SNAKE_SOUND.play()
                                self._snake_drawn = True
                                break
                elif event.key == pygame.K_ESCAPE:
                    self.quit_game()

    def handle_key(self, endless):
        self._timer += 1
        if self._timer <= self._FPS:
            draw_key(self._WIN, self._KEY_IMG, self._finger.selected_item)
        else:
            if not endless:
                self._current_round += 1
                if self._current_round > self._NUMBER_OF_ROUNDS:
                    self._current_part += 1
                    self._current_round = 1
                self._jars = custom_array(self._NUMBER_OF_JARS, self._KEY, self._SNAKE, self._current_part)
            else:
                self._jars = custom_array(self._NUMBER_OF_JARS, self._KEY, self._SNAKE, random.randrange(0, self._NUMBER_OF_JARS))
            self._finger.can_move = True
            self._key_drawn = False
            self._timer = 0

    def handle_snake(self):
        self._timer += 1
        if self._timer <= self._FPS:
            draw_snake(self._WIN, self._SNAKE_IMG, self._finger.selected_item)
        else:
            self._lives -= 1
            if self._lives == 0:
                self._game_over = True
            self._finger.can_move = True
            self._snake_drawn = False
            self._timer = 0

    def win_screen(self):
        self._timer += 1
        if self._timer < self._FPS:
            # if self._timer == 1:
            #     self._GAME_OVER_SOUND.play()
            win_rect = self._WIN_LABEL.get_rect(
                center=(self._WIN_WIDTH // 2, self._WIN_HEIGHT // 2)
            )
            self._WIN.blit(self._WIN_LABEL, win_rect)
        else:
            self.quit_game()

    def game_over_screen(self):
        self._timer += 1
        if self._timer < self._FPS:
            if self._timer == 1:
                self._GAME_OVER_SOUND.play()
            game_over_rect = self._GAME_OVER_LABEL.get_rect(
                center=(self._WIN_WIDTH // 2, self._WIN_HEIGHT // 2)
            )
            self._WIN.blit(self._GAME_OVER_LABEL, game_over_rect)
        else:
            self.quit_game()

    def launch(self):
        while True:
            lives_label = self._LABEL_FONT.render("Lives: " + str(self._lives), True, self._WHITE)
            part_label = self._LABEL_FONT.render("Part: " + str(self._current_part), True, self._WHITE)
            round_label = self._LABEL_FONT.render("Round: " + str(self._current_round), True, self._WHITE)

            self.check_game_events()
            try:
                self._WIN.fill(self._ALL_PART_COLORS[self._current_part - 1])
            except IndexError:  # If all the parts are done
                self._has_won = True

            if not self._has_won and not self._game_over:
                draw_labels(self._WIN, lives_label, part_label, round_label)
                if not self._key_drawn and not self._snake_drawn:
                    for i in range(len(self._jars)):
                        draw_jar(self._WIN, self._JAR_IMG, i)
                    self._finger.draw(self._WIN)
                elif self._key_drawn:
                    self.handle_key(False)
                elif self._snake_drawn:
                    self.handle_snake()
            elif self._has_won:
                self.win_screen()
            else:
                self.game_over_screen()

            pygame.display.update()
            self._CLOCK.tick(self._FPS)

    def endless_mode(self):
        while True:
            lives_label = self._LABEL_FONT.render("Lives: " + str(self._lives), True, self._WHITE)

            self.check_game_events()
            self._WIN.fill(self._BLACK)

            if not self._game_over:
                draw_labels(self._WIN, lives_label)
                if not self._key_drawn and not self._snake_drawn:
                    for i in range(len(self._jars)):
                        draw_jar(self._WIN, self._JAR_IMG, i)
                    self._finger.draw(self._WIN)
                elif self._key_drawn:
                    self.handle_key(True)
                elif self._snake_drawn:
                    self.handle_snake()
            else:
                self.game_over_screen()

            pygame.display.update()
            self._CLOCK.tick(self._FPS)
