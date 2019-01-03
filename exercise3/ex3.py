import unittest
from test.score import Score
from user.DAT110.exercise3 import Player

class TestPlayer(unittest.TestCase):
    score = Score(70, 100, 'TestPlayer')
    points_worth = 0

    @classmethod
    def tearDownClass(cls):
        print(cls.score.write_json())

    def tearDown(self):
        result = self.defaultTestResult()
        self._feedErrorsToResult(result, self._outcome.errors)
        error = result.errors
        failure = result.failures
        ok = not error and not failure
        if ok:
            self.score.increment_by(self.points_worth)

    def setUp(self):
        self.p = Player("Ola")

    def test_get_name(self):
        self.points_worth = 5
        self.assertEqual(self.p.get_name(), "Ola")

    def test_set_name(self):
        self.points_worth = 5
        self.p.set_name("Jens")
        self.assertEqual(self.p.get_name(), "Jens")

    def test_set_name_empty(self):
        self.points_worth = 5
        self.p.set_name("")
        self.assertEqual(self.p.get_name(), "Ola")

    def test_get_points_zero(self):
        self.points_worth = 5
        self.assertEqual(self.p.get_points(), 0)

    def test_add_points(self):
        self.points_worth = 5
        self.p.add_points(7)
        self.assertEqual(self.p.get_points(), 7)

    def test_set_points(self):
        self.points_worth = 5
        self.p.set_points(50)
        self.assertEqual(self.p.get_points(), 50)

    def test_set_negative_points(self):
        self.points_worth = 5
        self.p.set_points(-50)
        self.assertEqual(self.p.get_points(), 0)

    def test_get_ID(self):
        self.points_worth = 5
        self.assertTrue(isinstance(self.p.get_ID(), int))

    def test_id(self):
        self.points_worth = 10
        p2 = Player("Knut")
        self.assertTrue(p2.get_ID() != self.p.get_ID())

    def test_toString(self):
        self.points_worth = 20
        self.assertEqual(str(self.p), "Player " + str(self.p.get_ID()) + ": Ola has points: 0")