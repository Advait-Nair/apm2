from ..text import Text
from ..elements import Window
from ...feedback import coding


class StatusDialog (Window):
    def __init__(self, ErrorCode) -> None:
        self.ErrorCode = ErrorCode
        self.Message = coding.StatusAsMessage(ErrorCode).__str__()
        super().__init__(px=2, py=2, mx=2, my=2, width=60, height=10)
        self.Content = self.Message
    
    def Draw(self):
        """
        Draw the status dialog. Often called by the Frame object, but can be individually called.

        ```python
        Frame = ui.Frame()
        status_window = error.StatusDialog(self.status_code)
        Frame.add(status_window)

        Frame.Draw()

        print(status_window)

        status_window.SetReference('main.py/line:10')
        status_window.Draw() # Will be auto-called by the Frame or StatusDialog object.

        print(status_window.__str__())

        ```
        """
        # Draw two containers, one a title, the other the message.
        w = Window(self.px, self.py, self.mx, self.my, self.width, self.height)
        w.SetContent(self.Message)



        feedback_type = "Message"
        feedback_colour = "white"

        if 200 <= self.ErrorCode < 300:
            feedback_type = "Success"
            feedback_colour = "green"

        if 300 <= self.ErrorCode < 400:
            feedback_type = "Partial Success"
            feedback_colour = "yellow"

        if 400 <= self.ErrorCode < 500:
            feedback_type = "User Fault"
            feedback_colour = "red"
        
        if 500 <= self.ErrorCode < 600:
            feedback_type = "Program Fault"
            feedback_colour = "red"

        if 600 <= self.ErrorCode < 699:
            feedback_type = "Input Fault"
            feedback_colour = "red"

        if 700 <= self.ErrorCode < 800:
            feedback_type = "File Fault"
            feedback_colour = "magenta"
        if 800 <= self.ErrorCode < 900:
            feedback_type = "Package Fault"
            feedback_colour = "red"


        w.Format("b/{0}".format(feedback_colour))
        w.SetTitle('{0} / '.format(feedback_type) + str(self.ErrorCode))

        return w.Draw().__str__()

    def SetReference(self, reference):
        """
        Set a reference for the status delivery.

        ```python
        Frame = ui.Frame()
        status_window = error.StatusDialog(self.status_code)
        status_window.SetReference(self.reference)
        Frame.add(status_window)
        Frame.Draw()
        ```
        """
        if reference:
            self.reference = reference
            self.Message += f"\n\n Reference: {reference}"
        
        self.Draw()