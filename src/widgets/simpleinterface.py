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
class SimpleInterface(Widget):
    """
    Initialize SimpleInterface
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

        super(SimpleInterface, self).__init__(width, height, x0, y0) # Initialize variables in Element, Override height

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
        super(SimpleInterface, self).add_event(event_object)

        # Also calculate delimiter position updated!
        self._event_delimiter_line = self.foreground._height - len(self._events) - 1
        return None

    def get_secondary_widget_size(self):
        self._secondary_widget_x0 = 1
        self._secondary_widget_y0 = 1
        self._secondary_widget_width = self.foreground._width
        self._secondary_widget_height = self.foreground._height
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
        self.foreground.clear()

        # Refresh menu
        self.draw()
        super(SimpleInterface, self).run()    # Widget autoiterate events
        return None

    """
    Clear menu window.

    :return: None
    """

    def clear(self):
        self.foreground.clear()
        return None

    def clear_events(self):
        col = 0
        for index,event in enumerate(self._events):
            col = index + 1
            self.foreground.clearln(self.foreground._height - col)
        return None

    def draw_events(self):
        self.foreground.clear()
        
        # Print bottom options
        col = 0
        for index,event in enumerate(self._events):
            col = index + 1
            self.foreground.print_message(str(event.description), 0, self.foreground._height - col) # TODO change event.key for description

        # Reverse separator
        self.foreground.reverseln(self._event_delimiter_line)

        #self.foreground.window.refresh()
        return None

    """
    Draw SimpleInterface.

    :return: returns event selected
    """

    def draw(self):
        # Update background
        if self._print_title:
            self.background.print_message_center(self._title, 0)
        self.background.reverseln(0, False)
        self.background.reverseln(self.background._height - 1, False)
        self.background.window.refresh()

        # Update secondary widget
        if self._secondary_widget:
            self._secondary_widget.draw()

        # Update foreground

        self.draw_events()

        return None

    """
    Print command in reverse line

    :return: None
    """

    def print_command(self, message, x0 = 1):
        self.foreground.reverseln(self._event_delimiter_line, True)
        self.foreground.print_message(message, x0, self._event_delimiter_line, curses.A_REVERSE)
        return None
