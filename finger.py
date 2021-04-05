import os
import pygame


class Finger(pygame.sprite.Sprite):
    def __init__(self, window, length):
        super().__init__()
        self._LENGTH = length
        self._WIDTH = window.get_width()
        self._SIDE = 128
        self._IMG = pygame.image.load(os.path.join('assets', 'img', 'finger.png'))
        self._SELECTION_SOUND = pygame.mixer.Sound(os.path.join('assets', 'sfx', 'selection.wav'))
        self._BLOCKED_SOUND = pygame.mixer.Sound(os.path.join('assets', 'sfx', 'blocked.wav'))
        self._selected_item = 0

        self._x = (self._WIDTH - self._IMG.get_width()) // 5 - self._IMG.get_width()
        self._Y = window.get_height() // 2 + self._IMG.get_height()

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
        if self._selected_item - 1 >= 0:
            self._selected_item -= 1
            self._x -= self._SIDE
            self._SELECTION_SOUND.play()
        else:
            self._BLOCKED_SOUND.play()

    def move_right(self):
        if self._selected_item + 1 < self._LENGTH:
            self._selected_item += 1
            self._x += self._SIDE
            self._SELECTION_SOUND.play()
        else:
            self._BLOCKED_SOUND.play()

    def handle_movement(self, event):
        if event.key == pygame.K_a or event.key == pygame.K_LEFT:
            self.move_left()
        elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
            self.move_right()

    def draw(self, window):
        window.blit(self._IMG, (self._x, self._Y))
