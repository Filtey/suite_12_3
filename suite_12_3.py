import unittest
import test_12_3 as Tests


testsuite = unittest.TestSuite()

testsuite.addTest(unittest.TestLoader().loadTestsFromTestCase(Tests.RunnerTest))
testsuite.addTest(unittest.TestLoader().loadTestsFromTestCase(Tests.TournamentTest))

texttest = unittest.TextTestRunner(verbosity=2)
texttest.run(testsuite)