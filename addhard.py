# 1. Задание для начинающих:
# Написать программу-игру «угадай цифру». Генерируется число в диапазоне, например, от 1 до 10.
# Пользователь вводит ответ и чтобы угадать это число у него есть всего 3 попытки.
# Если угадали - выводится сообщение о выигрыше, если проиграли о проигрыше.
# Можно так же придумать какие либо подсказки, если пользователь ошибается.
#
# 2. Задание для тех кто уже Смешарик и первая задача для вас не вызывает трудностей:
# Необходимо реализовать терминальный аналог управления кассой магазина, с корзиной и формированием чека.
# Суть заключается в красивом оформлении программы и реализации функционала управления.
# Задача полностью творческая, то какой функционал и вид примет программа зависит
# от вашей фантазии и желания написать качественную программу.
#
# По второй задаче сейчас скину, что получилось у меня. Для оформления вывода я пользовался библиотекой rich,
# но для многих она может показаться сложной(нужно лезть в интернет и документацию). Можно использовать любую другую,
# либо не пользоваться ими вообще и оформлять вид обычными отступами, символами и т.д.

import random
import datetime


def input_check(*args):                                 # проверка ввода с клавиатуры
    try:
        input_ = int(*args)
    except ValueError:
        input_ = -1                                     # обозначение некорректного ввода
    return input_


def menu_choice(form=1, choice_max=2):
    choice_max = menu_print(form)
    choice = input_check(input("Ваш выбор? "))

    if choice == 0 or choice_max == -1:
        return 1
    elif choice < 0 or choice > choice_max:
        print("ОШИБКА ВВОДА!")
        return 0
    else:
        choice_to_exit = choice_process(form, choice)
        return choice_to_exit


def menu_print(form):                                           # функция отрисовки различных меню
    global check_num_
    print()
    match form:
        case 1:                                                 # стартовое меню
            print("----------------------")
            print("|----- Кто вы? -------")
            print("| 1. Продавец")
            print("| 2. Покупатель")
            print("----------------------")
            print("| 0. Завершить работу")
            print("----------------------")
            return 2
        case 11:                                                # стартовое меню продавца
            print("----------------------------")
            print("|------- Что делаем? -------")
            print("| 1. Список товаров")
            print("| 2. Изменить цену товара")
            print("| 3. Изменить остатки товара")
            print("| 4. Добавить товар")
            print("----------------------------")
            print("| 9. Сменить пользователя")
            print("| 0. Завершить работу")
            print("----------------------------")
            return 9
        case 111:                                               # список товаров
            print("-------------------------------")
            n = 1
            for i in goods_:
                print("| " + str(n) + ".", i + ":", end=" ")
                print(goods_.get(i)[0], "шт,", goods_.get(i)[1], "руб.")
                n += 1
            print("-------------------------------")
            return 0
        case 12:                                                # стартовое меню покупателя
            print("---------------------------")
            print("|------- Что делаем? ------")
            print("| 1. Список товаров")
            print("| 2. Добавить в корзину")
            print("| 3. Посмотреть корзину")
            print("| 4. Убрать из корзины")
            print("| 5. Очистить корзину")
            print("| 6. Сформировать чек")
            print("---------------------------")
            print("| 9. Сменить пользователя")
            print("| 0. Завершить работу")
            print("---------------------------")
            return 9
        case 121:                                               # список в корзине
            if not len(cart_):
                print("Ваша корзина пуста!")
                return -1
            print("-------------------------------")
            sum_ = 0
            n = 1
            for i in cart_:
                print("| " + str(n) + ".", i + ":", end=" ")
                print(cart_.get(i)[0], "шт,", cart_.get(i)[1], "руб.")
                sum_ += cart_.get(i)[0] * cart_.get(i)[1]
                n += 1
            print("-------------------------------")
            print("| Общая стоимость:", sum_)
            print("-------------------------------")
            return 0
        case 0:
            if not len(cart_):
                print("Ваша корзина пуста!")
                return -1
            print("----------------------------------")
            check_num_ = random.randint(check_num_+1, check_num_*2)
            now_date_ = datetime.date
            now_time_ = datetime.datetime.now()
            print("--------- Чек №", check_num_, "----------")
            print("| Дата:", now_date_.today(), "Время:", now_time_.strftime("%H:%M:%S"))
            sum_ = 0
            n = 1
            for i in cart_:
                print("| " + str(n) + ".", i + ":", end=" ")
                print(cart_.get(i)[0], "шт,", cart_.get(i)[1], "руб.")
                sum_ += cart_.get(i)[0] * cart_.get(i)[1]
                print("|    ", cart_.get(i)[0], "x", cart_.get(i)[1], "=", cart_.get(i)[0] * cart_.get(i)[1])
                n += 1
            print("----------------------------------")
            print("| Количество наименований:", len(cart_))
            print("| Сумма покупки:", sum_, "руб.")
            print("|    в т.ч. НДС:", round(sum_ * 0.2, 2), "руб.")
            print("----------------------------------")
            print("Спасибо за покупку!\nБудем рады Вас видеть снова!")
            print("----------------------------------")
            return 0
        case _:                                                 # проверка на ошибку идентификатора меню
            print("ОШИБКА ФОРМЫ МЕНЮ!")
            return -1


