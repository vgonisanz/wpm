import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '.', 'elements'))

import curses               # Todo remove chaning own variables
from curses import wrapper  # Use my own wrapper

from wpm import Wpm
from element import Element

class EventObject(object):
    character = None
    action = None
    args = []

    def __init__(self, character_input, action_input, args_input = None):
        # check type() is type
        self.character = character_input
        self.action = action_input
        self.args = args_input
        return None

class ChildElement(object):
    cid = ""
    celement = None

    def __init__(self, child_id, child_element):
        self.cid = child_id
        self.celement = child_element
        return None

"""
Functionality
"""
class Widget(object):

    _end_condition = False
    _background = None
    _events = []        # List with trigger and action
    _children = []      # List with children elements


    def __init__(self, width, height, x0, y0):
        self._background = Element(width, height, x0, y0)
        self._background.change_color(curses.COLOR_BLACK, curses.COLOR_WHITE) # Test
        return None

    """
    This private method iterate events while not end condition.

    :return: returns nothing
    """

    def _iterate_events(self):
        self._background.set_input_mode(True)
        self._end_condition = False
        while not self._end_condition:
            event = self._background.get_character()
            for member in self._events:
                if event == member.character:
                    if not member.args == None:
                        member.action(*member.args)
                    else:
                        member.action()
        self._background.set_input_mode(False)
        return None

    """
    Add a new children element.
    :input element
    :return: returns nothing
    """

    def add_child(self, element):
        self._children.append(element)
        return None

    """
    Add a new event. You must send a action object.
    :input action_object
    :return: returns nothing
    """

    def add_event(self, action_object):
        self._events.append(action_object)
        return None

    """
    Set end condition true.

    :return: returns nothing
    """
    def end_condition(self):
        self._end_condition = True
        return None

    """
    get background

    :return: returns nothing
    """
    def get_background(self):
        return self._background

    """
    This widget take the control of the UI.

    :return: returns nothing
    """
    def run(self):
        self._iterate_events()
        return None

    """
    Remove all events added of predefined.

    :return: returns nothing
    """

    def purge_events(self):
        self._events = []
        return None

    """
    Remove all children added.

    :return: returns nothing
    """

    def purge_children(self):
        self._children = []
        return None
