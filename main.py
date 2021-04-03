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

JAR_IMG = pygame.image.load(os.path.join('assets', 'img', 'jar.png'))
KEY_IMG = pygame.image.load(os.path.join('assets', 'img', 'key.png'))
SNAKE_IMG = pygame.image.load(os.path.join('assets', 'img', 'snake.png'))

KEY_SOUND = pygame.mixer.Sound(os.path.join('assets', 'sfx', 'key_picked.wav'))
SNAKE_SOUND = pygame.mixer.Sound(os.path.join('assets', 'sfx', 'snake_picked.wav'))
GAME_OVER_SOUND = pygame.mixer.Sound(os.path.join('assets', 'sfx', 'game_over.wav'))

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

    timer = 0
    game_over = False
    is_running = True

    while is_running:
        lives_label = LABEL_FONT.render("Lives: " + str(lives), True, WHITE)
        part_label = LABEL_FONT.render("Part: " + str(current_part), True, WHITE)
        round_label = LABEL_FONT.render("Round: " + str(current_round), True, WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    finger.move_left()
                elif event.key == pygame.K_RIGHT:
                    finger.move_right()
                elif event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                    for i in range(NUMBER_OF_JARS):
                        finger.can_move = False
                        if finger.selected_item == i:
                            if jars[i] == KEY:
                                KEY_SOUND.play()
                                key_drawn = True
                                break
                            else:
                                SNAKE_SOUND.play()
                                snake_drawn = True
                                break
                elif event.key == pygame.K_ESCAPE:
                    is_running = False

        WIN.fill(ALL_PART_COLORS[current_part - 1])

        if not game_over:
            draw_labels(WIN, lives_label, part_label, round_label)

            if not key_drawn and not snake_drawn:
                for i in range(len(jars)):
                    draw_jar(WIN, JAR_IMG, i)
                finger.draw(WIN)
            elif key_drawn:
                timer += 1
                if timer <= FPS:
                    draw_key(WIN, KEY_IMG, finger.selected_item)
                else:
                    # Next round
                    current_round += 1
                    if current_round > NUMBER_OF_ROUNDS:
                        current_part += 1
                        if current_part > NUMBER_OF_PARTS:
                            print('You won!')
                            break
                        current_round = 1
                    jars = custom_array(NUMBER_OF_JARS, KEY, SNAKE, current_part)
                    finger.can_move = True
                    key_drawn = False
                    timer = 0
            elif snake_drawn:
                timer += 1
                if timer <= FPS:
                    draw_snake(WIN, SNAKE_IMG, finger.selected_item)
                else:
                    lives -= 1
                    if lives == 0:
                        game_over = True
                    finger.can_move = True
                    snake_drawn = False
                    timer = 0
        else:
            timer += 1
            if timer < FPS:
                if timer == 1:
                    GAME_OVER_SOUND.play()
                game_over_label = BIG_FONT.render("Game Over", True, WHITE)
                game_over_rect = game_over_label.get_rect(
                    center=(WIN_WIDTH // 2, WIN_HEIGHT // 2)
                )
                WIN.blit(game_over_label, game_over_rect)
            else:
                is_running = False

        pygame.display.update()
        CLOCK.tick(FPS)

    # If not is_running
    pygame.quit()
    quit()


if __name__ == '__main__':
    main()
