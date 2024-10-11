import unittest
import tests_12_4 as test_runner
import test_rat
import logging

logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log',
                        encoding='UTF-8', format='%(asctime)s | %(levelname)s | %(message)s')

ratTS = unittest.TestSuite()
ratTS.addTest(unittest.TestLoader().loadTestsFromTestCase(test_runner.RunnerTest))
ratTS.addTest(unittest.TestLoader().loadTestsFromTestCase(test_rat.TournamentTest))

test_runner_ = unittest.TextTestRunner(verbosity=2)
test_runner_.run(ratTS)
