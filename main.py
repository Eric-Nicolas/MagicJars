# coding: utf-8
import random

__author__ = 'Eric-Nicolas'


def custom_array(length: int, common_value, rare_value) -> list:
    array = []
    for i in range(length - 1):
        array.append(common_value)
    array.append(rare_value)
    random.shuffle(array)
    return array


def main() -> None:
    NUMBER_OF_JARS = 5
    KEY = 'key'
    SNAKE = 'snake'

    bunch_of_keys = 0

    is_running = True
    while is_running:  # This loop is executed until we get 3 keys in bunch_of_keys
        jars = custom_array(5, KEY, SNAKE)
        sentence_key = "You now have " + str(bunch_of_keys) + " key"

        print("There are " + str(NUMBER_OF_JARS) + " jars in front of you.")
        if bunch_of_keys == 0:
            print("You have no key.")
        elif bunch_of_keys == 1:
            print(sentence_key + '.')
        else:
            print(sentence_key + 's.')

        user_choice = 0
        while user_choice == 0:
            user_choice = input("Choose a jar between the n°1 and the n°" + str(NUMBER_OF_JARS) + ": ")
            try:
                user_choice = int(user_choice)
                if user_choice < 1 or user_choice > NUMBER_OF_JARS:
                    raise ValueError
            except ValueError:
                print("Please enter a number between 1 and " + str(NUMBER_OF_JARS) + "!\n")
                user_choice = 0

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
