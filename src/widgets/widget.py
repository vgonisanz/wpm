import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '.', 'elements'))

import curses               # Todo remove chaning own variables
from curses import wrapper  # Use my own wrapper

from wpm import Wpm
from element import Element

"""
Functionality
"""
class Widget(object):

    _end_condition = False
    _background = None

    @classmethod
    def __init__(self, width, height, x0, y0):
        self._background = Element(width, height, x0, y0)
        return None

    """
    This widget take the control of the UI.

    :return: returns nothing
    """
    @classmethod
    def run(self):
        # Override me
        return None

    """
    This widget take the control of the UI.

    :return: returns nothing
    """
    @classmethod
    def run_test(self):
        self._background.change_color(curses.COLOR_BLACK, curses.COLOR_WHITE) # Test
        self._background.set_input_mode(True)
        self._end_condition = False
        while not self._end_condition:
            event = self._background.get_character()
            if event == curses.KEY_LEFT:
                self._background.print_message("Left\n")
            if event == curses.KEY_RIGHT:
                self._background.print_message("Right\n")
            if event == curses.KEY_UP:
                self._background.print_message("Up\n")
            if event == curses.KEY_DOWN:
                self._background.print_message("Down\n")
            if event == curses.KEY_BACKSPACE:
                self._background.print_message("Backspace\n")
            if event == ord('q'):
                self._background.print_message("Quit command\n")
                curses.napms(300)
                self._end_condition = True
        self._background.set_input_mode(False)
        return None
