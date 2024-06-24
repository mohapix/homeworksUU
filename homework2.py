# -*- coding: utf-8 -*-

# Фабрика функций для сложения, вычитания, умножения и деления:
def create_operation(operation):
    if operation == "plus":
        def plus(x, y):
            return x + y
        return plus
    elif operation == "minus":
        def minus(x, y):
            return x - y
        return minus
    elif operation == "multiply":
        def multiply(x, y):
            return x * y
        return multiply
    elif operation == "divide":
        def divide(x, y):
            try:
                result = x / y
            except ZeroDivisionError:
                return f'Error: Division by zero'
            else:
                return round(result, 2)
        return divide


new_func_plus = create_operation('multiply')
print(new_func_plus(2, 3))

new_func_divide = create_operation('divide')
print(new_func_divide(18, 9))
print(new_func_divide(20, 0))


# Лямбда функции с аналогом через def
my_num_xx2 = lambda x: x ** 2
print(my_num_xx2(4))


def func_num_xx2(num):
    return num ** 2


print(func_num_xx2(4))


# Создания вызываемого объекта
class Rect:
    def __init__(self, a, b):
        self.side_a = a
        self.side_b = b

    def __call__(self):
        return self.side_a * self.side_b

    def __repr__(self):
        return f'Стороны: {self.side_a}, {self.side_b}'


my_rect = Rect(2, 4)
print(my_rect)
print(f'Площадь: {my_rect()}')
