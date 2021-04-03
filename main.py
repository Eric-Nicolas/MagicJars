import os
import pygame
from finger import Finger
from functions import *


__author__ = 'Eric-Nicolas'

pygame.init()

WIN_WIDTH, WIN_HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("MagicJars")

LABEL_FONT = pygame.font.Font(None, 36)
BIG_FONT = pygame.font.Font(None, 120)

IMG_SIDE = 128

JAR_IMG = pygame.transform.scale(
            pygame.image.load(os.path.join('assets', 'img', 'jar.png')), (IMG_SIDE, IMG_SIDE))

KEY_IMG = pygame.transform.scale(
    pygame.image.load(os.path.join('assets', 'img', 'key.png')), (IMG_SIDE // 2, IMG_SIDE // 2))

SNAKE_IMG = pygame.transform.scale(
    pygame.image.load(os.path.join('assets', 'img', 'snake.png')), (IMG_SIDE // 2, IMG_SIDE // 2))

WHITE = (255, 255, 255)
ALL_PART_COLORS = (
    (128, 64, 64),
    (128, 0, 0),
    (64, 0, 0),
    (64, 0, 64)
)

CLOCK = pygame.time.Clock()
FPS = 60

NUMBER_OF_JARS = 5
NUMBER_OF_PARTS = 4
NUMBER_OF_ROUNDS = 3
KEY = 'key'
SNAKE = 'snake'


def main():
    lives = 3
    current_part = 1
    current_round = 1

    key_drawn = False
    snake_drawn = False

    jars = custom_array(NUMBER_OF_JARS, KEY, SNAKE, current_part)
    finger = Finger(WIN, IMG_SIDE, NUMBER_OF_JARS)

    time = 0
    is_running = True

    while is_running:
        lives_label = LABEL_FONT.render("Lives: " + str(lives), True, WHITE)
        part_label = LABEL_FONT.render("Part: " + str(current_part), True, WHITE)
        round_label = LABEL_FONT.render("Round: " + str(current_round), True, WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    finger.move_left()
                elif event.key == pygame.K_RIGHT:
                    finger.move_right()
                elif event.key == pygame.K_SPACE:
                    for i in range(NUMBER_OF_JARS):
                        finger.can_move = False
                        if finger.selected_item == i:
                            if jars[i] == KEY:
                                key_drawn = True
                                break
                            else:
                                snake_drawn = True
                                break

        WIN.fill(ALL_PART_COLORS[current_part - 1])

        draw_labels(WIN, (lives_label, part_label, round_label))

        if not key_drawn and not snake_drawn:
            for i in range(len(jars)):
                draw_jar(WIN, JAR_IMG, i)
            finger.draw(WIN)
        elif key_drawn:
            time += 1
            if time <= FPS:
                draw_key(WIN, KEY_IMG, finger.selected_item)
            else:
                # Next round
                current_round += 1
                if current_round > NUMBER_OF_ROUNDS:
                    current_part += 1
                    if current_part > NUMBER_OF_PARTS:
                        print('You won!')
                        is_running = False
                    current_round = 1
                jars = custom_array(NUMBER_OF_JARS, KEY, SNAKE, current_part)
                finger.can_move = True

                key_drawn = False
                time = 0
        elif snake_drawn:
            time += 1
            if time <= FPS:
                draw_snake(WIN, SNAKE_IMG, finger.selected_item)
            else:
                lives -= 1
                if lives == 0:
                    is_running = False
                finger.can_move = True
                snake_drawn = False

        pygame.display.update()
        CLOCK.tick(FPS)

    # If !is_running
    pygame.quit()
    quit()


if __name__ == '__main__':
    main()
