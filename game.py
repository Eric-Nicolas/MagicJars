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

        self._JAR_IMG = pygame.image.load(os.path.join('assets', 'img', 'jar.png'))
        pygame.display.set_icon(self._JAR_IMG)

        self._UNUSED_JAR_IMG = pygame.image.load(os.path.join('assets', 'img', 'unused_jar.png'))
        self._KEY_IMG = pygame.image.load(os.path.join('assets', 'img', 'key.png'))
        self._SNAKE_IMG = pygame.image.load(os.path.join('assets', 'img', 'snake.png'))
        self._CAVE_IMG = pygame.image.load(os.path.join('assets', 'img', 'cave.png'))

        self._LABEL_FONT = pygame.font.Font(os.path.join('assets', 'fonts', 'GoogleSans-Bold.ttf'), 30)
        self._BIG_FONT = pygame.font.Font(os.path.join('assets', 'fonts', 'GoogleSans-Bold.ttf'), 100)

        self._KEY_SOUND = pygame.mixer.Sound(os.path.join('assets', 'sfx', 'key_picked.wav'))
        self._SNAKE_SOUND = pygame.mixer.Sound(os.path.join('assets', 'sfx', 'snake_picked.wav'))
        self._GAME_OVER_SOUND = pygame.mixer.Sound(os.path.join('assets', 'sfx', 'game_over.wav'))
        self._WIN_SOUND = pygame.mixer.Sound(os.path.join('assets', 'sfx', 'win.wav'))

        self._TXT_FILENAME = os.path.join('assets', 'txt', 'highscore.txt')

        self._WHITE = (255, 255, 255)
        self._ALL_PART_COLORS = (
            (128, 64, 64),
            (128, 0, 0),
            (64, 0, 0),
            (64, 0, 64)
        )

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
        self._finger = Finger(self._WIN, self._NUMBER_OF_JARS)

        self._timer = 0
        self._has_won = False
        self._game_over = False

    @staticmethod
    def quit_game():
        pygame.quit()
        quit()

    def create_menu(self, title, option1, option2, func1, func2=None):
        menu = Menu(self._WIN, title, option1, option2)
        while True:
            menu.check_events(func1, func2)
            self._WIN.fill(self._ALL_PART_COLORS[0])
            self._WIN.blit(self._CAVE_IMG, (0, 0))
            menu.draw(self._WIN)
            pygame.display.update()
            self._CLOCK.tick(15)

    def launch_menu(self):
        self.create_menu("Magic Jars", "Play", "Quit", self.launch_submenu)

    def launch_submenu(self):
        self.create_menu("Select Mode", "Regular", "Endless", self.regular, self.endless)

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                self.quit_game()
            elif event.type == pygame.KEYDOWN:
                if not (self._has_won or self._game_over) and self._finger.can_move:
                    self._finger.handle_movement(event)
                    if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
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

    def handle_key(self, endless):
        self._timer += 1
        if self._timer <= self._FPS // 3:
            draw_key(self._WIN, self._KEY_IMG, self._finger.selected_item)
        else:
            self._current_round += 1
            if not endless:
                if self._current_round > self._NUMBER_OF_ROUNDS:
                    self._current_part += 1
                    self._current_round = 1
                self._jars = custom_array(self._NUMBER_OF_JARS, self._KEY, self._SNAKE, self._current_part)
            else:
                self._jars = custom_array(self._NUMBER_OF_JARS, self._KEY, self._SNAKE, 1)

            self._finger.can_move = True
            self._key_drawn = False
            self._timer = 0

    def handle_snake(self):
        self._timer += 1
        if self._timer <= self._FPS // 3:
            draw_snake(self._WIN, self._SNAKE_IMG, self._finger.selected_item)
        else:
            self._lives -= 1
            if self._lives == 0:
                self._game_over = True
            self._finger.can_move = True
            self._snake_drawn = False
            self._timer = 0

    def manage_jars_display(self):
        for i in range(len(self._jars)):
            if not (self._key_drawn or self._snake_drawn):
                draw_jar(self._WIN, self._JAR_IMG, i)
            elif self._finger.selected_item != i:
                draw_jar(self._WIN, self._UNUSED_JAR_IMG, i)

    def show_screen(self, text, sound):
        self._timer += 1
        if self._timer < self._FPS // 2:
            if self._timer == 1:
                sound.play()
            label = self._BIG_FONT.render(text, True, self._WHITE)
            label_rect = label.get_rect(
                center=(self._WIN_WIDTH // 2, self._WIN_HEIGHT // 2)
            )
            self._WIN.blit(label, label_rect)
        else:
            self.quit_game()

    def win_screen(self):
        self.show_screen("You Win!", self._WIN_SOUND)

    def game_over_screen(self):
        self.show_screen("Game Over", self._GAME_OVER_SOUND)

    def regular(self):
        while True:
            lives_label = self._LABEL_FONT.render("Lives: " + str(self._lives), True, self._WHITE)
            part_label = self._LABEL_FONT.render("Part: " + str(self._current_part), True, self._WHITE)
            round_label = self._LABEL_FONT.render("Round: " + str(self._current_round), True, self._WHITE)

            self.check_events()
            try:
                self._WIN.fill(self._ALL_PART_COLORS[self._current_part - 1])
            except IndexError:  # If all the parts are done
                self._has_won = True

            self._WIN.blit(self._CAVE_IMG, (0, 0))

            if not (self._has_won or self._game_over):
                draw_labels(self._WIN, lives_label, part_label, round_label)
                self.manage_jars_display()
                if not (self._key_drawn or self._snake_drawn):
                    self._finger.draw(self._WIN)
                elif self._key_drawn:
                    self.handle_key(False)
                else:
                    self.handle_snake()
            elif self._has_won:
                self.win_screen()
            else:
                self.game_over_screen()

            pygame.display.update()
            self._CLOCK.tick(self._FPS)

    def endless(self):
        highscore_text = "Highscore: "
        if os.stat(self._TXT_FILENAME).st_size == 0:  # If the file is empty
            highscore_text += '0'
        else:
            with open(self._TXT_FILENAME) as f:
                highscore_text += f.read()

        while True:
            lives_label = self._LABEL_FONT.render("Lives: " + str(self._lives), True, self._WHITE)
            highscore_label = self._LABEL_FONT.render(highscore_text, True, self._WHITE)
            score_label = self._LABEL_FONT.render("Score: " + str(self._current_round), True, self._WHITE)

            self.check_events()
            self._WIN.fill(self._ALL_PART_COLORS[2])
            self._WIN.blit(self._CAVE_IMG, (0, 0))

            if not self._game_over:
                draw_labels(self._WIN, lives_label, highscore_label, score_label, True)
                self.manage_jars_display()
                if not (self._key_drawn or self._snake_drawn):
                    self._finger.draw(self._WIN)
                elif self._key_drawn:
                    self.handle_key(True)
                else:
                    self.handle_snake()
            else:
                with open(self._TXT_FILENAME, 'w') as f:
                    f.write(str(self._current_round))
                self.game_over_screen()

            pygame.display.update()
            self._CLOCK.tick(self._FPS)
