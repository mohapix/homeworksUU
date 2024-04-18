my_list = ['яблоко', 'груша', 'персик', 'гранат', 'слива']
print(my_list)
print("Первый элемент:", my_list[0])
print("Последний элемент:", my_list[-1])
print("Элементы с 3 по 5:", my_list[2:5])
my_list[2] = 'апельсин'
print("Измененный список:", my_list)
print()

my_dict = {'Rainy': 'Дождливо',
           'Snowy': 'Идёт снег',
           'Sunny': 'Солнечно',
           'Cloudy': ['Облачно', 'Пасмурно']}
print("Словарь:", my_dict)
print("Элемент 'Snowy':", my_dict.get('Snowy'))
my_dict.update({'Snowy': 'Снегопад',
                'Windy': 'Ветренно'})
print("Измененный словарь:", my_dict)
