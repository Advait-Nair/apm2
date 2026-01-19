from ..ui import status
from .. import ui
from . import coding

class Feedback:
    """
    Create a standardised Feedback Object from the provided FeedbackCode.
    Allows a range of functions to be used, such as throwing the feedback.
    """
    def __init__(self, status_code):
        self.status_code = status_code
        self.reference = None
        self.message = coding.StatusAsMessage(status_code)
        
    def __str__(self):
        return self.message
    
    def SetReference(self, reference):
        """
        Set a reference for the feedback.

        ```python
        feedback = Feedback(StatusCodes().bad_request)
        feedback.SetReference('main.py/line:10')
        feedback.Throw()
        ```
        """
        self.reference = reference
    
    def Throw(self):
        """
        Throws the feedback using an StatusDialog.
        """
        Frame = ui.Frame()
        status_window = status.StatusDialog(self.status_code)
        status_window.SetReference(self.reference)
        Frame.add(status_window)
        Frame.Draw()