# Напишите программу, которая составляет словарь, используя grades и students,
# где ключом будет имя ученика, а значением - его средний балл.
#
# Вывод в консоль:
# {'Aaron': 4.0, 'Bilbo': 2.25, 'Johny': 4.0, 'Kendrik': 3.6666666666666665, 'Steve': 4.8}
# Самостоятельно составлять (вручную) словарь не нужно (только изначально пустой).
# Для решения задачи нужно вспомнить функции sum, len и др. (подумать самому).
# Помните, что множество не является упорядоченной последовательностью. (нужен перевод в другой тип).

grades = ['5 3 3 5 4', '2 2 2 3', '4 5 5 2', '4 4 3', '5 5 5 4 5']
students = {'Johnni', 'Bilbo', 'Steve', 'Kendrik', 'Aaron'}

# метод 1 - через перебор элементов строки и суммирование оценок, пропуская пробелы
grades_average = []
for i in range(len(grades)):
    sum_ = 0
    sum_count = 0
    for j in grades[i]:
        if j == " ":
            continue
        sum_ += int(j)
        sum_count += 1
    grades_average.append(sum_ / sum_count)

print(grades_average)
print(students)
print()

students_list = list(students)
students_grades_dict1 = {}
for i in range(len(students)):
    students_grades_dict1.update({students_list[i]: grades_average[i]})

print("Результат по методу 1:")
print(students_grades_dict1)
print()

# метод 2 - через функцию, распаковку, метод split с разделителем ' '
def grades_average_func(*grades):
    average_ = sum(grades) / len(grades)
    return average_


students_grades_dict2 = {}
for i in range(len(grades)):
    grades_split = map(int, grades[i].split(' '))
    students_grades_dict2.update({students_list[i]: grades_average_func(*grades_split)})

print("Результат по методу 2:")
print(students_grades_dict2)