def choice_process(form, choice):
    global menu_form
    if form == 1:                                               # стартовое меню
        match choice:
            case 1:                                             # если пользователь выбрал продавца
                password = random.randint(1, 10)              # рандомим пароль от 1 до 10
                tries = 3
                while tries > 0:
                    if tries == 1:
                        print("Последняя попытка!")
                    else:
                        print("Попыток осталось:", tries)
                    user_input = input_check(input("Введите пароль: "))
                    if user_input == password:                  # проверка на совпадение ввода с паролем
                        print("Вы успешно вошли в систему!")
                        menu_form = 11                          # обозначение стартового меню продавца
                        return 0
                    elif tries > 1 and user_input != -1:        # если это не последняя попытка и ввод корректен
                        print("Пароль", end=" ")
                        if password > user_input:
                            print("БОЛЬШЕ!")
                        else:
                            print("МЕНЬШЕ!")
                    elif user_input == -1:                      # если некорректный ввод
                        print("Ошибка ввода! Потрачена попытка")
                    tries -= 1
                print("Вход не выполнен! Возврат к предыдущему меню")
                return 0
            case 2:                                             # если пользователь выбрал покупателя
                menu_form = 12                                  # обозначение стартового меню покупателя
                return 0
    elif form == 11:                                            # меню продавца
        match choice:
            case 1:                                             # посмотреть список товаров
                menu_print(111)
                return 0
            case 2:                                             # изменить цену
                menu_print(111)
                print("| 0. Завершить работу")
                print("-------------------------------")
                choice_to_exit = goods_update(2)
                return choice_to_exit
            case 3:                                             # изменить количество
                menu_print(111)
                print("| 0. Завершить работу")
                print("-------------------------------")
                choice_to_exit = goods_update(3)
                return choice_to_exit
            case 4:                                             # добавить товар
                goods_new_renew()
                return 0
            case 9:                                             # сменить пользователя
                menu_form = 1
                return 0
    elif form == 12:                                            # меню покупателя
        match choice:
            case 1:                                             # список товаров
                menu_print(111)
                return 0
            case 2:                                             # добавить в корзину
                menu_print(111)
                print("| 0. Завершить работу")
                print("-------------------------------")
                choice_to_exit = goods_to_cart()
                if choice_to_exit == 0:
                    menu_print(121)
                return choice_to_exit
            case 3:                                             # посмотреть корзину
                menu_print(121)
                return 0
            case 4:                                             # убрать из корзины
                if menu_print(121) == -1:
                    return 0
                print("| 0. Завершить работу")
                print("-------------------------------")
                choice_to_exit = goods_of_cart()
                if choice_to_exit == 0:
                    menu_print(121)
                return choice_to_exit
            case 5:                                             # очистить корзину
                if menu_print(121) == -1:
                    return 0
                if input("Действительно очистить корзину? (Y/N) ") not in ('Y', 'y'):
                    print("Возврат в меню")
                    return 0
                n = len(cart_)
                while n > 0:
                    goods_of_cart(False)
                    n -= 1
                menu_print(121)
                return 0
            case 6:                                             # сформировать чек
                menu_print(0)
                if input("Оплатить чек? (Y/N) ") not in ('Y', 'y'):
                    print("Возврат в меню")
                    return 0
                n = len(cart_)
                while n > 0:
                    goods_of_cart(False, True)
                    n -= 1
                menu_print(121)
                return 0
            case 9:                                             # сменить пользователя
                menu_form = 1
                return 0
        return 0


def goods_update(n):                                            # функция изменения товаров
    user_input = input_check(input("Ваш выбор? "))
    if user_input < 0 or user_input > len(goods_):
        print("Ошибка ввода! Возврат к предыдущему меню")
        return 0
    elif user_input == 0:
        return 1
    goods_choice = list(goods_)[user_input-1]
    goods_new_data = input("Введите новые данные: ")
    if n == 2:
        try:
            goods_new_data = float(goods_new_data)
        except ValueError:
            goods_new_data = -1
    else:
        goods_new_data = input_check(goods_new_data)
    goods_old_data = goods_.get(goods_choice)               # сохраняем предыдущие значения на случай отмены изменений
    if goods_new_data > 0 and n == 2:
        goods_.update({goods_choice: [goods_old_data[0], goods_new_data]})
    elif goods_new_data >= 0 and n == 3:
        goods_.update({goods_choice: [goods_new_data, goods_old_data[1]]})
    else:
        print("Ошибка ввода! Возврат в меню")
    menu_print(111)
    if input("Сохранить изменения? (Y/N) ") not in ('Y', 'y'):
        goods_.update({goods_choice: goods_old_data})
        print("Данные восстановлены. Возврат в меню")
    else:
        print("Изменения успешно сохранены. Возврат в меню")
    return 0


