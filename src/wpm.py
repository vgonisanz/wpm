import curses
import locale

from element_button import Button

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
    @classmethod
    def __init__(self, echo=False):
        print("Initializing widget python manager")

        # Set UTF-8
        locale.setlocale(locale.LC_ALL, '')
        #code = locale.getpreferredencoding()

        # Initialize screen
        self._screen = curses.initscr()
        self._base_window_height, self._base_window_width = self._screen.getmaxyx()
        self._base_window = self.create_window(self._base_window_width, self._base_window_height, 0, 0)
        self.push_widget(self._base_window)

        # Initialize cursor
        curses.curs_set(0)  # Invisible

        # Configure colors
        curses.start_color()
        curses.use_default_colors()

        # Custom colors
        return

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
    Manage stack: Add a new window or widget into stack.

    :return: returns None
    """
    @classmethod
    def push_widget(self, widget):
        self._widget_stack.append(widget)
        self.restore_stack()
        return None

    """
    Manage stack: Restore as current window last element in stack.

    :return: returns None
    """
    @classmethod
    def restore_stack(self):
        self._current_window = self._widget_stack[len(self._widget_stack)-1]
        return None

    """
    Manage stack: Restore as current window last element in stack.

    :return: returns None
    """
    @classmethod
    def size_stack(self, echo = False):
        size = len(self._widget_stack)
        if echo:
            self.print_message(self.get_current_widget(), "You have %d widgets in the stack" % size)
        return size


    """
    Getters: Get size current window

    :return: returns None
    """
    @classmethod
    def get_window_size(self):
        if self._current_window != None:
            height, width = self._current_window.getmaxyx()
        return width, height

    """
    Getters: Get number of custom colors

    :return: returns None
    """
    @classmethod
    def get_max_custom_colors(self):
        return curses.COLORS

    """
    Getters: Get current color pair. Internally is stored into curses color pair 7. To set a color user set_color function.

    :return: returns None
    """
    @classmethod
    def get_current_color(self):
        return curses.color_pair(7)

    """
    Getter stack element: Return current stack element.

    :return: returns None
    """
    @classmethod
    def get_current_widget(self):
        widget = self._widget_stack[len(self._widget_stack)-1]
        return widget

    """
    Manage terminal color: Set a character color and background color.

    :return: returns None
    """
    @classmethod
    def set_color(self, color_character, color_background):
        curses.init_pair(7, color_character, color_background);
        return None
    """
    Manage cursor: Set cursor at position.

    :return: returns None
    """
    @classmethod
    def set_cursor(self, window, x0, y0):
        if window != None:
            window.move(y0, x0)
        return None

    """
    Clear line y.

    :return: returns None
    """
    @classmethod
    def clearln(self, window, y0):
        if window != None:
            window.move(y0, 0)
            window.clrtoeol()
            window.refresh()
        return None

    """
    Clear current window.

    :return: returns nothing
    """
    @classmethod
    def clear(self, window):
        if window != None:
            window.clear()
            window.refresh()
        return None

    """
    Refresh screen and wait time in milliseconds.

    :return: returns None
    """
    @classmethod
    def msleep(self, ms = 1):
        curses.napms(ms)
        return None

    """
    Refresh screen and wait time in milliseconds.

    :return: returns None
    """
    @classmethod
    def rwait(self, ms = 1):
        if self._current_window != None:
            self._current_window.refresh()
        curses.napms(ms)
        return None

    """
    Wait for key. TODO remove?

    :return: returns None
    """
    @classmethod
    def waitforkey(self, window, print_text = True, x0 = -1, y0 = -1):
        if window != None:
            self.rwait(1)
            if x0 > -1 and y0 > -1:
                self.set_cursor(window, x0, y0)
            if print_text:
                self.print_message(self.get_current_widget(), "\n Press any key to continue.")
            return window.getkey()
        return None

    """
    Print a message string into a window. Choose a position. This affect to cursor.

    :return: returns nothing
    """
    @classmethod
    def print_message(self, window, message, x0 = -1, y0 = -1, attributes = curses.A_NORMAL):
        if window != None:
            if x0 > -1 and y0 > -1:
                # Set cursor position
                window.move(y0, x0)
            # Print
            try:
                window.addstr(message, attributes)
            except curses.error:
                pass    # Allow to print last position
            # Refresh
            window.refresh()
        return None

    """
    Print a message string into a window. Choose y position, x automatically in the center. This affect to cursor.

    :return: returns nothing
    """
    @classmethod
    def print_message_center(self, window, message, y0, attributes = curses.A_NORMAL):
        if window != None:
            y_max, x_max = window.getmaxyx()
            lenght = len( message )
            indent = x_max - lenght
            indent = (int)(indent / 2)
            y0_int = (int)(y0)

            # Set attributes
            window.attrset(attributes)
            # Set cursor
            self.set_cursor(window, indent, y0_int)
            # Print
            window.addstr(message)
            # Restore attributes
            window.attroff(attributes)
        return None
    """
    Print background with color.

    :return: returns nothing
    """
    @classmethod
    def print_background(self, window, color_character, color_background):
        if window != None:
            # Set color
            self.set_color(color_character, color_background)
            # Draw background
            window.bkgd(self.get_current_color());
            self.msleep(1)
            window.refresh()
        return None
    """
    Create a curses window

    :return: returns window
    """
    @classmethod
    def create_window(self, width, height, x0 = 0, y0 = 0):
        window = curses.newwin(height, width, y0, x0)
        #self.print_background(window, 1, 2) # Truqui to check window
        return window

    """
    Create button element

    :return: returns nothing
    """
    @classmethod
    def create_element_button(self, message, width, x0, y0):
        button = Button(self, message, width, x0, y0)
        return button

    """
    Create a popup into current widget

    :return: returns nothing
    """
    @classmethod
    def create_popup_message(self):
        print("create_popup_message")
        return None
