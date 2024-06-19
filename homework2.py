# -*- coding: utf-8 -*-
# длина окружности = 2 * радиус * Pi

class MyException(Exception):

    def __init__(self, name, message, info=None):
        self.name = name
        self.message = message
        self.info = info


def get_pi():
    count = 0

    def pi(x, action):
        nonlocal count
        if count == 100:
            raise MyException('ProcessingError', 'устал считать Пи', f'остановился на делителе {x}')
        if action == '+':
            count += 1
            return 1 / x + pi(x + 2, '-')
        elif action == '-':
            count += 1
            return 1 / x - pi(x + 2, '+')

    return 4 * pi(1, '-')


def get_radius():
    user_input = input('Введите радиус окружности: ')
    if not user_input.isnumeric():
        raise MyException('InvalidDataError', 'введены неверные данные', f'введено "{user_input}"')
    else:
        return int(user_input)


def circle_len():
    return 2 * get_radius() * get_pi()


try:
    result = circle_len()
    print(result)
except MyException as exc:
    print(f'Ошибка: {exc.name} - {exc.message}, дополнительная информация: {exc.info}')
