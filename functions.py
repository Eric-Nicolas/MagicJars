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


def get_value_safely(text_input: str, max_value: int) -> int:
    value = 0
    while value == 0:
        value = input(text_input)
        try:
            value = int(value)
            if value < 1 or value > max_value:
                raise ValueError
        except ValueError:
            print("Please enter a number between 1 and " + str(max_value) + "!\n")
            value = 0
    return value


def get_difficulty() -> int:
    print("Here are the levels of difficulty:")
    print("1 - Easy : 1 snake in the jars")
    print("2 - Medium : 2 snakes in the jars")
    print("3 - Hard : 3 snakes in the jars\n")

    return get_value_safely("Select a difficulty: ", 3)


def get_user_choice(number_of_jars: int) -> int:
    return get_value_safely("Choose a jar between the n°1 and the n°" + str(number_of_jars) + ": ", number_of_jars)
