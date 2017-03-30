import curses   # TODO remove for my colors or color pairs.
from element import Element

from enum import Enum

class ButtonState(Enum):
    normal = 0
    inactive = 1
    focused = 2
    pushed = 3

class Button(Element):
    _title = ""
    _state = ButtonState.normal


    def __init__(self, text, width, x0, y0):
        super(Button, self).__init__(width, 1, x0, y0) # Initialize variables in Element, Override height
        self._text = text[:self._width-2]
        return None

    """
    Force to ser normal or inactive a button

    return: True always
    """

    def set_active(self, active):
        if active:
            self._state = ButtonState.normal
        else:
            self._state = ButtonState.inactive
        return True

    """
    Set button on focus mode if is not inactive

    return: True always
    """

    def set_focus(self):
        success = True
        if self._state == ButtonState.inactive:
            sucess = False
        else:
            self._state = ButtonState.focused
        return success

    """
    Draw button in its position with its state

    return: None
    """

    def draw(self):

        # Put text cropped and centered
        len_text = len(self._text)
        start_position = 1
        if len_text > 0:
            start_position = int( ( self._width - len_text) / 2)

        attributes = curses.A_DIM

        # Calculate attributes
        if self._state == ButtonState.pushed:
            attributes = curses.A_BLINK
        elif self._state == ButtonState.focused:
            attributes = curses.A_REVERSE
        elif self._state == ButtonState.inactive:
            attributes = curses.A_UNDERLINE

        # Print it
        self.window.clear() # Need clear before redraw
        self.window.bkgd(attributes)
        self.print_message(">", 0, 0, attributes)
        self.print_message(self._text, start_position, 0, attributes)
        self.print_message("<", self._width - 1, 0, attributes)
        return None
