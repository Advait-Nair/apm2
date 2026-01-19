class UnicodeElements:
    def __init__(self):

        # BOX #

        self.box_tl = '╭'
        self.box_tr = '╮'
        self.box_bl = '╰'
        self.box_br = '╯'
    
        self.box_horiz = '─'
        self.box_vert = '│'
        self.box_junc_center_down = '┬'
        self.box_junc_center_up = '┴'
        self.box_junc_center_left = '┤'
        self.box_junc_center_right = '├'

        self.box_junc_4way = '┼'
    
        # STATE #

        self.state_on = '◉'
        self.state_off = '◯'
        self.state_disabled = '⬚'
        self.state_enabled = '✓'
        self.state_warning = '⚠'
        self.state_error = '𐄂'


        # FULFILLMENT #

        self.loading_f1 = '▚'
        self.loading_f2 = '▞'

        self.bar_unit_full = '█'
        self.bar_unit_3quarter = '▊'
        self.bar_unit_half = '▌'
        self.bar_unit_quarter = '▍'

        self.bar_unit_empty = '░'

        # ARROWS #

        self.arrow_up = '↑'
        self.arrow_down = '↓'
        self.arrow_left = '←'
        self.arrow_right = '→'

        self.arrow_up_right = '↗'
        self.arrow_up_left = '↖'
        self.arrow_down_right = '↘'
        self.arrow_down_left = '↙'

        # MATHEMATICAL #

        self.math_plus = '+'
        self.math_minus = '-'
        self.math_times = '×'
        self.math_divide = '÷'

        self.math_equals = '='
        self.math_not_equals = '≠'
        self.math_approx_equals = '≈'

        self.math_less_than = '<'
        self.math_greater_than = '>'
        self.math_less_than_equals = '≤'
        self.math_greater_than_equals = '≥'

        self.math_and = '∧'
        self.math_or = '∨'
        self.math_not = '¬'

        self.math_for_all = '∀'
        self.math_there_exists = '∃'

        self.math_integral = '∫'
        self.math_derivative = '∂'

        self.math_summation = '∑'
        self.math_product = '∏'

        self.math_infinity = '∞'

        # GREEK #

        self.greek_alpha = 'α'
        self.greek_beta = 'β'
        self.greek_gamma = 'γ'
        self.greek_delta = 'δ'
        self.greek_epsilon = 'ε'
        self.greek_zeta = 'ζ'
        self.greek_eta = 'η'
        self.greek_theta = 'θ'
        self.greek_iota = 'ι'
        self.greek_kappa = 'κ'
        self.greek_lambda = 'λ'
        self.greek_mu = 'μ'
        self.greek_nu = 'ν'
        self.greek_xi = 'ξ'
        self.greek_omicron = 'ο'
        self.greek_pi = 'π'
        self.greek_rho = 'ρ'
        self.greek_sigma = 'σ'
        self.greek_tau = 'τ'
        self.greek_upsilon = 'υ'
        self.greek_phi = 'φ'
        self.greek_chi = 'χ'
        self.greek_psi = 'ψ'
        self.greek_omega = 'ω'

        # MISC #

        self.misc_heart = '❤'
        self.misc_star = '★'
        self.misc_arrow = '➤'
        self.misc_check = '✔'
        self.misc_cross = '✘'
        self.misc_lightning = '⚡'
        self.misc_sun = '☀'
        self.misc_cloud = '☁'
        self.misc_snowflake = '❄'
        self.misc_umbrella = '☂'
        self.misc_snowman = '☃'
        self.misc_comet = '☄'
        self.misc_music_note = '♫'

from ..text import Text
import re


class Element:
    def __init__(self):
        self.Content = ""
        self.Embodiment = self.Draw()

    def SetContent(self, Content):
        self.Content = Content
        self.Embodiment = self.Draw()

    def GetContent(self):
        return self.Content
    
    def ClearContent(self):
        self.Content = ""
        self.Embodiment = self.Draw()

    def Draw(self):
        return ""
    
    def Output(self):
        self.Draw()
        print(self.Embodiment)

    def __str__(self):
        return self.Embodiment