def goods_new_renew():                                          # функция добавления новых товаров
    goods_new_data_name = input("Введите название: ")
    goods_new_data_quantity = input_check(input("Введите количество: "))
    goods_new_data_price = input("Введите цену: ")
    try:                                                        # проверка корректности ввода для дробного числа
        goods_new_data_price = float(goods_new_data_price)
    except ValueError:
        goods_new_data_price = -1
    if goods_new_data_quantity <= 0 or goods_new_data_price <= 0:
        print("Введены некорректные данные! Возврат в меню")
        return
    if goods_new_data_name in goods_:
        if input("Такой товар уже есть. Обновить данные? (Y/N) ") not in ('Y', 'y'):
            print("Изменения не внесены. Возврат в меню")
            return
    goods_.update({goods_new_data_name: [goods_new_data_quantity, goods_new_data_price]})
    menu_print(111)
    print("Изменения успешно сохранены. Возврат в меню")


def goods_to_cart():                                            # функция добавления в корзину
    error_, goods_choice, goods_quantity, goods_price, user_input, user_input_quantity = data_get(**goods_)
    if error_ == 1:
        return 1
    elif error_ == -1:
        return -1
    if goods_choice in cart_:                           # если это наименование уже есть в корзине, добавляем кол-во
        cart_quantity = cart_.get(goods_choice)[0]
        cart_.update({goods_choice: [cart_quantity+user_input_quantity, goods_price]})
    else:
        cart_.update({goods_choice: [user_input_quantity, goods_price]})
    goods_.update({goods_choice: [goods_quantity-user_input_quantity, goods_price]})    # убираем из магазина
    return 0


# функция удаления из корзины. Свойства: is_custom_ - выбор вручную или авто, is_bought_ - куплены товары или нет
def goods_of_cart(is_custom_=True, is_bought_=False):
    error_, goods_choice, goods_quantity, goods_price, user_input, user_input_quantity = data_get(is_custom_, **cart_)
    if error_ == 1:
        return 1
    elif error_ == -1:
        return -1
    cart_quantity = cart_.get(goods_choice)[0]
    if cart_quantity == user_input_quantity:                # проверяем убрать всё кол-во выбранного товара или часть
        cart_.pop(goods_choice)                             # если всё
    else:                                                   # если часть
        cart_.update({goods_choice: [cart_quantity-user_input_quantity, goods_price]})
    if not is_bought_:                                          # если товары куплены - не возвращаем в магазин
        goods_.update({goods_choice: [goods_quantity+user_input_quantity, goods_price]})    # возвращаем не купленные
    return 0


# функция сбора данных по товарам в корзине. Свойства: is_custom_ - выбор вручную или авто
def data_get(is_custom_=True, **kwargs):
    get_from_ = kwargs
    if is_custom_:                                              # ручное назначение позиций товаров
        user_input = input_check(input("Ваш выбор? "))
        if user_input < 0 or user_input > len(get_from_):       # проверка на корректность ввода
            print("Ошибка ввода! Возврат к предыдущему меню")
            return -1, 0, 0, 0, 0, 0
        elif user_input == 0:
            return 1, 0, 0, 0, 0, 0
        user_input_quantity = input_check(input("Количество? "))
        if user_input_quantity < 1 or user_input_quantity > get_from_.get(list(get_from_)[user_input-1])[0]:
            print("Превышено количество! Возврат к предыдущему меню")
            return -1, 0, 0, 0, 0, 0
        elif user_input == 0:
            return 1, 0, 0, 0, 0, 0
    else:                                                       # авто определение позиций товаров
        user_input = len(get_from_)
        user_input_quantity = get_from_.get(list(get_from_)[user_input-1])[0]
    goods_choice = list(get_from_)[user_input-1]
    goods_quantity = goods_.get(goods_choice)[0]
    goods_price = goods_.get(goods_choice)[1]
    return 0, goods_choice, goods_quantity, goods_price, user_input, user_input_quantity


# стартер пак магазина [количество, цена]
goods_ = {
    'хлеб': [10, 36.00],
    'молоко': [5, 59.50],
    'колбаса': [1, 174.20],
    'сыр': [3, 135.80]
}

cart_ = {}                                                      # стартовая пустая корзина
check_num_ = random.randint(50, 100)                          # генерация случайного номера чека

choice_exit = 0
menu_form = 1
while choice_exit != 1:
    choice_exit = menu_choice(menu_form)

print()
print('Спасибо за выбор магазина "Шестерочка"!')
print('До свидания!')
