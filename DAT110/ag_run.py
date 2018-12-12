import unittest
from pathlib import Path
from test.score import Score
from test.code_extractor import extract

print('Extracting code fro ipynb.')
path_wo_fileending = 'user/DAT110/exercise1'

f = Path(path_wo_fileending + '.ipynb')
print('Could {} find file.'.format('not' if not f.is_file() else ''))

success = extract(path_wo_fileending + '.ipynb', path_wo_fileending + '.py')
print('Code extraction was {}'.format('successful.' if success else 'unsuccessful.'))

from user.DAT110.exercise1 import falling_object, sum_integers, falling_object_more


print('Extracting code fro ipynb.')
path_wo_fileending = 'user/DAT110/exercise2'

f = Path(path_wo_fileending + '.ipynb')
print('Could {} find file.'.format('not' if not f.is_file() else ''))

success = extract(path_wo_fileending + '.ipynb', path_wo_fileending + '.py')
print('Code extraction was {}'.format('successful.' if success else 'unsuccessful.'))

from user.DAT110.exercise2 import geometric_series, is_divisible, smallest_divisible, is_prime, is_leapyear


print('Extracting code fro ipynb.')
path_wo_fileending = 'user/DAT110/exercise3'

f = Path(path_wo_fileending + '.ipynb')
print('Could {} find file.'.format('not' if not f.is_file() else ''))

success = extract(path_wo_fileending + '.ipynb', path_wo_fileending + '.py')
print('Code extraction was {}'.format('successful.' if success else 'unsuccessful.'))

from user.DAT110.exercise3 import Player

# TODO: should the imports be in try-except clause?
# TODO: extract tests for different exercises in different files.


class TestFallingObject(unittest.TestCase):
    score = Score(10, 10, 'TestFallingObject')
    points_worth = 0

    @classmethod
    def tearDownClass(cls):
        print(cls.score.write_json())

    def tearDown(self):  # https://stackoverflow.com/questions/4414234/getting-pythons-unittest-results-in-a-teardown-method : hynekcer
        result = self.defaultTestResult()
        self._feedErrorsToResult(result, self._outcome.errors)
        error = result.errors
        failure = result.failures
        ok = not error and not failure
        if ok:
            self.score.increment_by(self.points_worth)

    def test_normal_case_1(self):
        self.points_worth = 4
        self.assertEqual(falling_object(10), 981.00)

    def test_normal_case_2(self):
        self.points_worth = 4
        self.assertEqual(falling_object(56), 30764.16)

    def test_falling_object_negative(self):
        self.points_worth = 2
        with self.assertRaises(Exception): falling_object(-1)


class TestSumIntegers(unittest.TestCase):
    score = Score(8, 20, 'TestSumIntegers')
    points_worth = 0

    @classmethod
    def tearDownClass(cls):
        print(cls.score.write_json())

    def tearDown(self):  # https://stackoverflow.com/questions/4414234/getting-pythons-unittest-results-in-a-teardown-method : hynekcer
        result = self.defaultTestResult()
        self._feedErrorsToResult(result, self._outcome.errors)
        error = result.errors
        failure = result.failures
        ok = not error and not failure
        if ok:
            self.score.increment_by(self.points_worth)

    def test_normal_case_1(self):
        self.points_worth = 2
        self.assertEqual(sum_integers([10, 10]), 20)

    def test_normal_case_2(self):
        self.points_worth = 2
        self.assertEqual(sum_integers([90, 10, 45, 25]), 170)

    def test_zero(self):
        self.points_worth = 2
        self.assertEqual(sum_integers([0, 0]), 0)

    def test_negative(self):
        self.points_worth = 2
        with self.assertRaises(Exception): sum_integers([1, 20, -1])


