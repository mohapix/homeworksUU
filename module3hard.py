# Задание "Раз, два, три, четыре, пять .... Это не всё?":
# Все ученики урбана, без исключения, - очень умные ребята. Настолько умные, что иногда по утру сами путаются в том,
# что намудрили вчера вечером.
# Один из таких учеников уснул на клавиатуре в процессе упорной учёбы (ещё и трудолюбивые). Тем не менее, даже после
# сна, его код остался рабочим и выглядел следующим образом:
#
# data_structure = [
#     [1, 2, 3],
#     {'a': 4, 'b': 5},
#     (6, {'cube': 7, 'drum': 8}),
#     "Hello",
#     ((), [{(2, 'Urban', ('Urban2', 35))}])
# ]
#
# Увидев это студент задался вопросом: "А есть ли универсальное решение для подсчёта суммы всех
# чисел и длин всех строк?"
# Да, выглядит страшно, да и обращаться нужно к каждой внутренней структуре (списку, словарю и т.д.) по разному.
#
# Ученику пришлось каждый раз использовать индексацию и обращение по ключам - универсального решения для таких
# структур он не нашёл.
#
# Помогите сокурснику осуществить его задумку.
#
# Что должно быть подсчитано:
# Все числа (не важно, являются они ключами или значениям или ещё чем-то).
# Все строки (не важно, являются они ключами или значениям или ещё чем-то)
#
# Для примера, указанного выше, рассчёт вёлся следующим образом:
# 1 + 2 + 3 + len('a') + 4 + len('b') + 5 + 6 + len('cube') + 7 + .... + 35 = 99
#
# Входные данные (применение функции):
# data_structure = [
#     [1, 2, 3],
#     {'a': 4, 'b': 5},
#     (6, {'cube': 7, 'drum': 8}),
#     "Hello",
#     ((), [{(2, 'Urban', ('Urban2', 35))}])
# ]
#
# result = calculate_structure_sum(data_structure)
# print(result)
#
#
# Выходные данные (консоль):
# 99
#
#
# Примечания (рекомендации):
# Весь подсчёт должен выполняться одним вызовом функции.
# Рекомендуется применить рекурсивный вызов функци, для каждой внутренней структуры.
# Т.к. каждая структура может содержать в себе ещё несколько элементов, можно использовать параметр *args
# Для определения типа данного используйте функцию isinstance.

def calculate_structure_sum(*args):
    sum_ = 0
    if isinstance(*args, int):
        return sum_ + int(*args)
    elif isinstance(*args, str):
        return sum_ + len(str(*args))
    elif isinstance(*args, dict):
        data_element = dict(*args)
        for i in data_element:
            sum_ += calculate_structure_sum(i) + calculate_structure_sum(data_element.get(i))
        return sum_
    else:
        data_element = list(*args)
        for i in range(len(data_element)):
            sum_ += calculate_structure_sum(data_element[i])
        return sum_


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)