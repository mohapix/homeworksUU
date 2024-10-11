import runner_and_tournament as rat
import unittest


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.test_runner1 = rat.Runner('Усэйн', 10)
        self.test_runner2 = rat.Runner('Андрей', 9)
        self.test_runner3 = rat.Runner('Ник', 3)

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

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tournament1(self):
        test_tour1 = rat.Tournament(90, self.test_runner1, self.test_runner3)
        self.all_results['test_tournament1'] = test_tour1.start()
        speeds = _form_speeds_list(self.all_results['test_tournament1'])
        self.assertEqual(speeds, sorted(speeds, reverse=True))

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tournament2(self):
        test_tour2 = rat.Tournament(90, self.test_runner2, self.test_runner3)
        self.all_results['test_tournament2'] = test_tour2.start()
        speeds = _form_speeds_list(self.all_results['test_tournament2'])
        self.assertEqual(speeds, sorted(speeds, reverse=True))

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tournament3(self):
        test_tour3 = rat.Tournament(90, self.test_runner1, self.test_runner2, self.test_runner3)
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
