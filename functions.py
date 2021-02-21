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


def get_user_choice(number_of_jars: int) -> int:
    user_choice = 0
    while user_choice == 0:
        user_choice = input("Choose a jar between the n°1 and the n°" + str(number_of_jars) + ": ")
        try:
            user_choice = int(user_choice)
            if user_choice < 1 or user_choice > number_of_jars:
                raise ValueError
        except ValueError:
            print("Please enter a number between 1 and " + str(max_value) + "!\n")
            user_choice = 0
    return user_choice
