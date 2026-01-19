from utilities.proc import commands
from utilities.ui.elements import *
from utilities.ui.status import *
from utilities.ui.text import *

from utilities.feedback import Feedback, coding as c
from utilities.ui import *

coding = c.StatusCodes()
import os
import json

class APYTools:
    """
    @apm2 Utility
    """

    def __caller__(self):
        return "prun"

    def Default(self, args={}, _co=False, _argreq=False, _default=False, noVenv=False):
        if _co:
            return commands.Command("default", "APYTOOLS PythonRun (prun)", self.Default)
        if _argreq:
            return {"version/string": "Python version to run the project with (default: 3.12)"}
        if _default:
            pass

        def InvalidVersion():
            f = Feedback(coding.package_not_installed)
            f.SetReference(f"python{v}")
            f.Throw()

        
        WindowInfo = Window(width=60, mx=2)
        WindowInfo.SetTitle("Python Run | prun")
        WindowInfo.SetContent("Running project at __main__ root. Specify a python version to run the project with (default: 3.12). Use --nvenv 1 to disable venv detection.")
        WindowInfo.Output()

        v = "3.12"

        if "version" in args:
            v = args["version"]


        # Check if the version is installed
        if not os.path.exists(f"/usr/bin/python{v}") and not os.path.exists(f"/usr/local/bin/python{v}"):
            InvalidVersion()
            return
        
        use_venv = False
        if os.path.exists("./venv"): use_venv = './venv'
        if os.path.exists("./.venv"): use_venv = './.venv'
        

        if noVenv: use_venv = False

        try:
            mainExists = os.path.exists("./__main__.py")
            if use_venv:
                WindowInfo = Window(width=60, mx=2)
                WindowInfo.SetTitle("Python Run | prun")
                WindowInfo.SetContent("A venv has been detected. Running from venv.")
                WindowInfo.Output()
                # Run the venv python: if __main__ found
                if mainExists:
                    os.system(f"source {use_venv}/bin/activate && python{v} -B .")
                    return
                os.system(f"source {use_venv}/bin/activate && python{v} -B main.py")
            
            # Normal python run
            if mainExists: 
                os.system(f"python{v} -B .")
                return
            os.system(f"python{v} -B main.py")
            
        except Exception as e:
            f = Feedback(coding.package_not_installed)
            f.SetReference(f"Failed to run the project with {'venv ' if use_venv else ''}python {v}: {e}")
            f.Throw()
            return
    
    def NoVenv(self, args={}, _co=False, _argreq=False, _default=False):
        if _co:
            return commands.Command("novenv", "APYTOOLS PythonRun (prun)", self.NoVenv)
        if _argreq:
            return {"version/string": "Python version to run the project with (default: 3.12)"}
        if _default:
            pass

        return self.Default(args, _co=_co, noVenv=True)