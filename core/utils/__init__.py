from utilities.proc import commands
from utilities.ui.elements import *
from utilities.ui.status import *
from utilities.ui.text import *

from utilities.feedback import Feedback, coding
from utilities.ui import *


class Utils:
    """
    @apm2 Utility
    """

    def __caller__(self):
        return "utils"

    def Default(self, args={}, _co=False, _argreq=False, _default=False):
        if _co:
            return commands.Command("default", "Default utility called.", self.Default)
        if _argreq:
            return {}
        if _default:
            pass


        print("Default utility called.")

    
    def Help(self, args={}, _co=False, _argreq=False, _default=False):
        if _co:
            return commands.Command("help", "Help utility called.", self.Help)
        if _default:
            pass
        if _argreq:
            return {}


        print("Help utility called.")

    
    def Generate(self, args={}, _co=False, _argreq=False, _default=False):
        if _co:
            return commands.Command("generate", "Generate utility called.", self.Generate)
        
        if _default:
            frame = Frame()
            windowInfo = Window(width=60, my=0)
            windowInfo.SetTitle("Generate Utility")
            windowInfo.SetContent("Generate utility called. This utility is used to generate files, directories, and other resources. It is a powerful tool that can be used to create new projects, files, and more.")
            windowArgs = Window(width=60, my=0)
            windowArgs.SetTitle("Arguments")
            windowArgs.SetContent(dir(args))

            frame.add(windowInfo)
            frame.add(windowArgs)
            frame.Draw()
        
        if _argreq:
            return {"name/string": "Name of the resource to generate."}


    def PackageTemplateBuild(self, args={}, _co=False, _argreq=False, _default=False):
        if _co:
            return commands.Command("package-template-build", "Build a package template.", self.PackageTemplateBuild)
        
        if _default:
            frame = Frame()
            windowInfo = Window(width=60, my=0)
            windowInfo.SetTitle("Package Template Build Utility")
            windowInfo.SetContent("Package Template Build utility can create a package template based on --location and --name arguments.")
            windowArgs = Window(width=60, my=0)
            windowArgs.SetTitle("Arguments")
            windowArgs.SetContent(dir(args))

            frame.add(windowInfo)
            frame.add(windowArgs)
            frame.Draw()
        
        if _argreq:
            return {"name/string": "Name of the package template to build."}
