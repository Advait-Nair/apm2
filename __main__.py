import sys

sys.dont_write_bytecode = True

from core import apm2
from utilities.proc import commands

if __name__ == "__main__":
    # get arguments given to the program from the command line
    command = sys.argv[2:]
    # call the main function with the arguments
    apm2.Main(command, sys.argv)
