# -*- coding: utf-8 -*-
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


class Widget(object):
    """Functionality to all group of elements. No draw functions here or in its children, just logic.
    * Background: Element with ALL size, usually to print border and shadow propertly.
    * Foreground: Element with inside background to print without border description.
    """
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

    def _iterate_events(self):
        """This private method iterate events while not end condition.
        :return: returns nothing
        """
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

    def _draw_children(self):
        """This private method iterate children and draw them.
        :return: returns nothing
        """
        for child in self._children:
            #child.celement.clear()
            child.celement.draw()
            child.celement.window.refresh()
        return None

    def add_child(self, element):
        """Add a new children element.
        :input element
        :return: returns nothing
        """
        self._children.append(element)
        return None

    def add_event(self, action_object):
        """Add a new event. You must send a action object.
        :input action_object
        :return: returns nothing
        """
        self._events.append(action_object)
        return None

    def add_option(self, option_struct):
        """Add a new option. You must send a option structs.
        :input action_object
        :return: returns nothing
        """
        self._options.append(option_struct)
        return None

    def end_condition(self):
        """Set end condition true.
        :return: returns nothing
        """
        self._end_condition = True
        return None

    def get_child(self, child_id):
        """Get child by ID
        return: None
        """
        child = None
        for member in self._children:
            if member.cid == child_id:
                return member.celement
        return child

    def get_background(self):
        """Get background
        :return: returns nothing
        """
        return self.background

    def get_foreground(self):
        """Get foreground
        :return: returns nothing
        """
        return self.foreground

    def run(self):
        """This widget take the control of the UI.
        :return: returns nothing
        """
        self._iterate_events()
        return None

    def purge_events(self):
        """Remove all events added of predefined.
        :return: returns nothing
        """
        self._events = []
        return None

    def purge_children(self):
        """Remove all children added.
        :return: returns nothing
        """
        self._children = []
        return None

    def store_widget(self):
        """Store all elements, background, foreground and children.
        :return: returns nothing
        """
        self.background.store_window()
        self.foreground.store_window()
        for child in self._children:
            child.celement.store_window()
        return None

    def restore_widget(self):
        """Restore all elements, background, foreground and children.
        :return: returns nothing
        """
        self.background.restore_window()
        self.foreground.restore_window()
        for child in self._children:
            child.celement.restore_window()
        return None
