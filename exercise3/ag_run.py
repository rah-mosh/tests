import unittest
from pathlib import Path
from test.score import Score
from test.code_extractor import extract

print('Extracting code fro ipynb.')
path_wo_fileending = 'user/DAT110/exercise3'
f = Path(path_wo_fileending + '.ipynb')
print('Could {} find file.'.format('not' if not f.is_file() else ''))
success = extract(path_wo_fileending + '.ipynb', path_wo_fileending + '.py')
print('Code extraction was {}'.format('successful.' if success else 'unsuccessful.'))

import ex3

# initialize the test suite
loader = unittest.TestLoader()
suite  = unittest.TestSuite()

suite.addTests(loader.loadTestsFromModule(ex3))

try:
    # initialize a runner, pass it your suite and run it
    runner = unittest.TextTestRunner(verbosity=3)
    result = runner.run(suite)
except Exception as e:
    print(e)