class TestFallingObjectMore (unittest.TestCase):
    score = Score(10, 20, 'TestFallingObjectMore')
    points_worth = 0

    @classmethod
    def tearDownClass(cls):
        print(cls.score.write_json())

    def tearDown(self):  # https://stackoverflow.com/questions/4414234/getting-pythons-unittest-results-in-a-teardown-method : hynekcer
        result = self.defaultTestResult()
        self._feedErrorsToResult(result, self._outcome.errors)
        error = result.errors
        failure = result.failures
        ok = not error and not failure
        if ok:
            self.score.increment_by(self.points_worth)

    def test_normal_case_1(self):
        self.points_worth = 2
        self.assertEqual(falling_object_more(20, 5), [3924.00, 15696.00, 15696.00, 35316.00, 62784.00])

    def test_zero_1(self):
        self.points_worth = 2
        self.assertEqual(falling_object_more(3, 0), [])

    def test_zero_2(self):
        self.points_worth = 2
        with self.assertRaises(Exception): falling_object_more(0, 3)

    def test_negative_1(self):
        self.points_worth = 2
        with self.assertRaises(Exception): falling_object_more(-1, 3)

    def test_negative_2(self):
        self.points_worth = 2
        with self.assertRaises(Exception): falling_object_more(1, -1)


class TestGeometricSeries(unittest.TestCase):
    score = Score(4, 10, 'TestGeometricSeries')
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

    def test_normal_case_1(self):
        self.points_worth = 1
        self.assertEqual(geometric_series(4, 10, 5), 444444)

    def test_normal_case_2(self):
        self.points_worth = 1
        self.assertEqual(geometric_series(-1, 10, 5), -111111)

    def test_normal_case_3(self):
        self.points_worth = 1
        self.assertEqual(geometric_series(-1, -1, 5), 0)

    def test_normal_case_4(self):
        self.points_worth = 1
        self.assertEqual(geometric_series(-1, -1, 4), -1)


class TestIsDivisible(unittest.TestCase):
    score = Score(3, 10, 'TestIsDivisible')
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

    def test_normal_case_1(self):
        self.points_worth = 1
        self.assertEqual(is_divisible(4, 2), True)

    def test_normal_case_2(self):
        self.points_worth = 1
        self.assertEqual(is_divisible(3, 2), False)

    def test_normal_case_3(self):
        self.points_worth = 1
        self.assertEqual(is_divisible(0, 1), True)


class TestSmallestDivisible(unittest.TestCase):
    score = Score(6, 10, 'TestSmallestDivisible')
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

    def test_normal_case_1(self):
        self.points_worth = 2
        self.assertEqual(smallest_divisible(10), 2)

    def test_normal_case_2(self):
        self.points_worth = 2
        self.assertEqual(smallest_divisible(9), 3)

    def test_normal_case_3(self):
        self.points_worth = 1
        self.assertEqual(smallest_divisible(1), -1)

    def test_normal_case_4(self):
        self.points_worth = 1
        self.assertEqual(smallest_divisible(0), -1)


class TestIsPrime(unittest.TestCase):
    score = Score(7, 10, 'TestIsPrime')
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

    def test_normal_case_1(self):
        self.points_worth = 1
        self.assertEqual(is_prime(2), True)

    def test_normal_case_2(self):
        self.points_worth = 1
        self.assertEqual(is_prime(3), True)

    def test_normal_case_3(self):
        self.points_worth = 1
        self.assertEqual(is_prime(5), True)

    def test_normal_case_4(self):
        self.points_worth = 1
        self.assertEqual(is_prime(6), False)

    def test_normal_case_5(self):
        self.points_worth = 1
        self.assertEqual(is_prime(9), False)

    def test_normal_case_6(self):
        self.points_worth = 1
        self.assertEqual(is_prime(10), False)

    def test_normal_case_7(self):
        self.points_worth = 1
        self.assertEqual(is_prime(1279), True)


class TestIsLeapYear(unittest.TestCase):
    score = Score(7, 10, 'TestIsLeapYear')
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

    def test_normal_case_1(self):
        self.points_worth = 1
        self.assertEqual(is_leapyear(1828), True)

    def test_normal_case_2(self):
        self.points_worth = 1
        self.assertEqual(is_leapyear(2020), True)

    def test_normal_case_3(self):
        self.points_worth = 1
        self.assertEqual(is_leapyear(2148), True)

    def test_normal_case_4(self):
        self.points_worth = 1
        self.assertEqual(is_leapyear(2268), True)

    def test_normal_case_5(self):
        self.points_worth = 1
        self.assertEqual(is_leapyear(2300), False)

    def test_normal_case_6(self):
        self.points_worth = 1
        self.assertEqual(is_leapyear(2200), False)

    def test_normal_case_7(self):
        self.points_worth = 1
        self.assertEqual(is_leapyear(2018), False)


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

if __name__ == '__main__':
    unittest.main()
