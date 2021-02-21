# coding: utf-8
from functions import *


__author__ = 'Eric-Nicolas'


def main() -> None:
    NUMBER_OF_JARS = 5
    KEY = 'key'
    SNAKE = 'snake'
    DIFFICULTY = get_difficulty()



    bunch_of_keys = 0
    lives = 3

    is_running = True
    while is_running:  # This loop is executed until we get 3 keys in bunch_of_keys
        jars = custom_array(NUMBER_OF_JARS, KEY, SNAKE, DIFFICULTY)
        sentence_key = "You now have " + str(bunch_of_keys) + " key"

        print("There are " + str(NUMBER_OF_JARS) + " jars in front of you.")
        if bunch_of_keys == 0:
            print("You have no key.")
        elif bunch_of_keys == 1:
            print(sentence_key + '.')
        else:
            print(sentence_key + 's.')

        user_choice = get_user_choice(NUMBER_OF_JARS)

        if jars[user_choice - 1] == KEY:
            print("You won! You get one key.\n")
            bunch_of_keys += 1
        else:
            sentence = "A snake attacked you! "
            if bunch_of_keys > 0:
                bunch_of_keys -= 1
                sentence += "You lost a key."
            sentence += '\n'
            print(sentence)

        if bunch_of_keys == 3:
            print("You become the king of the temple!")
            is_running = False


if __name__ == '__main__':
    main()
