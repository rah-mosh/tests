import unittest
from test.score import Score
from user.DAT110.exercise2 import geometric_series, is_divisible, smallest_divisible, is_prime, is_leapyear

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
