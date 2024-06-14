# -*- coding: utf-8 -*-

team1_name = 'Мастера кода'
team2_name = 'Волшебники данных'
team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
tasks_total = 82
team1_time = 1552.512
team2_time = 2153.31451
time_avg = (team1_time + team2_time) / tasks_total
challenge_result = 'Победа команды '

if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    challenge_result += team1_name
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    challenge_result += team2_name
else:
    challenge_result = 'Ничья!'

# Использование %
print('В команде %s участников: %d !' % (team1_name, team1_num))
print('Итого сегодня в командах участников: %d и %d !' % (team1_num, team2_num))

# Использование format()
print('Команда {} решила задач: {} !'.format(team2_name, score_2))
print('{name} решили задачи за {time:6.2f} с !'.format(name=team2_name, time=team2_time))

# Использование f-строк
print(f'Команды решили {score_1} и {score_2} задач.')
print(f'Результат битвы: {challenge_result:-^40s}')
print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg:07.2f} секунды на задачу!')