def removeANSI(string):
    removed = re.sub(r'\x1b[^m]*m', '', string)
    return removed

class Window (Element):
    def __init__(self, px=2, py=2, mx=2, my=2, width=20, height=10):
        self.px = px
        self.py = py
        self.width = width
        self.height = height
        self.mx = mx
        self.my = my
        self.title = None
        super().__init__()

    def SetTitle(self, title):
        """
        Set the title of the window.

        ```python
        w = Window(px=2, py=2, mx=2, my=2, width=50, height=10)
        w.SetTitle("Hello, World!")
        print(w)
        """
        self.title = title
        self.Embodiment = self.Draw()
    
    def ClearTitle(self):
        """
        Clear the title of the window.
        """
        self.title = None
        self.Embodiment = self.Draw()
    
    def SetParams(self, px, py, mx, my, width, height=10):
        """
        Set or replace the parameters of the window.

        ```python
        w = Window(px=2, py=2, mx=2, my=2, width=50, height=10)
        print(w)
        w.SetParams(1, 1, 1, 1, 50, 10)
        print(w)
        ```
        """
        self.px = px
        self.py = py
        self.width = width
        self.height = height
        self.mx = mx
        self.my = my
        self.Embodiment = self.Draw()

    def Format(self, formatString):
        self.formatString = formatString
        self.Embodiment = self.Draw()

    def Draw(self):
        """
        Draw the window.

        ```python
        w = Window(px=2, py=2, mx=2, my=2, width=50, height=10)
        w.SetContent("Hello, World!")
        print(w)
        windowString = w.__str__()

        # to stdout
        w.Output()
        ```
        """
        wsp = " "
        mx = self.mx
        my = self.my
        px = self.px
        py = self.py

        window_roof = wsp*mx + UnicodeElements().box_tl + UnicodeElements().box_horiz * self.width + UnicodeElements().box_tr + wsp*mx
        window_floor = wsp*mx + UnicodeElements().box_bl + UnicodeElements().box_horiz * self.width + UnicodeElements().box_br + wsp*mx

        line = wsp*mx + UnicodeElements().box_vert + wsp*(self.width) + UnicodeElements().box_vert + wsp*mx

        maxLineLen = (self.width) - px*2

        def asLine (content, _r=True):
            pcontent = content
            pcontent = ''.join(content.split("\n"))
            # remove leading/trailing whitespace
            pcontent = pcontent.strip()
            # if last character is not whitespace, add -
            # negator = 0
            # if pcontent.__len__() > 0 and pcontent[-1] != " " and pcontent[-1] != "-" and pcontent[-1] != '':
            #     pcontent += "-"
            #     negator = 1
            ANSILength = len(content) - len(removeANSI(content))
            f = line.replace(wsp*(maxLineLen+px*2), px*wsp + pcontent.ljust(maxLineLen + (ANSILength)) + px*wsp)
            # print(1,f,1)
            return f

        # Separate lines for wrapping, every maxLineLen characters

        content = self.Content.__str__()
        contentLen = (content).__len__()
        lines = [content[i:i+maxLineLen] for i in range(0, contentLen, maxLineLen)]
        # print(lines)
        drawn = ""
        if self.title != None:
            title = self.title
            title = title.center(maxLineLen)
            divider = UnicodeElements().box_junc_center_right + UnicodeElements().box_horiz * (self.width) + UnicodeElements().box_junc_center_left
            drawn = "\n"*(my//2) + window_roof + "\n" + (asLine(title)+'\n')*(py//2) + wsp*mx + divider + "\n" + (asLine('')+'\n')*(py//2) + "\n".join([asLine(line) for line in lines]) + "\n" + (asLine('')+'\n')*(py//2) + window_floor + "\n"*(my//2)
        else:
            drawn = "\n"*(my//2) + window_roof + "\n" + (asLine('')+'\n')*(py//2) + "\n".join([asLine(line) for line in lines]) + "\n" + (asLine('')+'\n')*(py//2) + window_floor + "\n"*(my//2)

        if hasattr(self, 'formatString'):
            return Text(drawn, self.formatString)
        else:
            return drawn

        