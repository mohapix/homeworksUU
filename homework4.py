immutable_var = (1, "string", True, [100, True])
print(immutable_var)
# immutable_var[2] = False  // нельзя (изменение элемента кортежа)
# immutable_var[3][1] = False  // можно (изменения элемента списка внутри кортежа)
mutable_list = [1, "string", False]
mutable_list[0] = mutable_list[0] + immutable_var[3][0]
print(mutable_list)
