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

print('Extracting code fro ipynb.')
path_wo_fileending = 'user/DAT110/exercise2'
f = Path(path_wo_fileending + '.ipynb')
print('Could {} find file.'.format('not' if not f.is_file() else ''))
success = extract(path_wo_fileending + '.ipynb', path_wo_fileending + '.py')
print('Code extraction was {}'.format('successful.' if success else 'unsuccessful.'))


#from user.DAT110.exercise1 import falling_object, sum_integers, falling_object_more

# TODO: should the imports be in try-except clause?
# TODO: extract tests for different exercises in different files.


# import your test modules
import ex1
import ex2
import ex3

# initialize the test suite
loader = unittest.TestLoader()
suite  = unittest.TestSuite()

# add tests to the test suite
suite.addTests(loader.loadTestsFromModule(ex1))
suite.addTests(loader.loadTestsFromModule(ex2))
suite.addTests(loader.loadTestsFromModule(ex3))

try:
    # initialize a runner, pass it your suite and run it
    runner = unittest.TextTestRunner(verbosity=3)
    result = runner.run(suite)

except Exception as e:
    print(e)