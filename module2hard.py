# Задание "Слишком древний шифр":
# Вы отправились в путешествие на необитаемый остров и конечно же в очередной вылазке в джунгли вы попали в ловушку
# местному племени (да-да, классика "Индиана Джонса").
# К вашему удивлению, в племени были неплохие математики и по совместительству фантазёры.
# Вы поняли это, когда после долгих блужданий перед вами появились ворота (выход из ловушки) с двумя каменными
# вставками для чисел.
# В первом поле камни с числом менялись постоянно (от 3 до 20) случайным образом, а второе было всегда пустым.
#
# К вашему счастью рядом с менее успешными и уже неговорящими путешествинниками находился попирус, где были написаны
# правила для решения этого "ребуса". (Как жаль, что они поняли это так поздно :( ).
#
# Во вторую вставку нужно было написать те пары чисел друг за другом, чтобы число из первой вставки было кратно
# сумме их значений.
#
# Пример 1:
# 9 - число из первой вставки
# 1218273645 - нужный пароль (1 и 2, 1 и 8, 2 и 7, 3 и 6, 4 и 5 - пары; число 9 кратно сумме каждой пары)
#
# Пример 2:
# 11 - число из первой вставки
# 11029384756 - нужный пароль (1 и 10, 2 и 9, 3 и 8, 4 и 7, 5 и 6 - пары; число 11 кратно сумме каждой пары)
#
#
# К сожалению, у вас не так много времени, чтобы подбирать пароль вручную, шипы сверху уже движуться
# на вас (обожаю клише), тем более числа в первой вставке будут попадаться случайно.
#
# Составьте алгоритм, используя циклы, чтобы в независимости от введённого числа n (от 3 до 20)
# программа выдавала нужный пароль result, для одного введённого числа.
#
# Все пароли для чисел от 3 до 20 (для сверки):
# 3 - 12
# 4 - 13
# 5 - 1423
# 6 - 121524
# 7 - 162534
# 8 - 13172635
# 9 - 1218273645
# 10 - 141923283746
# 11 - 11029384756
# 12 - 12131511124210394857
# 13 - 112211310495867
# 14 - 1611325212343114105968
# 15 - 1214114232133124115106978
# 16 - 1317115262143531341251161079
# 17 - 11621531441351261171089
# 18 - 12151811724272163631545414513612711810
# 19 - 118217316415514613712811910
# 20 - 13141911923282183731746416515614713812911

# import random
# number_main = random.randint(3, 20)
# print("Число из первой вставки:", number_main)
number_main = int(input("Введите число из первой вставки: "))


def pairs_generator(number_current):
    result_str = ''
    pairs_dict = {}
    for divisor in range(2, number_current + 1):
        if number_current % divisor == 0:
            pair_list = []
            for pair_half in range(1, divisor + 1):
                if pair_half > divisor // 2:
                    break
                pair_list.append(str(pair_half) + str(divisor - pair_half))
                result_str += str(pair_half) + str(divisor - pair_half)
            pairs_dict.update({divisor: pair_list})
    return result_str, pairs_dict


# for number_main in range(3, 21):
#     result, result_dict = pairs_generator(number_main)
#     print("Варианты пар для пароля.\nДелитель: [список пар]")
#     print(result_dict)
#     print(f"Число: {number_main}, пароль: {result}")
#     print()
result, result_dict = pairs_generator(number_main)
print("Результат:", result)
print()
print("Варианты пар для пароля.\nДелитель: [список пар]")
print(result_dict)
