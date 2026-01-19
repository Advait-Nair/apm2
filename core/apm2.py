from utilities.feedback import Feedback
from utilities.feedback.coding import StatusCodes
from utilities.proc import commands

# Utilities
from .PackageHandler import UtilityList
from . import *  # Default Utility cannot be removed
from .packages import Packages  # Core package utility cannot be removed

def Main(command, argv) -> int:
    '''
    Main entry point for APM2. Calling apm2.Main() will call a parser that executes requested commands.
    The program will return an integer value to the caller when the process terminates.
    '''

    # Publish Utilities
    utilities = UtilityList
    utilities.append(Default())
    utilities.append(Packages())

    # Format sys entries: merge all items with index 2 or more together
    # request = command[0:2] + [' '.join(command[2:])]
    request = command

    
    # Parse the request
    requester = commands.Request(request, utilities)
    fulfill = requester.ParseRequest(request, argv)

    if fulfill: fulfill()