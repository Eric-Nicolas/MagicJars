import os
import pygame
from finger import Finger
from functions import *


__author__ = 'Eric-Nicolas'

pygame.init()

WIN_WIDTH, WIN_HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("MagicJars")

FPS = 60
CLOCK = pygame.time.Clock()

FONT = pygame.font.Font(None, 36)

IMG_SIDE = 128

JAR_IMG = pygame.transform.scale(
            pygame.image.load(os.path.join('assets', 'jar.png')), (IMG_SIDE, IMG_SIDE))

KEY_IMG = pygame.transform.scale(
    pygame.image.load(os.path.join('assets', 'key.png')), (IMG_SIDE // 2, IMG_SIDE // 2))

SNAKE_IMG = pygame.transform.scale(
    pygame.image.load(os.path.join('assets', 'snake.png')), (IMG_SIDE // 2, IMG_SIDE // 2))

FINGER_IMG = pygame.image.load(os.path.join('assets', 'finger.png'))

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


def main():
    lives = 3
    current_part = 1
    current_round = 1
    color_counter = 0

    jars = custom_array(NUMBER_OF_JARS, KEY, SNAKE, current_part)

    finger = Finger(WIN, IMG_SIDE, NUMBER_OF_JARS)

    while True:
        lives_label = FONT.render("Lives: " + str(lives), True, WHITE)
        part_label = FONT.render("Part: " + str(current_part), True, WHITE)
        round_label = FONT.render("Round: " + str(current_round), True, WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    finger.move_left()
                elif event.key == pygame.K_RIGHT:
                    finger.move_right()
                elif event.key == pygame.K_RETURN:
                    pass

        WIN.fill(ALL_PART_COLORS[color_counter])

        draw_labels(WIN, (lives_label, part_label, round_label))

        for i in range(len(jars)):
            draw_jar(WIN, JAR_IMG, i)

            if jars[i] == KEY:
                draw_key(WIN, KEY_IMG, i)
            else:
                draw_snake(WIN, SNAKE_IMG, i)

        finger.draw(WIN)

        pygame.display.update()
        CLOCK.tick(FPS)


if __name__ == '__main__':
    main()
