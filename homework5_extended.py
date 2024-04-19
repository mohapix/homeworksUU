my_list = ['яблоко', 'груша', 'персик', 'гранат', 'слива']
print(my_list)
print("Первый элемент:", my_list[0])
print("Последний элемент:", my_list[-1])


def user_input(my_list_len, count):
    print("-----------------------")
    print("Задайте два целых значения от 1 до", my_list_len, "через пробел: ")
    print("(осталось попыток:", str(3 - count) + ")")
    user_input_elem1, user_input_elem2 = map(int, input() .split())
    if user_input_elem1 > user_input_elem2:
        elem_fix_list = [user_input_elem2, user_input_elem1, user_input_elem2 - 1]
    else:
        elem_fix_list = [user_input_elem1, user_input_elem2, user_input_elem1 - 1]
    return elem_fix_list, count + 1


elem_list, user_input_tries = user_input(len(my_list), 0)
while (elem_list[2] >= len(my_list) or elem_list[1] > len(my_list)) and user_input_tries < 3:
    elem_list, user_input_tries = user_input(len(my_list), user_input_tries)
if len(set(elem_list)) < len(elem_list) and elem_list[2] < len(my_list) and elem_list[1] <= len(my_list):
    print("Элемент", str(elem_list[0]) + ":", my_list[elem_list[2]])
elif elem_list[2] < len(my_list) and elem_list[1] <= len(my_list):
    print("Элементы с", elem_list[0], "по",  str(elem_list[1]) + ":", my_list[elem_list[2]:elem_list[1]])
else:
    print("Ошибка: значения не соответствуют заданным параметрам. Использованы все попытки.")
    print("-----------------------")
my_list[2] = 'апельсин'
print("Измененный список:", my_list)
print("-----------------------")

my_dict = {'Rainy': 'Дождливо',
           'Snowy': 'Идёт снег',
           'Sunny': 'Солнечно',
           'Cloudy': ['Облачно', 'Пасмурно']}
print("Словарь:", my_dict)
print("Элемент 'Snowy':", my_dict.get('Snowy'))
my_dict.update({'Snowy': 'Снегопад',
                'Windy': 'Ветренно'})
print("Измененный словарь:", my_dict)
