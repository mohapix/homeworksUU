from random import choice

# Lambda-функция

first = 'Мама мыла раму'
second = 'Рамена мало было'

my_func = lambda lit1, lit2: lit1 == lit2

print(list(map(my_func, first, second)))
"""
[False, True, True, False, False, False, False, False, True, False, False, False, False, False]
"""


# Замыкание


def get_advanced_writer(file_name):

    def write_everything(*data_set):
        with open(file_name, mode='w') as file:
            for line in data_set:
                file.write(str(line) + '\n')

    return write_everything


write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])
"""
Это строчка
['А', 'это', 'уже', 'число', 5, 'в', 'списке']
"""


# Метод __call__
class MysticBall:

    def __init__(self, *words):
        self.words = words

    def __call__(self):
        return choice(self.words)


first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())
"""
Нет
Наверное
Наверное
"""
