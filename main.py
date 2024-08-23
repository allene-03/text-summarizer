import sys
from main_code import *

try:
    if __name__ == '__main__':
        args = sys.argv[1:]
        if args[0] == '-f':
            Modifier(False)
        elif args[0] == '-fw':
            Modifier(True)
        elif args[0] == '--v':
            Version()
        else:
            ArgumentErrors()
except IndexError:
    ArgumentErrors()
