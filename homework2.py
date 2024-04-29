num1 = int(input("Введите целое число: "))
print("Время суток?", end=' ')
if 5 <= num1 <= 11:
    print("Утро", end='\n')
elif 12 <= num1 <= 17:
    print("День", end='\n')
elif 18 <= num1 <= 22:
    print("Вечер", end='\n')
elif (0 <= num1 <= 4) or (23 <= num1 <= 24):
    print("Ночь", end='\n')
else:
    print("Ошибка", end='\n')

if '34' > '123':
    print("успех")

if '123' > '12':
    print("успех")

if [1, 2] > [1, 1]:
    print("успех")

if '6' != 5:
    print("успех")
