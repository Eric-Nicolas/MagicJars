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

    jars = custom_array(5, KEY, SNAKE)

    print("There are " + str(NUMBER_OF_JARS) + " jars in front of you.")

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

    if jars[user_choice] == KEY:
        print("You won!")
    else:
        print("You have been trapped!")


if __name__ == '__main__':
    main()
