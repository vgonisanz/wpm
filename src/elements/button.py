import curses   # TODO remove for my colors or color pairs.
from element import Element

from enum import Enum

class ButtonState(Enum):
    normal = 0
    inactive = 1
    focused = 2
    pushed = 3

class Button(Element):
    def __init__(self, text, width, x0, y0):
        # Initialize all variables
        self._title = ""
        self._state = ButtonState.normal
        self._on_push_callback = None

        # Assign
        super(Button, self).__init__(width, 1, x0, y0) # Initialize variables in Element, Override height
        self._text = text[:self._width-2]
        return None

    """
    Set a callback to call when button is pushed

    return: True always
    """

    def set_on_push_callback(self, callback):
        self._on_push_callback = callback
        return True

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
            success = False
        else:
            self._state = ButtonState.focused
        return success

    """
    Push button

    return: True always
    """

    def push(self, ms = 300):
        success = True
        if not self._state == ButtonState.inactive:
            self._state = ButtonState.pushed
            self.draw()
            curses.napms(ms)
            self._state = ButtonState.normal
            self.draw()
            self._on_push_callback()
        else:
            success = False
        return None

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

        attributes = curses.A_NORMAL

        # Calculate attributes
        if self._state == ButtonState.pushed:
            attributes = curses.A_REVERSE
        elif self._state == ButtonState.focused:
            attributes = curses.A_UNDERLINE
        elif self._state == ButtonState.inactive:
            attributes = curses.A_DIM

        # Print it
        self.window.clear() # Need clear before redraw
        self.window.bkgd(attributes)
        self.print_message(">", 0, 0, attributes)
        self.print_message(self._text, start_position, 0, attributes)
        self.print_message("<", self._width - 1, 0, attributes)
        return None
