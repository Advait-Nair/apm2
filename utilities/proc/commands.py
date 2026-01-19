"""
Process commands & requests with ease and structure.

[Caller] [Utility] [Command] [Arguments]

```sh
anair@adva-remote ~ % apm2 generate html-meta --title "Hello, World!" --author "John Doe" --date "2021-01-01" --description "This is a test page." --keywords "test, page, hello, world" --output "test.html"
```
"""

from ..ui.elements import Window
from ..ui import *
from ..feedback import *

import re

class Command:
    def __init__(self, call, description, function):
        self.call = call
        self.description = description
        self.function = function
        self.optional_args_to_fill = []
        self._parseOptionalArgs()

    def __caller__(self):
        return self.call

    def __str__(self):
        DescriptionFrame = Frame()

        Desc = Window()
        Desc.SetContent(self.description)
        Desc.SetTitle(self.call)
        DescriptionFrame.add(Desc)
        DescriptionFrame.Draw()

        return DescriptionFrame.__str__()

    def _parseOptionalArgs(self):
        argsNeeded = self.function(_argreq=True)
        if argsNeeded == None:
            argsNeeded = {}
        
        for key in argsNeeded:
            # Required argument not found?
            if '?' in key:
                self.optional_args_to_fill.append(key.split('?/')[0])
    
    
    def Execute(self, args):
        # check if args are present and auto-feedback/enter if not
        argsNeeded = self.function(_argreq=True)
        # lookup each dictionary key in argsNeeded, splitting the key by / to get the left parameter and right type

        if argsNeeded == None:
            argsNeeded = {}
        
        # if no args, call with _default=True
        if args == None:
            self.function(_default=True)
            return

        for key in argsNeeded:
            # Required argument not found?
            if (key.split('/')[0] not in dir(args)) and not ('?' in key):
                err = Feedback(coding.StatusCodes().missing_argument)
                err.SetReference(f"{key}: {argsNeeded[key]}")
                err.Throw()
                return
            # elif '?' in key:
            #     self.optional_args_to_fill.append(key.split('?/')[0])
        
        def loc (root_reference):
            if args.__cdloc__:
                # print (args.__cdloc__ + root_reference)
                return args.__cdloc__ + root_reference
            else:
                # error
                err = Feedback(coding.StatusCodes().internal_argument_not_found)
                err.SetReference(f"__cdloc__ in {args}")
        
        
        self.function(args,loc=loc)


class Request:
    def __init__(self, request, utilities):
        self.request = request
        self.utilities = utilities
        # self.ParseRequest(self.request)
    
    def SetUtilities(self, utilities):
        """
        Set the utilities class for the request.
        """
        self.utilities = utilities

    def ParseArguments(self, args, argv, optionalsToFill=[]):
        """
        Parse the arguments into a dictionary.

        ```
        apm2 generate html-meta --title "Hello, World!" --author "John Doe" --date "2027-02-04" --description "This is a test page." --keywords "test, page, hello, world" --output "test.html" --number 4 -f
        ```
        """
        arguments = {}

        if args == None or len(args) == 0:
            return None

        for arg in args:
            if arg.startswith("--"):
                # valuated argument
                # check if index above exists, if not throw malformed input error
                if args.index(arg) + 1 >= len(args):
                    err = Feedback(coding.StatusCodes().malformed_input)
                    err.SetReference(f"{arg}")
                    err.Throw()
                    return None
                
                def formatIfNumber(val):
                    if val.isdigit():
                        return int(val)
                    elif re.match(r'^\d+\.\d+$', val):
                        return float(val)
                    else:
                        return val

                # add to dictionary
                arguments[arg.replace("--",'')] = formatIfNumber(args[args.index(arg) + 1])

            elif arg.startswith("-") and not arg.startswith("--"):
                # flag argument
                arguments[arg.replace('-','')] = True
        
        for opt in optionalsToFill:
            if opt in arguments:
                continue
            arguments[opt] = False
        
        # print (f"Arguments: {arguments}, otf: {optionalsToFill}")


        arguments['__cdloc__'] = argv[0].split('/__main')[0]+'/'
        MapDictToClass = lambda x: type('Arguments', (object,), x)()

        return MapDictToClass((arguments))
    

    def ParseRequest(self, req, argv):
        """
        Parse the request into a utility, command and arguments.
        Returns a lambda function that when called, executes the command if present.add()

        ```python
        requester = commands.Request(request, utilities)
        fulfill = requester.ParseRequest(request)

        if fulfill:
            fulfill()
        """
        
        # inits
        self.utility = ""
        self.command = ""
        self.arguments = {}

        if len(req) >= 1:
            # if utility given
            self.utility = req[0].strip().lower()
        if len(req) >= 2:
            # if command given
            self.command = req[1].strip().lower()
        # if arguments are present
        if len(req) > 2:
            self.arguments = req[2:]
        
        # if no utility given
        if self.utility == "": self.utility = "default"
        # if no command given
        if self.command == "": self.command = "default"




        # match utility; return error if not found
        such_utility = False
        utilityObject = None
        for utility in self.utilities:
            if utility.__caller__() == self.utility:
                self.utility = PublishUtility(utility).BuildCommandLists()
                utilityObject = utility
                such_utility = True
                break
        if not such_utility:
            err = Feedback(coding.StatusCodes().no_such_method)
            err.SetReference(f"{self.utility}:{self.command}")
            err.Throw()
            return
        
        # match command; return error if not found
        such_command = False
        for command in self.utility:
            if command.__caller__() == self.command:
                self.command = command
                such_command = True
                break
        if not such_command:
            err = Feedback(coding.StatusCodes().no_such_method)
            err.SetReference(f"{utilityObject.__caller__()}:{self.command}")
            err.Throw()
            return
        
        # print(self.command.optional)
        return lambda: self.command.Execute(self.ParseArguments(self.arguments, argv, optionalsToFill=self.command.optional_args_to_fill))
        


    def __str__(self):
        return f"Utility: {self.utility}\nCommand: {self.command}\nArguments: {self.arguments}"


class PublishUtility:
    """
    @apm2 Executable List
    """
    def __init__(self, UtilityClass):
        self.UtilityClass = UtilityClass
    
    def BuildCommandLists(self):
        # call every method in the utility class and return the list of command classes
        commandlist = []
        for method in dir(self.UtilityClass):
            if callable(getattr(self.UtilityClass, method)) and not method.startswith("__"):
                commandlist.append(getattr(self.UtilityClass, method)(_co=True))
        return commandlist
