import rt_with_exceptions as runner
import logging
import unittest


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        try:
            test_walk = runner.Runner('test_walk', -5)
        except ValueError:
            logging.warning(f'Неверная скорость для Runner', exc_info=True)
        else:
            for i in range(10):
                test_walk.walk()
            self.assertEqual(test_walk.distance, 50)
            logging.info('"test_walk" выполнен успешно')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        try:
            test_run = runner.Runner(10)
        except TypeError:
            logging.warning(f'Неверный тип данных для объекта Runner', exc_info=True)
        else:
            for i in range(10):
                test_run.run()
            self.assertEqual(test_run.distance, 100)
            logging.info('"test_run" выполнен успешно')


    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        test_challenge1 = runner.Runner('test_challenge1')
        test_challenge2 = runner.Runner('test_challenge2')
        for i in range(10):
            test_challenge1.run()
            test_challenge2.walk()
        self.assertNotEqual(test_challenge1.distance, test_challenge2.distance)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log',
                        encoding='UTF-8', format='%(asctime)s | %(levelname)s | %(message)s')
    unittest.main()
