import curses
from enum import Enum

class State(Enum):
    normal = 0
    inactive = 1
    focus = 2
    pushed = 3

class Button(object):
    _wpm = None     # Instance to wpm manager to autodraw element
    _window = None  # Button window
    _text = ""
    _state = State.normal
    _button_width = 0
    _button_height = 0
    _button_x0 = 0
    _button_y0 = 0

    """
    Initialize Button
    """
    @classmethod
    def __init__(self, wpm, text="Ok"):
        self._wpm = wpm
        self._text = text
        self._state = State.focus
        self._button_width = 9
        self._button_height = 3
        self._button_x0 = 1
        self._button_y0 = 1
        self._window = self._wpm.create_window(self._button_width, self._button_height, self._button_x0, self._button_y0)
        return None
    """
    Draw itself
    """
    def draw(self):
        #self._wpm.print_message("  %s  " % self._text)
        if self._state == State.normal:
            self._window.border()
            self._wpm.print_message_center(self._window, self._text, self._button_y0)
            self._window.refresh()
        if self._state == State.focus:
            self._window.border()
            self._wpm.print_message_center(self._window, self._text, self._button_y0, curses.A_REVERSE)
            self._window.refresh()
            # Use color pair?
        return None
