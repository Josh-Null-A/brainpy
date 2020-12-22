import sys
import os

from lexer       import Lexer
from interpreter import Interpreter

def check_file(file_path):
    """
        Called upon loading this file.
        Loads a BrainF**k file and passes it to a lexer and parser.

        Parameters
        ==========
            file_path: str
                       The file path for any file ending in a .bf prefix.
    """

    # Try to find the file path given by the user.
    if os.path.exists(file_path):
        # Assert that the user has given us a BrainF**k file.
        assert file_path[-3:] == '.bf' or file_path[-2:] == '.b', 'File prefix must end in .bf'

        # Call the run function.
        run(file_path)

    else:
        print(f'FileNotFoundError: Cannot find file with path {file_path}')
        quit()

def run(file):
    """
        Handles the flow of the data of a .bf file.

        Parameters
        ==========
            file: str
                  The file path for any file ending in a .bf prefix.
    """

    tokens = Lexer.find_tokens(file)
    Interpreter.interpret(tokens)

if __name__ == '__main__':
    check_file(sys.argv[1])
