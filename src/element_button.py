import curses
from enum import Enum

class ButtonState(Enum):
    normal = 0
    inactive = 1
    focus = 2
    pushed = 3

class Button(object):
    _wpm = None     # Instance to wpm manager to autodraw element
    _window = None  # Button window
    _text = ""
    _state = ButtonState.normal
    _button_width = 0
    _button_height = 0
    _button_x0 = 0
    _button_y0 = 0

    """
    Initialize Button
    """
    @classmethod
    def __init__(self, wpm, text="Ok", width = 10, x0 = 0, y0 = 0):
        self._wpm = wpm

        # Size variables
        self._button_width = width
        self._button_height = 1
        self._button_x0 = x0
        self._button_y0 = y0

        # Text and status
        self._text = text[:self._button_width-2]
        self._state = ButtonState.normal

        # Create container
        self._window = self._wpm.create_window(self._button_width, self._button_height, self._button_x0, self._button_y0)
        return None
    """
    Draw itself
    """
    def draw(self):
        # Put text cropped and centered
        # text_list = list()  # Crop size if needed
        len_text = len(self._text)
        start_position = 1
        if len_text > 0:
            start_position = int( ( self._button_width - len_text) / 2)

        self._wpm.print_message(self._window, ">", 0, 0)
        self._wpm.print_message(self._window, self._text, start_position, 0)
        self._wpm.print_message(self._window, "<", self._button_width - 1, 0)
        self._wpm.print_background(self._window, 0, 5)
        return None
