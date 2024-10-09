"""
test_walk - метод, в котором создаётся объект класса Runner с произвольным именем.
 Далее вызовите метод walk у этого объекта 10 раз.
  После чего методом assertEqual сравните distance этого объекта со значением 50.
test_run - метод, в котором создаётся объект класса Runner с произвольным именем.
 Далее вызовите метод run у этого объекта 10 раз.
  После чего методом assertEqual сравните distance этого объекта со значением 100.
test_challenge - метод в котором создаются 2 объекта класса Runner с произвольными именами.
 Далее 10 раз у объектов вызываются методы run и walk соответственно.
  Т.к. дистанции должны быть разными, используйте метод assertNotEqual,
   чтобы убедится в неравенстве результатов.
Запустите кейс RunnerTest. В конечном итоге все 3 теста должны пройти проверку.
"""

import runner
import unittest


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        test_walk = runner.Runner('test_walk')
        for i in range(10):
            test_walk.walk()
        self.assertEqual(test_walk.distance, 50)

    def test_run(self):
        test_run = runner.Runner('test_run')
        for i in range(10):
            test_run.run()
        self.assertEqual(test_run.distance, 100)

    def test_challenge(self):
        test_challenge1 = runner.Runner('test_challenge1')
        test_challenge2 = runner.Runner('test_challenge2')
        for i in range(10):
            test_challenge1.run()
            test_challenge2.walk()
        self.assertNotEqual(test_challenge1.distance, test_challenge2.distance)


if __name__ == '__main__':
    unittest.main()
