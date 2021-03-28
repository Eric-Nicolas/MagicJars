# coding: utf-8
import random

__author__ = 'Eric-Nicolas'


def custom_array(length, common_value, rare_value, rare_value_frequency) -> list:
    array = []
    for i in range(length - rare_value_frequency):
        array.append(common_value)
    for i in range(rare_value_frequency):
        array.append(rare_value)
    random.shuffle(array)
    return array


def draw_jar(window, jar_img, index):
    jar_rect = jar_img.get_rect(
        center=(
            window.get_width() // 5 - jar_img.get_width() // 5 + jar_img.get_width() * index,
            window.get_height() // 2
        )
    )
    window.blit(jar_img, jar_rect)


def draw_key(window, key_img, index):
    key_rect = key_img.get_rect(
        center=(
            window.get_width() // 5 - key_img.get_width() // 5 + key_img.get_width() * 2 * index - 10,
            window.get_height() // 2 + 6
        )
    )
    window.blit(key_img, key_rect)


def draw_snake(window, snake_img, index):
    snake_rect = snake_img.get_rect(
        center=(
            window.get_width() // 5 - snake_img.get_width() // 5 + snake_img.get_width() * 2 * index - 11,
            window.get_height() // 2
        )
    )
    window.blit(snake_img, snake_rect)


def draw_labels(window, labels: tuple):
    window.blit(labels[0], (10, 10))
    window.blit(labels[1], (window.get_width() - labels[1].get_width() - 39, 10))
    window.blit(labels[2], (window.get_width() - labels[2].get_width() - 10, labels[2].get_height() + 10))


def get_user_choice(number_of_jars):
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
