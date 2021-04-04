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
    def __init__(self, window):
        WIDTH, HEIGHT = window.get_width(), window.get_height()
        self._FONT = pygame.font.Font(None, 36)
        self._BIG_FONT = pygame.font.Font(None, 60)
        self._BLACK = (0, 0, 0)
        self._WHITE = (255, 255, 255)

        self._selected_item = 0
        self._TITLE = Label("Magic Jars", self._WHITE, self._BIG_FONT)
        self._TITLE_WIDTH = self._TITLE.get_width()
        self._TITLE.set_pos(((WIDTH - self._TITLE_WIDTH) // 2, 20))

        self._SELECTION_SOUND = pygame.mixer.Sound(os.path.join('assets', 'sfx', 'selection.wav'))
        self._SELECTED_SOUND = pygame.mixer.Sound(os.path.join('assets', 'sfx', 'selected.wav'))

        self._labels = [Label('Play', self._BLACK), Label('Endless Mode', self._WHITE), Label('Quit', self._WHITE)]

        for i in range(len(self._labels)):
            self._labels[i].set_font(self._FONT)
            self._labels[i].set_pos(((WIDTH - self._TITLE_WIDTH) // 2, HEIGHT // (len(self._labels) + 1) * (i + 1)))

    def get_pressed_item(self):
        return self._selected_item

    def move_up(self):
        if self._selected_item - 1 >= 0:
            self._labels[self._selected_item].set_color(self._WHITE)
            self._selected_item -= 1
            self._labels[self._selected_item].set_color(self._BLACK)
            self._SELECTION_SOUND.play()

    def move_down(self):
        if self._selected_item + 1 < len(self._labels):
            self._labels[self._selected_item].set_color(self._WHITE)
            self._selected_item += 1
            self._labels[self._selected_item].set_color(self._BLACK)
            self._SELECTION_SOUND.play()

    def play_selected_sound(self):
        self._SELECTED_SOUND.play()

    def draw(self, window):
        self._TITLE.draw(window)
        for label in self._labels:
            label.draw(window)
