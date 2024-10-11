import unittest
import test_runner
import test_rat


ratTS = unittest.TestSuite()
ratTS.addTest(unittest.TestLoader().loadTestsFromTestCase(test_runner.RunnerTest))
ratTS.addTest(unittest.TestLoader().loadTestsFromTestCase(test_rat.TournamentTest))

test_runner_ = unittest.TextTestRunner(verbosity=2)
test_runner_.run(ratTS)
