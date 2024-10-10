"""
Напишите класс TournamentTest, наследованный от TestCase. В нём реализуйте следующие методы:

setUpClass - метод, где создаётся атрибут класса all_results.
 Это словарь в который будут сохраняться результаты всех тестов.
setUp - метод, где создаются 3 объекта:
Бегун по имени Усэйн, со скоростью 10.
Бегун по имени Андрей, со скоростью 9.
Бегун по имени Ник, со скоростью 3.
tearDownClass - метод, где выводятся all_results по очереди в столбец.

Так же методы тестирования забегов, в которых создаётся объект Tournament на дистанцию 90.
 У объекта класса Tournament запускается метод start, который возвращает словарь в переменную all_results.
  В конце вызывается метод assertTrue, в котором сравниваются последний объект из all_results
   (брать по наибольшему ключу) и предполагаемое имя последнего бегуна.
Напишите 3 таких метода, где в забегах участвуют (порядок передачи в объект Tournament соблюсти):
Усэйн и Ник
Андрей и Ник
Усэйн, Андрей и Ник.
Как можно понять: Ник всегда должен быть последним.

Дополнительно (не обязательно, не влияет на зачёт):
В данной задаче, а именно в методе start класса Tournament, допущена логическая ошибка.
 В результате его работы бегун с меньшей скоростью может пробежать некоторые дистанции быстрее, чем бегун с большей.
Попробуйте решить эту проблему и обложить дополнительными тестами.
"""
import runner_and_tournament as ran
import unittest


class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.test_runner1 = ran.Runner('Усэйн', 10)
        self.test_runner2 = ran.Runner('Андрей', 9)
        self.test_runner3 = ran.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for tour in cls.all_results:
            print(f'{tour}:')
            for place in cls.all_results[tour]:
                print(f'{place}: {cls.all_results[tour][place]}')
            print()

    def tearDown(self):
        key_tour = list(self.all_results.keys())[-1]
        key_place = list(self.all_results[key_tour].keys())[-1]
        self.assertTrue(self.all_results[key_tour][key_place], self.test_runner3)

    def test_tournament1(self):
        test_tour1 = ran.Tournament(90, self.test_runner1, self.test_runner3)
        self.all_results['test_tournament1'] = test_tour1.start()
        speeds = _form_speeds_list(self.all_results['test_tournament1'])
        self.assertEqual(speeds, sorted(speeds, reverse=True))

    def test_tournament2(self):
        test_tour2 = ran.Tournament(90, self.test_runner2, self.test_runner3)
        self.all_results['test_tournament2'] = test_tour2.start()
        speeds = _form_speeds_list(self.all_results['test_tournament2'])
        self.assertEqual(speeds, sorted(speeds, reverse=True))

    def test_tournament3(self):
        test_tour3 = ran.Tournament(90, self.test_runner1, self.test_runner2, self.test_runner3)
        self.all_results['test_tournament3'] = test_tour3.start()
        speeds = _form_speeds_list(self.all_results['test_tournament3'])
        self.assertEqual(speeds, sorted(speeds, reverse=True))


def _form_speeds_list(tour_results: dict):
    speeds = []
    for place in list(tour_results.keys()):
        speeds.append(tour_results[place].speed)
    return speeds


if __name__ == '__main__':
    unittest.main()
