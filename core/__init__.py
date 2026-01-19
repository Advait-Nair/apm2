from utilities.proc import commands

import utilities.ui as ui
from utilities.ui import elements, status, text


class Default:
    """
    @apm2 Default call
    """

    def __caller__(self):
        return "default"

    def Default(self, args={}, _co=False, _argreq=False, _default=False):
        if _co:
            return commands.Command("default", "Default utility called.", self.Default)
        if _argreq:
            return {}
        if _default: # Has the default only been called? As in, apm2 only (in this case)?
            pass

        Welcome = ui.Frame()

        WindowWelcome = elements.Window(width=60, mx=4)
        WindowWelcome.SetTitle("Welcome to " + text.Text("APM2",'b/blue').GetContent())
        WindowWelcome.SetContent(text.Text.AutoColour("Welcome to bi/magenta(apm2)! Call 'help' for a list of commands."))
        Welcome.add(WindowWelcome)

        Welcome.Draw()

    def Help(self, args={}, _co=False, _argreq=False, _default=False):
        if _co:
            return commands.Command("help", "Help utility called.", self.Help)
        if _argreq:
            return {}
        if _default:
            pass
        WindowHelp = elements.Window(width=60, mx=4)
        WindowHelp.SetTitle("Help")

        # Aggregate all commands
        commands_list = []
        # for cmd in


        