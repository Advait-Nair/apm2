"""
Provide text utilities for UI.
Bold, Italic, Underline, Strike, and Colour are provided.
"""

class Format:
    """
    ANSI Codes for text formatting.
    """
    def __init__(self):
        self.BOLD = "\033[1m"
        self.ITALIC = "\033[3m"
        self.UNDERLINE = "\033[4m"
        self.STRIKE = "\033[9m"
        self.RESET = "\033[0m"
        self.BLACK = "\033[30m"
        self.RED = "\033[31m"
        self.GREEN = "\033[32m"
        self.YELLOW = "\033[33m"
        self.BLUE = "\033[34m"
        self.MAGENTA = "\033[35m"
        self.CYAN = "\033[36m"
        self.WHITE = "\033[37m"
        self.BRIGHT_BLACK = "\033[90m"
        self.BRIGHT_RED = "\033[91m"
        self.BRIGHT_GREEN = "\033[92m"
        self.BRIGHT_YELLOW = "\033[93m"
        self.BRIGHT_BLUE = "\033[94m"
        self.BRIGHT_MAGENTA = "\033[95m"
        self.BRIGHT_CYAN = "\033[96m"
        self.BRIGHT_WHITE = "\033[97m"
        self.BG_BLACK = "\033[40m"
        self.BG_RED = "\033[41m"
        self.BG_GREEN = "\033[42m"
        self.BG_YELLOW = "\033[43m"
        self.BG_BLUE = "\033[44m"
        self.BG_MAGENTA = "\033[45m"
        self.BG_CYAN = "\033[46m"
        self.BG_WHITE = "\033[47m"
        self.BG_BRIGHT_BLACK = "\033[100m"
        self.BG_BRIGHT_RED = "\033[101m"
        self.BG_BRIGHT_GREEN = "\033[102m"
        self.BG_BRIGHT_YELLOW = "\033[103m"
        self.BG_BRIGHT_BLUE = "\033[104m"
        self.BG_BRIGHT_MAGENTA = "\033[105m"
        self.BG_BRIGHT_CYAN = "\033[106m"
        self.BG_BRIGHT_WHITE = "\033[107m"

    def stringAsCode(self, string):
        """
        Return the ANSI code for a given string.
        """
        return getattr(self, string.upper())

def bold(text):
    """
    Bold the argument string with an ANSI code.

    ```python
    bold_text = bold("Hello, World!")
    print(bold_text)
    ```
    """
    return Format().BOLD + text + Format().RESET

def italic(text):
    """
    Italicise the argument string with an ANSI code.

    ```python
    italic_text = italic("Hello, World!")
    print(italic_text)
    ```
    """
    return Format().ITALIC + text + Format().RESET

def underline(text):
    """
    Underline the argument string with an ANSI code.

    ```python
    underline_text = underline("Hello, World!")
    print(underline_text)
    ```
    """
    return Format().UNDERLINE + text + Format().RESET

def strike(text):
    """
    Strike the argument string with an ANSI code.

    ```python
    strike_text = strike("Hello, World!")
    print(strike_text)
    ```
    """
    return Format().STRIKE + text + Format().RESET

def colour(text, colour):
    """
    Colour the argument string with an ANSI code.

    ```python
    red_text = colour("Hello, World!", Format().RED)
    print(red_text)
    ```
    """
    return colour + text + Format().RESET

import re

class Text:
    """
    Text formatting utilities.
    ```python
        text = "Hello, World!"
        format_string = "biu/red"
        formatted_text = Text(text, format_string)
        print(formatted_text)
    ```
    """
    def __init__(self, raw_text, formatString):
        self.bold = bold
        self.italic = italic
        self.underline = underline
        self.strike = strike
        self.colour = colour

        self.raw_text = raw_text
        self.formatString = formatString
        self.formatted_string = self.ParseFormatString()

    def __len__(self):
        return len(self.formatted_string)
    
    def __str__(self):
        return self.formatted_string
    
    def GetContent(self):
        return self.formatted_string
    
    def AutoColour(raw_text):
        """
        Automatically colour text based on format patterns in the text.

        ```python
        text = "Hello, b/blue(World)!"
        """

        # Find pattern matches such as the right using regex: c/colour(text)
        matches = re.findall(r'(\w+\/\w+\(.*?\))', raw_text)

        buffer = raw_text

        for match in matches:
            # for each match, extrapolate the formatString and text. Do not consider escaped brackets.
            formatString = match.split("(")[0]
            interior_text = match.split("(")[1].split(")")[0]

            # Replace the match with the formatStringed text.

            processed = Text(interior_text, formatString).GetContent()

            buffer = buffer.replace(match, processed)

        
        return buffer


    
    def parseFontFormatting(self, format_string, raw_text):
        buffer = ""
        for char in format_string:
            if char.strip() == "b":
                buffer = bold(raw_text)
            if char.strip() == "i":
                buffer = italic(buffer)
            if char.strip() == "u":
                buffer = underline(buffer)
            if char.strip() == "s":
                buffer = strike(buffer)
        
        return buffer
    
    def ParseFormatString(self):
        """
        Parse a format string and return a formatted string.
        
        ```python
        text = "Hello, World!"
        format_string = "biu/red"
        formatted_text = Text(text, format_string)
        print(formatted_text)
        ```
        """

        format_string = self.formatString

        output = ""

        if "/" in format_string:
            font_formatting = format_string.split("/")[0]
            fcolour = format_string.split("/")[1]

            text = self.parseFontFormatting(font_formatting, self.raw_text)
            output = colour(text, Format().stringAsCode(fcolour))
        else:
            output = self.parseFontFormatting(format_string, self.raw_text)
        
        return output
    
import re

def RemoveFormatting(text):
    """
    Remove ANSI formatting from a string.
    """
    return re.sub(r'\033\[[0-9;]*m', '', text)