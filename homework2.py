def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")

    inner_function()


try:
    inner_function()
except NameError:
    print("Функция не объявлена")
