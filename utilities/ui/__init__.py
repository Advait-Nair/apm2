class Frame:
    """
    A Frame is a container for elements. When the frame is displayed, all elements within it are displayed.
    The frame can be removed, replaced and refreshed, acting like a window. It can alternatively serve as a container for elements.
    """

    def __init__(self, elements=[]):
        self.elements = elements

    def add (self, element):
        """
        Add an element to the frame.
        """
        self.elements.append(element)

    def remove (self, element):
        """
        Remove an element from the frame.
        """
        self.elements.remove(element)
    
    def replace (self, element, replacement):
        """
        Replace an element in the frame with another element.
        """
        self.elements[self.elements.index(element)] = replacement
    
    def Draw(self):
        """
        Draw the frame and all elements within it, printing it to stdout
        """
        for element in self.elements:
            print(element.Draw())

