def num_multiplier(num):
    return num ** 2


def odd_check(num):
    return num % 2


list_ = [1, 2, 5, 7, 12, 11, 35, 4, 89, 10]
list_2 = list(map(num_multiplier, filter(odd_check, list_)))
print(list_2)
