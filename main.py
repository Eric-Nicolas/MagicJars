# coding: utf-8
from functions import *

__author__ = 'Eric-Nicolas'


def main() -> None:
    NUMBER_OF_JARS = 5
    NUMBER_OF_PARTS = 4
    NUMBER_OF_ROUNDS = 3
    KEY = 'key'
    SNAKE = 'snake'

    lives = 3
    current_part = 1
    current_round = 1

    print("There are " + str(NUMBER_OF_JARS) + " jars in front of you.")

    is_running = True
    while is_running:
        jars = custom_array(NUMBER_OF_JARS, KEY, SNAKE, current_part)
        print(jars)

        sentence = "You have " + str(lives) + " live"

        if lives > 1:
            sentence += "s."
        else:
            sentence += '.'

        print(sentence)

        user_choice = get_user_choice(NUMBER_OF_JARS)

        if jars[user_choice - 1] == KEY:
            print("You won! You get one key.\n")
            current_round += 1
            if current_round > NUMBER_OF_ROUNDS:
                current_part += 1
                if current_part > NUMBER_OF_PARTS:
                    print("You won!\n")
                    break
                current_round = 1
                print("NEW PART!")
                print("There are " + str(current_part) + " snakes in the jars.")
        else:
            print("You have been attacked by a snake!")
            lives -= 1
            if lives == 0:
                print("You have no more lives. You lost.\n")
                is_running = False
            else:
                print("You lost one life.\n")


if __name__ == '__main__':
    main()
