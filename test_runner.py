import runner
import unittest


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        test_walk = runner.Runner('test_walk')
        for i in range(10):
            test_walk.walk()
        self.assertEqual(test_walk.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        test_run = runner.Runner('test_run')
        for i in range(10):
            test_run.run()
        self.assertEqual(test_run.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        test_challenge1 = runner.Runner('test_challenge1')
        test_challenge2 = runner.Runner('test_challenge2')
        for i in range(10):
            test_challenge1.run()
            test_challenge2.walk()
        self.assertNotEqual(test_challenge1.distance, test_challenge2.distance)


if __name__ == '__main__':
    unittest.main()
