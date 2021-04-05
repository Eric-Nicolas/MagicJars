import random

__author__ = 'Eric-Nicolas'


def custom_array(length, common_value, rare_value, rare_value_frequency):
    if rare_value_frequency > length:
        raise IndexError()
    array = []
    for i in range(length - rare_value_frequency):
        array.append(common_value)
    for i in range(rare_value_frequency):
        array.append(rare_value)
    random.shuffle(array)

    print(array)

    return array


def draw_jar(window, jar_img, index):
    jar_rect = jar_img.get_rect(
        center=(
            window.get_width() // 5 - jar_img.get_width() // 5 + jar_img.get_width() * index,
            window.get_height() // 3 + jar_img.get_height() * 2 + 1
        )
    )
    window.blit(jar_img, jar_rect)


def draw_key(window, key_img, index):
    key_rect = key_img.get_rect(
        center=(
            window.get_width() // 5 - key_img.get_width() // 5 + key_img.get_width() * 2 * index - 10,
            window.get_height() // 2 + key_img.get_height() * 2 + 30
        )
    )
    window.blit(key_img, key_rect)


def draw_snake(window, snake_img, index):
    snake_rect = snake_img.get_rect(
        center=(
            window.get_width() // 5 - snake_img.get_width() // 5 + snake_img.get_width() * 2 * index - 11,
            window.get_height() // 2 + snake_img.get_height() * 2 + 30
        )
    )
    window.blit(snake_img, snake_rect)


def draw_labels(window, label1, label2, label3, offset=False):
    window.blit(label1, (10, 10))
    window.blit(label2, (window.get_width() - label2.get_width() - 42, 10))
    if not offset:
        window.blit(label3, (window.get_width() - label3.get_width() - 10, label3.get_height() + 10))
    else:
        window.blit(label3, (window.get_width() - 225, label3.get_height() + 10))
