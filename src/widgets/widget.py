import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '.', 'elements'))

import curses               # Todo remove chaning own variables
from curses import wrapper  # Use my own wrapper

from wpm import Wpm
from element import Element

class ActionObject(object):
    character = None
    action = None

    @classmethod
    def __init__(self, character_input, action_input):
        # check type() is type
        self.character = character_input
        self.action = action_input
        return None
"""
Functionality
"""
class Widget(object):

    _end_condition = False
    _background = None
    _events = []    # List with trigger and action

    @classmethod
    def __init__(self, width, height, x0, y0):
        self._background = Element(width, height, x0, y0)
        return None

    """
    This private method iterate events while not end condition.

    :return: returns nothing
    """
    @classmethod
    def _iterate_events(self):
        self._background.change_color(curses.COLOR_BLACK, curses.COLOR_WHITE) # Test
        self._background.set_input_mode(True)
        self._end_condition = False
        while not self._end_condition:
            event = self._background.get_character()
            #self._background.print_message(str(len(self._events)))
            for member in self._events:
                self._background.print_message(str(member.character))
                self._background.print_message(" END ")
                #if event == member.character:
                #    self._background.print_message(str(event))
                #    self._background.print_message(str(member.character))
                #    self._background.print_message("si")
                #    self._background.print_message("SI")
                #else:
                #    self._background.print_message("NO")

                #if event == member.character:
                    #self._background.print_message(str(member.character))
                    #member.action()
        self._background.set_input_mode(False)
        return None

    """
    Add a new event. You must send a action object.
    :input action_object
    :return: returns nothing
    """
    @classmethod
    def add_event(self, action_object):
        self._events.append(action_object)
        return None

    """
    Set end condition true.

    :return: returns nothing
    """
    @classmethod
    def end_condition(self):
        self._end_condition = True
        return None

    """
    get background

    :return: returns nothing
    """
    @classmethod
    def get_background(self):
        return self._background

    """
    This widget take the control of the UI.

    :return: returns nothing
    """
    @classmethod
    def run(self):
        # Override me
        self._iterate_events()
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
