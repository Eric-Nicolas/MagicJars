# coding: utf-8
import random

__author__ = 'Eric-Nicolas'


def custom_array(length: int, common_value: str, rare_value: str, rare_value_number: int) -> list:
    array = []
    for i in range(length - rare_value_number):
        array.append(common_value)
    for i in range(rare_value_number):
        array.append(rare_value)
    random.shuffle(array)
    return array


def get_difficulty() -> int:
    print("Here are the levels of difficulty:")
    print("1 - Easy : 1 snake in the jars")
    print("2 - Medium : 2 snakes in the jars")
    print("3 - Hard : 3 snakes in the jars\n")

    difficulty = 0
    while difficulty == 0:
        difficulty = input("Select a difficulty: ")

        try:
            difficulty = int(difficulty)
            if difficulty < 1 or difficulty > 3:
                raise ValueError
        except ValueError:
            print("Please enter a number between 1 and 3!\n")
            difficulty = 0
    print()
    return difficulty


def get_user_choice(number_of_jars: int) -> int:
    user_choice = 0
    while user_choice == 0:
        user_choice = input("Choose a jar between the n°1 and the n°" + str(number_of_jars) + ": ")
        try:
            user_choice = int(user_choice)
            if user_choice < 1 or user_choice > number_of_jars:
                raise ValueError
        except ValueError:
            print("Please enter a number between 1 and " + str(number_of_jars) + "!\n")
            user_choice = 0
    return user_choice


def main() -> None:
    NUMBER_OF_JARS = 5
    KEY = 'key'
    SNAKE = 'snake'
    DIFFICULTY = get_difficulty()

    bunch_of_keys = 0

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
