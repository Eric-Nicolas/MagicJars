# coding: utf-8
import os
from functions import *


__author__ = 'Eric-Nicolas'

pygame.init()

WIN_WIDTH, WIN_HEIGHT = 800, 600
WIN: pygame.Surface = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("MagicJars")

FPS = 60
CLOCK = pygame.time.Clock()

FONT = pygame.font.Font(None, 36)

IMG_SIDE = 128

JAR_IMG: pygame.Surface = pygame.transform.scale(
    pygame.image.load(os.path.join('assets', 'jar.png')), (IMG_SIDE, IMG_SIDE))

KEY_IMG: pygame.Surface = pygame.transform.scale(
    pygame.image.load(os.path.join('assets', 'key.png')), (IMG_SIDE // 2, IMG_SIDE // 2))

SNAKE_IMG: pygame.Surface = pygame.transform.scale(
    pygame.image.load(os.path.join('assets', 'snake.png')), (IMG_SIDE // 2, IMG_SIDE // 2))

WHITE = (255, 255, 255)
FIRST_PART_COLOR = (128, 64, 64)
SECOND_PART_COLOR = (128, 0, 0)
THIRD_PART_COLOR = (64, 0, 0)
FOURTH_PART_COLOR = (64, 0, 64)
ALL_PART_COLORS = [FIRST_PART_COLOR, SECOND_PART_COLOR, THIRD_PART_COLOR, FOURTH_PART_COLOR]

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

    jars = custom_array(NUMBER_OF_JARS, KEY, SNAKE, current_part)

    is_running = True
    while is_running:
        lives_label = FONT.render("Lives: " + str(lives), True, WHITE)
        part_label = FONT.render("Part: " + str(current_part), True, WHITE)
        round_label = FONT.render("Round: " + str(current_round), True, WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        WIN.fill(ALL_PART_COLORS[color_counter])

        WIN.blit(lives_label, (10, 10))
        WIN.blit(part_label, (WIN_WIDTH - part_label.get_width() - 39, 10))
        WIN.blit(round_label, (WIN_WIDTH - round_label.get_width() - 10, round_label.get_height() + 10))

        for i in range(NUMBER_OF_JARS):
            draw_jar(WIN, JAR_IMG, i)

        for i in range(len(jars)):
            if jars[i] == KEY:
                draw_key(WIN, KEY_IMG, i)
            else:
                draw_snake(WIN, SNAKE_IMG, i)

        pygame.display.update()
        CLOCK.tick(FPS)


if __name__ == '__main__':
    main()
