def print_params(a=1, b='default string', c=True):
    print(f"Параметр 'a': {a}, параметр 'b': {b}, параметр 'c': {c}")


print_params()
print_params(b=25)
print_params(c=[1,2,3])

values_list = ['This is values_list', 50, [10, 20]]
values_dict = {'a': False, 'b': 100, 'c': 'This is values_dict'}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [[0, True], 'This is values_list_2']
print_params(*values_list_2, 42)
