from pathlib import Path
import os
import json

# Extracts code in Jupyter Notebook files to a new Python file
def extract(filename, new_filename):
    code_cells = []
    f = Path(filename)
    if not f.is_file():
        print('Could not find file.')
        return False

    with open(filename, 'r') as file:
        ipynb = json.load(file)
        for cell in ipynb['cells']:
            if (cell['cell_type'] == 'code'):
                code_cells.append(cell['source'])

    with open (new_filename, 'w+') as file:
        print('Extracting file to {}'.format(os.getcwd()))
        for cell in code_cells:
            file.write('\n\n' + ''.join(str(line) for line in cell))

    return True

#extract('../assignments/DAT110_ass1/falling_object.ipynb', 'falling_object.py')