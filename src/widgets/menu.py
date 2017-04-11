#!/usr/bin/env python
# -*- coding: utf-8 -*-

import curses   # TODO remove for my colors or color pairs.
from widget import Widget
from widget import EventObject
from widget import ChildElement

"""
Simple menu widget. You can create nested menus with *TODO*
Usage: menu = MenuCM(width, height, x0, y0, title, options, instructions)
"""
class Menu(Widget):
    _title = None
    _options_size = 0
    _options = []
    _option_selected = 0
    _instructions = None
    _title_padding = 1
    _instruction_padding = 1
    _centered = False           # If true menu options will be centered.


    """
    Initialize MenuCM
    """

    def __init__(self, width, height, x0, y0, title, options, instructions = "", title_padding = 1, instruction_padding = 1):
        if len(options) <= 0:
            return None
        super(Menu, self).__init__(width, height, x0, y0) # Initialize variables in Element, Override height

        self._title = title
        self._option_size = len(options)
        self._options = options
        self._instructions = instructions
        self._title_padding = title_padding
        self._instruction_padding = instruction_padding

        # Create event enter with ENTER
        event_enter = EventObject(10, self.callback_enter) # Shall be curses.KEY_ENTER = 10
        self.add_event(event_enter)

        # Add arrow controls
        event_up = EventObject(curses.KEY_UP, self.callback_up)
        event_down = EventObject(curses.KEY_DOWN, self.callback_down)
        self.add_event(event_up)
        self.add_event(event_down)
        return None

    def callback_enter(self):
        self.end_condition()
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
    Option to set centered options

    :return: None
    """

    def set_centered(self, value):
        self._centered = True
        return None

    """
    Print menu and wait response.

    :return: returns -1 if enter with q or ESC, option id from [0, N-1] if ENTER
    """

    def run(self):
        self.background.clear()
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
        self.background.clear()
        return None

    """
    Draw menu options. Private, autoinvoked. Note: Is possible to optimize draw with only changed sections, maybe someday.

    :return: returns option selected
    """

    def draw(self):
        if self._option_selected < 0:
            self._option_selected = 0
        if self._option_selected >= self._option_size:
            self._option_selected = self._option_size - 1

        if self._centered:
            self._redraw_center()
        else:
            self._redraw_normal()
        return self._option_selected

    def _redraw_normal(self):
        counter = 0
        self.background.print_message(self._title, 0, 0, curses.A_UNDERLINE)
        for option in self._options:
            if self._option_selected == counter:
                self.background.print_message(option, 0, counter + 0 + self._title_padding + 1, curses.A_REVERSE)
            else:
                self.background.print_message_center(option, counter + 0 + self._title_padding + 1)
            counter = counter + 1
        self.background.print_message(self._instructions, 0, counter + 0 + self._title_padding + self._instruction_padding + 1)
        return None

    def _redraw_center(self):
        counter = 0
        self.background.print_message_center(self._title, 0, curses.A_UNDERLINE)
        for option in self._options:
            if self._option_selected == counter:
                self.background.print_message_center(option, counter + 0 + self._title_padding + 1, curses.A_REVERSE)
            else:
                self.background.print_message_center(option, counter + 0 + self._title_padding + 1)
            counter = counter + 1
        self.background.print_message(self._instructions, 0, counter + 0 + self._title_padding + self._instruction_padding + 1)
        return None
