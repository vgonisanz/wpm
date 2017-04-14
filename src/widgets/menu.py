#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'structs'))

import curses   # TODO remove for my colors or color pairs.
from widget import Widget
from eventobject import EventObject
from childelement import ChildElement
from optionstruct import OptionStruct

"""
Simple menu widget.
Usage: menu = MenuCM(width, height, x0, y0, title, options, instructions)
"""
class Menu(Widget):
    """
    Initialize Menu
    """

    def __init__(self, width, height, x0, y0, title, instructions = "", title_padding = 1, instruction_padding = 1):
        # Initialize all variables
        self._title = None
        self._option_selected = 0
        #self._instructions = None
        self._title_padding = 1
        #self._instruction_padding = 1
        self._centered = False           # If true menu options will be centered.

        super(Menu, self).__init__(width, height, x0, y0) # Initialize variables in Element, Override height

        # Assign
        self._title = title
        #self._instructions = instructions
        self._title_padding = title_padding
        #self._instruction_padding = instruction_padding

        # Quit event
        event_quit = EventObject(ord('q'), self.callback_quit)
        event_quit.description = "Press <q> to quit"
        self.add_event(event_quit)

        # Create event enter with ENTER
        event_enter = EventObject(10, self.callback_enter) # Shall be curses.KEY_ENTER = 10
        event_enter.description = "Press <ENTER> to select"
        self.add_event(event_enter)

        # Add arrow controls
        event_up = EventObject(curses.KEY_UP, self.callback_up)
        event_up.description = "Press <UP> to go up"
        event_down = EventObject(curses.KEY_DOWN, self.callback_down)
        event_down.description = "Press <DOWN> to go down"
        self.add_event(event_up)
        self.add_event(event_down)
        return None

    def callback_quit(self):
        self.end_condition()
        return None

    def callback_enter(self):
        option = self._options[self._option_selected]
        if not option.action == None:
            if not option.args == None:
                option.action(option.args)
            else:
                option.action()
        self.draw()
        return None

    def callback_up(self):
        self._option_selected = self._option_selected - 1
        self.draw()
        return None

    def callback_down(self):
        self._option_selected = self._option_selected + 1
        self.draw()
        return None

    """
    Set variable to set draw options centered

    :return: None
    """

    def set_centered(self, value):
        self._centered = value
        return None

    """
    Print menu and wait response.

    :return: returns -1 if enter with q or ESC, option id from [0, N-1] if ENTER
    """

    def run(self):
        self.foreground.clear()
        self._option_selected = 0

        # Refresh menu
        self.draw() # TODO needed?
        super(Menu, self).run()    # Widget autoiterate events
        return self._option_selected

    """
    Clear menu window.

    :return: None
    """

    def clear(self):
        self.foreground.clear()
        return None

    """
    Draw menu options. Private, autoinvoked. Note: Is possible to optimize draw with only changed sections, maybe someday.

    :return: returns option selected
    """

    def draw(self):
        if len(self._options) == 0:
            return -1
        if self._option_selected < 0:
            self._option_selected = 0
        if self._option_selected >= len(self._options):
            self._option_selected = len(self._options) - 1

        self.background.clear()

        if self._centered:
            self._redraw_center()
        else:
            self._redraw_normal()
            
        self.foreground.window.refresh()
        return self._option_selected

    def _redraw_normal(self):
        counter = 0
        self.foreground.print_message(self._title, 0, 0, curses.A_UNDERLINE)
        for option in self._options:
            if self._option_selected == counter:
                self.foreground.print_message(option.text, 0, counter + 0 + self._title_padding + 1, curses.A_REVERSE)
            else:
                self.foreground.print_message(option.text, 0, counter + 0 + self._title_padding + 1)
            counter = counter + 1
        #self.foreground.print_message(self._instructions, 0, counter + 0 + self._title_padding + self._instruction_padding + 1)
        return None

    def _redraw_center(self):
        counter = 0
        self.foreground.print_message_center(self._title, 0, curses.A_UNDERLINE)
        for option in self._options:
            if self._option_selected == counter:
                self.foreground.print_message_center(option.text, counter + 0 + self._title_padding + 1, curses.A_REVERSE)
            else:
                self.foreground.print_message_center(option.text, counter + 0 + self._title_padding + 1)
            counter = counter + 1
        #self.foreground.print_message(self._instructions, 0, counter + 0 + self._title_padding + self._instruction_padding)
        return None
