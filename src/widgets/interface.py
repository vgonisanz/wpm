#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'structs'))
import logging

import curses   # TODO remove for my colors or color pairs.
from widget import Widget
from eventobject import EventObject
from childelement import ChildElement

"""
Simple interface widget.
Usage: ui = Interface(
"""
class Interface(Widget):
    """
    Initialize interface
    """

    def __init__(self, width, height, x0, y0, title, print_title):
        # Initialize all variables
        self.logger = None
        self._title = ""
        self._print_title = False
        self._secondary_widget = None
        self._event_delimiter_line = 0
        self._secondary_widget_x0 = 0
        self._secondary_widget_y0 = 0
        self._secondary_widget_width = 0
        self._secondary_widget_height = 0

        # Assign
        self.logger = logging.getLogger("wpm")
        self._title = title
        self._print_title = print_title

        super(Interface, self).__init__(width, height, x0, y0) # Initialize variables in Element, Override height

        # Quit event by default, you can purge it if you want.
        event_quit = EventObject(ord('q'), self.callback_quit)
        event_quit.description = "Press <q> to quit"
        self.add_event(event_quit)
        return None

    def callback_quit(self):
        self.end_condition()
        return None

    """
    :input Add a new widget event action_object
    :return: returns nothing
    """
    def add_event(self, event_object):
        # Parent add to events
        #super(Interface, self).add_event(event_object)
        self._events.append(event_object)
        # Also calculate delimiter position updated!
        self._event_delimiter_line = self.background._height - len(self._events) - 1 # background was y_max TODO remove comment
        for event in self._events:
            self.logger.debug("Delimiter is %s" % event.description)
        return None

    def get_secondary_widget_size(self):
        self._secondary_widget_x0 = 0
        self._secondary_widget_y0 = 1
        self._secondary_widget_width = self.background._width
        self._secondary_widget_height = self.background._height - len(self._events) - 3
        if not self._print_title:
            self._secondary_widget_y0 = 0
        return self._secondary_widget_width, self._secondary_widget_height, self._secondary_widget_x0, self._secondary_widget_y0

    def set_secondary_widget(self, widget):
        self._secondary_widget = widget
        return None

    """
    Print menu and wait response.

    :return: returns -1 if enter with q or ESC, event id from [0, N-1] if ENTER
    """

    def run(self):
        self.background.clear()
        #self.background.print_message("HIHIHI")
        #self.background.waitforkey()
        # Refresh menu
        self.draw()
        super(Interface, self).run()    # Widget autoiterate events
        return None

    """
    Clear menu window.

    :return: None
    """

    def clear(self):
        self.background.clear()
        return None

    """
    Draw interface.

    :return: returns event selected
    """

    def draw(self):
        if self._secondary_widget:
            self._secondary_widget.draw()

        # Print bottom options
        col = 0
        for index,event in enumerate(self._events):
            col = index + 1
            self.background.print_message(str(event.description), 0, self.background._height - col) # TODO change event.key for description

        # Reverse separator
        self.background.reverseln(self._event_delimiter_line)

        # Box secondary window
        #self._secondary_widget.border()
        #***
        # Print title if needed
        if self._print_title:
            self.background.print_message_center(self._title, 0)
            self.background.reverseln(0, False)
        return None
