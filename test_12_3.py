import runner
import unittest

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_walk(self):
        self.runner = runner.Runner("Ivan")
        for i in range (10):
            self.runner.walk()
        self.assertEqual(self.runner.distance, 50)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_run(self):
        self.runner = runner.Runner("Petya")
        for i in range (10):
            self.runner.run()
        self.assertEqual(self.runner.distance, 100)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_challenge(self):
        self.runner = runner.Runner("Runner1")
        self.runner2 = runner.Runner("Runner2")
        for i in range (10):
            self.runner.run()
            self.runner2.walk()
        self.assertNotEqual(self.runner.distance, self.runner2.distance)




import runner_and_tournament as runner2
class TournamentTest(unittest.TestCase):
    is_frozen = True
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner1 = runner2.Runner("Усэйн", 10)
        self.runner2 = runner2.Runner("Андрей", 9)
        self.runner3 = runner2.Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        for key, value in cls.all_results.items():
            print(f"{key} : {value}")

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_zabeg1(self):
        tournament = runner2.Tournament(90, self.runner1, self.runner3)
        self.__class__.all_results = tournament.start()
        self.assertTrue(self.all_results[1], "Усейн")

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_zabeg2(self):
        tournament = runner2.Tournament(90, self.runner2, self.runner3)
        self.__class__.all_results = tournament.start()
        self.assertTrue(self.all_results[1], "Андрей")

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_zabeg3(self):
        tournament = runner2.Tournament(90, self.runner1, self.runner2, self.runner3)
        self.__class__.all_results = tournament.start()
        self.assertTrue(self.all_results[1], "Усэйн")

if __name__ == "__main__":
    unittest.main()
