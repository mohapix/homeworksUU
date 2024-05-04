def test(a=10, b='String', c=True):
    print(a, b, c)
    return


test()
print()


def faktorial(n):
    if n == 1:
        return 1
    return n * faktorial(n - 1)


num = int(input("Задайте число: "))
print("Факториал заданного числа:", faktorial(num))
