import curses   # TODO remove for my colors or color pairs.
from element import Element

from enum import Enum

class ButtonState(Enum):
    normal = 0
    inactive = 1
    focus = 2
    pushed = 3

class Button(Element):
    _title = ""

    @classmethod
    def __init__(self, text, width, x0, y0):
        super(Button, self).__init__(width, 1, x0, y0) # Initialize variables in Element, Override height
        self._text = text[:self._width-2]
        self._state = ButtonState.normal
        return None

    @classmethod
    def draw(self):
        # Put text cropped and centered
        len_text = len(self._text)
        start_position = 1
        if len_text > 0:
            start_position = int( ( self._width - len_text) / 2)

        attributes = curses.A_NORMAL

        # Calculate attributes
        if self._state == ButtonState.pushed:
            attributes = curses.A_REVERSE
        elif self._state == ButtonState.focus:
            attributes = curses.A_UNDERLINE

        # Print it
        self.print_message(">", 0, 0)
        self.print_message(self._text, start_position, 0)
        self.print_message("<", self._width - 1, 0)
        return None
