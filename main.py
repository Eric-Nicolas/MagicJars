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

jar_rect = JAR_IMG.get_rect(
    center=(
        WIN_WIDTH // 5 - JAR_IMG.get_width() // 5,
        WIN_HEIGHT // 2 - JAR_IMG.get_height() // 2
    )
)

KEY_IMG: pygame.Surface = pygame.transform.scale(
    pygame.image.load(os.path.join('assets', 'key.png')), (IMG_WIDTH // 2, IMG_HEIGHT // 2))

SNAKE_IMG: pygame.Surface = pygame.transform.scale(
    pygame.image.load(os.path.join('assets', 'snake.png')), (IMG_WIDTH // 2, IMG_HEIGHT // 2))

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


def main() -> None:
    lives = 3
    current_part = 1
    current_round = 1
    color_counter = 0

    is_running = True
    while is_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        WIN.fill(ALL_COLORS[color_counter])

        WIN.blit(JAR_IMG, jar_rect)
        WIN.blit(KEY_IMG, (0, 0))
        WIN.blit(SNAKE_IMG, (WIN_WIDTH - SNAKE_IMG.get_width(), 0))

        pygame.display.update()


if __name__ == '__main__':
    main()
