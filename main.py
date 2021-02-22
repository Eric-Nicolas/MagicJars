# coding: utf-8
import pygame
import os
from functions import *


__author__ = 'Eric-Nicolas'

pygame.init()

WIN_WIDTH, WIN_HEIGHT = 800, 600
WIN: pygame.Surface = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("MagicJars")

IMG_WIDTH, IMG_HEIGHT = 128, 128

JAR_IMG: pygame.Surface = pygame.transform.scale(
    pygame.image.load(os.path.join('assets', 'jar.png')), (IMG_WIDTH, IMG_HEIGHT))

KEY_IMG: pygame.Surface = pygame.transform.scale(
    pygame.image.load(os.path.join('assets', 'key.png')), (IMG_WIDTH // 2, IMG_HEIGHT // 2))

SNAKE_IMG: pygame.Surface = pygame.transform.scale(
    pygame.image.load(os.path.join('assets', 'snake.png')), (IMG_WIDTH // 2, IMG_HEIGHT // 2))

snake_rect = SNAKE_IMG.get_rect(
    center=(
        WIN_WIDTH // 5 - JAR_IMG.get_width() // 5 + JAR_IMG.get_width() * 4,
        WIN_HEIGHT // 2
    )
)

FIRST_PART_COLOR = (128, 64, 64)
SECOND_PART_COLOR = (128, 0, 0)
THIRD_PART_COLOR = (64, 0, 0)
FOURTH_PART_COLOR = (64, 0, 64)
ALL_COLORS = [FIRST_PART_COLOR, SECOND_PART_COLOR, THIRD_PART_COLOR, FOURTH_PART_COLOR]

NUMBER_OF_JARS = 5
NUMBER_OF_PARTS = 4
NUMBER_OF_ROUNDS = 3
KEY = 'key'
SNAKE = 'snake'


def draw_key(index: int) -> None:
    key_rect = KEY_IMG.get_rect(
        center=(
            WIN_WIDTH // 5 - KEY_IMG.get_width() // 5 + JAR_IMG.get_width() * index - 10,
            WIN_HEIGHT // 2 + 6
        )
    )
    WIN.blit(KEY_IMG, key_rect)


def draw_snake(index: int) -> None:
    rect = SNAKE_IMG.get_rect(
        center=(
            WIN_WIDTH // 5 - JAR_IMG.get_width() // 5 + JAR_IMG.get_width() * index,
            WIN_HEIGHT // 2
        )
    )
    WIN.blit(SNAKE_IMG, rect)


def draw_jar(index: int) -> None:
    jar_rect = JAR_IMG.get_rect(
        center=(
            WIN_WIDTH // 5 - JAR_IMG.get_width() // 5 + JAR_IMG.get_width() * index,
            WIN_HEIGHT // 2
        )
    )
    WIN.blit(JAR_IMG, jar_rect)


def main() -> None:
    lives = 3
    current_part = 1
    current_round = 1
    color_counter = 0

    jars = custom_array(NUMBER_OF_JARS, KEY, SNAKE, current_part)

    is_running = True
    while is_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        WIN.fill(ALL_COLORS[color_counter])

        for i in range(NUMBER_OF_JARS):
            draw_jar(i)

        for i in range(len(jars)):
            if jars[i] == KEY:
                draw_key(i)
            else:
                draw_snake(i)

        pygame.display.update()


if __name__ == '__main__':
    main()
