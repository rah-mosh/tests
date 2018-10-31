import unittest
#from prepcourse.lab1.exercise1 import hello_world #https://stackoverflow.com/questions/16981921/relative-imports-in-python-3
from user.lab1.exercise1 import hello_world #https://stackoverflow.com/questions/16981921/relative-imports-in-python-3


class TestExerciseSet(unittest.TestCase):

    def test_helloworld(self):
        self.assertEqual(hello_world(), 'Hello, world!')

if __name__ == '__main__':
    unittest.main()