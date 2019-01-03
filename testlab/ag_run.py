import unittest
#from prepcourse.lab1.exercise1 import hello_world #https://stackoverflow.com/questions/16981921/relative-imports-in-python-3
#from prepcourse_test.score import Score
from user.lab1.exercise1 import hello_world #https://stackoverflow.com/questions/16981921/relative-imports-in-python-3
from test.score import Score


class TestExerciseSet(unittest.TestCase):
    score = Score(10, 10, 'lab1_ex1')

    def test_helloworld(self):
        if hello_world() == 'Hello, world!':
            self.score.increment_by(10)
            print(self.score.write_json())
        self.assertEqual(hello_world(), 'Hello, world!')

if __name__ == '__main__':
    unittest.main()