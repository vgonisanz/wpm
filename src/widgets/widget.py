import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '.', 'elements'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'structs'))

import curses               # Todo remove chaning own variables
from curses import wrapper  # Use my own wrapper

from wpm import Wpm
from element import Element
from eventobject import EventObject
from childelement import ChildElement

#from popup import Popup

"""
Functionality
"""
class Widget(object):

    def __init__(self, width, height, x0, y0, create_foreground = True, debug = False):
        # Initialize all variables
        self.background = None          # background element object with drawable window including border
        self.foreground = None          # Foreground element object with drawable window without border
        self._end_condition = False     # End bucle run checking events in _iterate_events function. Use end_condition function to set.
        self._events = []               # List with trigger and action with key callback
        self._options = []              # List with options to trigger and action if command
        self._children = []             # List with drawable children elements

        # Assign a drawable element
        self.background = Element(width, height, x0, y0)
        if create_foreground:
            self.foreground = Element(width - 2, height - 2, x0 + 1, y0 + 1)

        if debug:
            if create_foreground:
                self.foreground.change_color(curses.COLOR_BLACK, curses.COLOR_WHITE) # Test
        return None

    """
    This private method iterate events while not end condition.

    :return: returns nothing
    """

    def _iterate_events(self):
        self.background.set_input_mode(True)
        self._end_condition = False
        while not self._end_condition:
            event = self.background.get_character()
            for member in self._events:
                if event == member.key:
                    if not member.args == None:
                        member.action(*member.args)
                    else:
                        member.action()
        self.background.set_input_mode(False)
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
    Add a new option. You must send a option structs.
    :input action_object
    :return: returns nothing
    """
    def add_option(self, option_struct):
        self._options.append(option_struct)
        return None

    """
    Set end condition true.

    :return: returns nothing
    """
    def end_condition(self):
        self._end_condition = True
        return None

    """
    Get child by ID

    return: None
    """

    def get_child(self, child_id):
        child = None
        for member in self._children:
            if member.cid == child_id:
                return member.celement
        return child

    """
    get background

    :return: returns nothing
    """
    def get_background(self):
        return self.background

    """
    get foreground

    :return: returns nothing
    """
    def get_foreground(self):
        return self.foreground

    """
    Draw prototype, only border. Complete in children. TODO change for restore background.

    :return: returns nothing
    """
    def draw(self):
        self.background.print_border()
        return None

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


    """
    This private method iterate children and draw them.

    :return: returns nothing
    """

    def _draw_children(self):
        for child in self._children:
            #child.celement.clear()
            child.celement.draw()
            child.celement.window.refresh()
        return None
