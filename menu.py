import os
import pygame


class Label:
    def __init__(self, text, color, font=None):
        self._TEXT = text
        self._color = color
        self._font = font
        self._pos = (0, 0)

    def get_width(self):
        return self._font.render(self._TEXT, True, self._color).get_width()

    def set_color(self, color):
        self._color = color

    def set_font(self, font):
        self._font = font

    def set_pos(self, pos):
        self._pos = pos

    def draw(self, window):
        window.blit(self._font.render(self._TEXT, True, self._color), self._pos)


class Menu:
    def __init__(self, window, title, *texts):
        WIDTH, HEIGHT = window.get_width(), window.get_height()
        self._FONT = pygame.font.Font(os.path.join('assets', 'fonts', 'GoogleSans-Bold.ttf'), 36)
        self._BIG_FONT = pygame.font.Font(os.path.join('assets', 'fonts', 'GoogleSans-Bold.ttf'), 60)
        self._BLACK = (0, 0, 0)
        self._WHITE = (255, 255, 255)

        self._selected_item = 0
        self._TITLE = Label(title, self._WHITE, self._BIG_FONT)
        self._TITLE_WIDTH = self._TITLE.get_width()
        self._TITLE.set_pos(((WIDTH - self._TITLE_WIDTH) // 2, 20))

        self._SELECTION_SOUND = pygame.mixer.Sound(os.path.join('assets', 'sfx', 'selection.wav'))
        self._SELECTED_SOUND = pygame.mixer.Sound(os.path.join('assets', 'sfx', 'selected.wav'))
        self._BLOCKED_SOUND = pygame.mixer.Sound(os.path.join('assets', 'sfx', 'blocked.wav'))

        self._labels = [Label(texts[0], self._BLACK, self._FONT)]
        for i in range(1, len(texts)):
            self._labels.append(Label(texts[i], self._WHITE, self._FONT))

        for i in range(len(self._labels)):
            self._labels[i].set_pos(((WIDTH - self._TITLE_WIDTH) // 2, HEIGHT // (len(self._labels) + 1) * (i + 1)))

        self._button_pressed = False

    @staticmethod
    def quit():
        pygame.quit()
        quit()

    def move_up(self):
        if self._selected_item - 1 >= 0:
            self._labels[self._selected_item].set_color(self._WHITE)
            self._selected_item -= 1
            self._labels[self._selected_item].set_color(self._BLACK)
            self._SELECTION_SOUND.play()
        else:
            self._BLOCKED_SOUND.play()

    def move_down(self):
        if self._selected_item + 1 < len(self._labels):
            self._labels[self._selected_item].set_color(self._WHITE)
            self._selected_item += 1
            self._labels[self._selected_item].set_color(self._BLACK)
            self._SELECTION_SOUND.play()
        else:
            self._BLOCKED_SOUND.play()

    def play_selected_sound(self):
        self._SELECTED_SOUND.play()

    def select(self, func1, func2):
        self.play_selected_sound()
        if self._selected_item == 0:
            func1()
        elif self._selected_item == 1:
            if func2 is None:
                self.quit()
            else:
                # self.endless_mode()
                func2()

    def check_events(self, joystick: pygame.joystick.Joystick, func1, func2):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE or joystick.get_button(7):
                self.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    self.move_up()
                elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    self.move_down()
                elif event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                    self.select(func1, func2)
            elif event.type == pygame.JOYHATMOTION:
                if joystick.get_hat(0) == (0, 1):
                    self.move_up()
                elif joystick.get_hat(0) == (0, -1):
                    self.move_down()
            elif event.type == pygame.JOYBUTTONDOWN and joystick.get_button(0):
                self.select(func1, func2)

    def draw(self, window):
        self._TITLE.draw(window)
        for label in self._labels:
            label.draw(window)
