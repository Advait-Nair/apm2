from utilities.proc import commands
from utilities.ui.elements import *
from utilities.ui.status import *
from utilities.ui.text import *

from utilities.feedback import Feedback, coding as c
from utilities.ui import *

coding = c.StatusCodes()
import os
import json

class Packages:
    """
    @apm2 Utility
    """

    def __caller__(self):
        return "packages"

    def Default(self, args={}, _co=False, _argreq=False, _default=False):
        if _co:
            return commands.Command("default", "Default utility called.", self.Default)
        if _argreq:
            return {}
        if _default:
            pass


        WindowInfo = Window(width=60, mx=2)
        WindowInfo.SetTitle("Packages Utility")
        WindowInfo.SetContent("Packages utility called. This utility is used to manage packages. It is a powerful tool that can be used to install, remove, and update packages.")

        WindowInfo.Output()

    
    def Help(self, args={}, _co=False, _argreq=False, _default=False):
        if _co:
            return commands.Command("help", "Help utility called.", self.Help)


        WindowInfo = Window(width=60, mx=2)
        WindowInfo.SetTitle("Packages Utility Help")
        WindowInfo.SetContent("Packages utility called. This utility is used to manage packages. It is a powerful tool that can be used to install, remove, and update packages.")
        WindowInfo.Output()

    def Uninstall(self, args={}, _co=False, _argreq=False, _default=False, loc=None):
        if _co:
            return commands.Command("uninstall", "Uninstall utility called.", self.Uninstall)
        if _argreq:
            return {'package/string': 'Package to uninstall.'}
        
        WindowInfo = Window(width=60, mx=2)
        WindowInfo.SetTitle(Text.AutoColour("b/blue(Uninstall Utility)"))
        def NoArgs():
            WindowInfo.SetContent(Text.AutoColour("b/blue(Uninstall) a package. Specify a package to uninstall with the b/magenta(--package) attribute to remove it."))
            WindowInfo.Output()
        
        def PackageProvided():
            # Package exists?
            if not os.path.exists(loc('core/'+args.package)):
                f = Feedback(coding.package_not_installed)
                f.SetReference(args.package)
                f.Throw()
                return
            # Package is a file?
            if os.path.isfile(loc('core/'+args.package)):
                f = Feedback(coding.package_malformed)
                f.SetReference('Package is a file instead of a folder.')
                f.Throw()
                return
            # Package is a core package?
            if args.package in ['PackageHandler', 'utils', 'ui', 'status', 'text', 'commands', 'feedback']:
                f = Feedback(coding.package_core)
                f.SetReference(args.package)
                f.Throw()
                return
            # No package.apm2.json?
            if not os.path.exists(os.path.join(loc('core/'+args.package), 'package.apm2.json')):
                f = Feedback(coding.package_malformed)
                f.SetReference('Package does not contain package.apm2.json, which is needed to remove it.')
                f.Throw()
                return
            

            # WindowInfo.SetContent(Text.AutoColour("b/green(Uninstalling) package \"{0}\".".format(args.package)))
            # WindowInfo.Output()

            # edit PackageHandler.py to remove the package
            # remove import at # **import
            # remove utility list at # **add

            # get caller from package.apm2.json
            with open(os.path.join(loc('core/'+args.package), 'package.apm2.json'), 'r') as f:
                package = json.load(f)
                caller = package['loader']
                name = package['name']
                f.close()
                

            with open(loc('core/PackageHandler.py'), 'r') as f:
                data = f.read()
                foldername = args.package
                importPoint = f"from .{name} import *\n# **import"
                addPoint = f"{caller}(), # **add"
                data = data.replace(importPoint, "# **import")
                data = data.replace(addPoint, "# **add")
                f.close()
            with open(loc('core/PackageHandler.py'), 'w') as f:
                f.write(data)
                f.close()

            # remove folder from packages
            os.system(f"rm -r {loc('core/'+foldername)}")
            # output
            WindowInfo.SetContent(Text.AutoColour("b/green(Uninstalled) package \"{0}\".".format(args.package.strip())))
            WindowInfo.Output()
        
        if _default:
            NoArgs()
        else:
            PackageProvided()

    
    def Install(self, args={}, _co=False, _argreq=False, _default=False, loc=None):
        if _co:
            return commands.Command("install", "Install utility called.", self.Install)
        if _argreq:
            return {'location/string': 'Location of package to install.'}
        
        try: verbose = args.v
        except: verbose = False

        def vprint(*args, **kwargs):
            if verbose: print(*args, **kwargs)
        
        WindowInfo = Window(width=60, mx=2)
        WindowInfo.SetTitle(Text.AutoColour("b/blue(Install Utility)"))
        def NoArgs():
            WindowInfo.SetContent(Text.AutoColour("b/blue(Install) a package. Specify a b/magenta(--location) attribute to beam it from a specific location."))
            WindowInfo.Output()

        def LocationProvided():
            # Location exists?
            if not os.path.exists(args.location):
                f = Feedback(coding.file_does_not_exist)
                f.SetReference(args.location)
                f.Throw()
                return
            # Location already installed?
            if os.path.exists(loc('core/'+args.location.split('/')[-1])):
                f = Feedback(coding.package_already_installed)
                f.SetReference(args.location)
                f.Throw()
                return
            # Location is a file?
            if os.path.isfile(args.location):
                f = Feedback(coding.package_malformed)
                f.SetReference('Location is a file instead of a folder.')
                f.Throw()
                return
            # Location doesn't have __init__.py and package.apm2?
            if not os.path.exists(os.path.join(args.location, '__init__.py')) or not os.path.exists(os.path.join(args.location, 'package.apm2.json')):
                f = Feedback(coding.package_malformed)
                f.SetReference('Location does not contain __init__.py or package.apm2.json')
                f.Throw()
                return



            # WindowInfo.SetContent(Text.AutoColour("b/green(Installing) package from \"{0}\".".format(args.location)))
            # WindowInfo.Output()

            # first, read the package.apm2.json file
            with open(os.path.join(args.location, 'package.apm2.json'), 'r') as f:
                package = json.load(f)

                # load package name, version, and description
                try:
                    name = package['name'].lower()
                    version = package['version']
                    description = package['description']
                    loader = package['loader']
                except:
                    f = Feedback(coding.package_malformed)
                    f.SetReference('package.apm2.json is malformed or missing required fields: name, version, description, loader.')
                    f.Throw()
                    return
                
                # output

                WindowInfo.SetContent(Text.AutoColour("b/green(Installing) the requested package \"b/blue({0})\" b/magenta(v{1}): {2}".format(name.strip(), version.strip(), description.strip())))
                WindowInfo.Output()

                # edit PackageHandler.py to include the package
                # insert import at # **import
                # insert utility list at # **add
                # try: 
                with open(loc('core/PackageHandler.py'), 'r') as f:
                    data = f.read()
                    foldername = args.location.split('/')[-1]
                    importPoint = f"from .{foldername} import *\n# **import"
                    addPoint = f"{loader}(), # **add"
                    data = data.replace("# **import", importPoint)
                    data = data.replace("# **add", addPoint)



                    vprint (data)
                    f.close()
                with open(loc('core/PackageHandler.py'), 'w') as f:
                    f.write(data)
                    f.close()

                # copy folder to packages
                os.system(f"cp -r {args.location} {loc('core/'+foldername)}")
                # output
                WindowInfo.SetContent(Text.AutoColour("b/green(Installed) package \"b/blue({0})\" b/magenta(v{1})".format(name.strip(), version.strip())))

                WindowInfo.Output()

                # except Exception as e:
                #     # needs sudo
                #     f = Feedback(coding.internal_error)
                #     f.SetReference(e)
                #     f.Throw()
                


        
        if _default:
            NoArgs()
        else:
            LocationProvided()


    def PackageReload(self, args={}, _co=False, _argreq=False, _default=False, loc=None):
        if _co:
            return commands.Command("reload", "Reload packages (uninstall -> reinstall)", self.PackageReload)
        if _argreq:
            return {"location/string": "Location of package to reload."}
        if _default:
            WindowInfo = Window(width=60, mx=2)
            WindowInfo.SetTitle(Text.AutoColour("b/blue(Package Reload Utility)"))
            WindowInfo.SetContent("Reloading packages. This will reload all packages and their utilities.")
            WindowInfo.Output()
            return

        # get package.apm2.json
        try:
            with open(os.path.join(args.location, 'package.apm2.json'), 'r') as f:
                package = json.load(f)
                try:
                    name = package['name'].lower()
                    # version = package['version']
                    # description = package['description']
                    # loader = package['loader']
                except:
                    f = Feedback(coding.package_malformed)
                    f.SetReference('package.apm2.json is malformed or missing required fields: name.')
                    f.Throw()
                    return

            class packageInfo:
                def __init__(self, package, location):
                    self.package = package
                    self.location = location
            pi = packageInfo(package=name, location=args.location)
            self.Uninstall(args=pi, loc=loc)
            self.Install(args=pi, loc=loc)
        except Exception as e:
            f = Feedback(coding.file_does_not_exist)
            f.SetReference(f'Failed to reload package. {e}')
            f.Throw()
