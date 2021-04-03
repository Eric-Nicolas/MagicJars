import os
import pygame


class Finger(pygame.sprite.Sprite):
    def __init__(self, window, side, length):
        super().__init__()
        self._LENGTH = length
        self._WIDTH = window.get_width()
        self._SIDE = side
        self._IMG = pygame.image.load(os.path.join('assets', 'finger.png'))
        self._selected_item = 0

        self._x = (self._WIDTH - self._IMG.get_width()) // 5 - self._IMG.get_width()
        self._Y = window.get_height() // 3 * 2

        self._can_move = True

    @property
    def selected_item(self):
        return self._selected_item

    @property
    def can_move(self):
        return self._can_move

    @can_move.setter
    def can_move(self, value):
        self._can_move = value

    def move_left(self):
        if self._can_move and self._selected_item - 1 >= 0:
            self._selected_item -= 1
            self._x -= self._SIDE

    def move_right(self):
        if self._can_move and self._selected_item + 1 < self._LENGTH:
            self._selected_item += 1
            self._x += self._SIDE

    def draw(self, window):
        window.blit(self._IMG, (self._x, self._Y))