import locale

import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), 'elements'))

import curses

from element import Element

"""
This python 3 class will manager a widgets using curses for you,

To generate HTML documentation for this module issue the command:

    pydoc -w Wpm
"""

class Wpm(object):
    _screen = None              # Curses screen
    _widget_stack = []          # List with elements created. Internally is a stack.
    _base_window = None        # First window create. Background.
    _base_window_height = 0
    _base_window_width = 0
    _current_window = None      # Current widget object to render. Last element in widget stack. Can be changed manually. Restore last element with restore_stack.

    """
    Initialize class: Initialize CursesManager
    """

    def __init__(self, echo=False):
        print("Initializing widget python manager")

        # Set UTF-8
        locale.setlocale(locale.LC_ALL, '')
        #code = locale.getpreferredencoding()

        # Initialize screen
        self.initializeScreen()
        return None

    # Catch any weird termination situations
    def __del__(self):
        self.restoreScreen()
        # Deactive control
        #self._base_window.keypad(True)
        return None

    """
    Diagnose terminal and print info. Static, you can use githout instance.
    Give all info about curses and you terminal. Use it at the beginning to test.

    :return: returns nothing
    """
    @staticmethod
    def diagnose():
        window = curses.initscr()
        window.addstr("\n  Userful info:")
        window.addstr("\n  Terminal: %s" % curses.longname())
        window.addstr("\n  Can use color: %s" % curses.has_colors())
        if curses.has_colors():
            window.addstr("\n  Can change colors: %s" % curses.can_change_color())
            window.addstr("\n  Terminal has %s colors" % curses.COLORS)
            window.addstr("\n  Terminal has %s pairs of colors" % curses.COLOR_PAIRS)
        window.addstr("\n  Number of lines: %s (y size) " % curses.LINES)
        window.addstr("\n  Number of cols: %s (x size)" % curses.COLS)

        window.border()
        window.getkey()
        curses.endwin()
        return None

    """
    Manage screen: Initialize terminal to be used appropitly

    :return: returns None
    """

    def initializeScreen(self):
        self._screen = curses.initscr()
        self._base_window_height, self._base_window_width = self._screen.getmaxyx()
        self._base_window = Element(self._base_window_width, self._base_window_height, 0, 0)
        self.push_widget(self._base_window)

        # Initialize cursor
        curses.curs_set(0)  # Invisible

        # Configure colors
        curses.start_color()
        curses.use_default_colors()

        # Custom colors

        # Active control
        #self._base_window.keypad(True)
        return None

    """
    Manage screen: Restore normal terminal behavior

    :return: returns None
    """

    def restoreScreen(self):
        #curses.initscr()
        curses.nocbreak()
        curses.echo()
        curses.endwin()
        return None

    """
    Manage stack: Add a new window or widget into stack.

    :return: returns None
    """

    def push_widget(self, widget):
        self._widget_stack.append(widget)
        self.restore_stack()
        return None

    """
    Manage stack: Restore as current window last element in stack.

    :return: returns None
    """

    def restore_stack(self):
        self._current_window = self._widget_stack[len(self._widget_stack)-1]
        return None

    """
    Manage stack: Restore as current window last element in stack.

    :return: returns None
    """

    def size_stack(self, echo = False):
        size = len(self._widget_stack)
        if echo:
            self.print_message(self.get_current_widget(), "You have %d widgets in the stack" % size)
        return size

    """
    Getters: Get background window

    :return: returns None
    """

    def get_background(self):
        return self._base_window

    """
    Getters: Get size current window

    :return: returns None
    """

    def get_window_size(self):
        if self._current_window != None:
            height, width = self._current_window.getmaxyx()
        return width, height

    """
    Getters: Get number of custom colors

    :return: returns None
    """

    def get_max_custom_colors(self):
        return curses.COLORS

    """
    Getters: Get current color pair. Internally is stored into curses color pair 7. To set a color user set_color function.

    :return: returns None
    """

    def get_current_color(self):
        return curses.color_pair(7)

    """
    Getter stack element: Return current stack element.

    :return: returns None
    """

    def get_current_widget(self):
        widget = self._widget_stack[len(self._widget_stack)-1]
        return widget

    """
    Manage terminal color: Set a character color and background color.

    :return: returns None
    """

    def set_color(self, color_character, color_background):
        curses.init_pair(7, color_character, color_background);
        return None

    """
    Refresh screen and wait time in milliseconds.

    :return: returns None
    """

    def msleep(self, ms = 1):
        curses.napms(ms)
        return None

    """
    Create button element. *TODO* Need create????

    :return: returns nothing
    """

    def create_element_button(self, message, width, x0, y0):
        button = Button(self, message, width, x0, y0)
        return button

    """
    Create a popup into current widget

    :return: returns nothing
    """

    def create_popup_message(self):
        print("create_popup_message")
        return None
