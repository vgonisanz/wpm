import curses

class Element(object):

    _window = None
    _width = None
    _height = None
    _x = None
    _y = None

    @classmethod
    def __init__(self, width, height, x0, y0):
        self._width = width
        self._height = height
        self._x = x0
        self._y = y0
        self._window = curses.newwin(height, width, y0, x0)
        return None

    """
    Clear current window.

    :return: returns nothing
    """
    @classmethod
    def clear(self):
        if self._window != None:
            self._window.clear()
            self._window.refresh()
        return None

    """
    Clear line y.

    :return: returns None
    """
    @classmethod
    def clearln(self, y0):
        if self._window != None:
            self._window.move(y0, 0)
            self._window.clrtoeol()
        return None

    """
    Print a message string into its window. Choose a position. This affect to cursor.

    :return: returns nothing
    """
    @classmethod
    def print_message(self, message, x0 = -1, y0 = -1, attributes = curses.A_NORMAL):
        if self._window != None:
            if x0 > -1 and y0 > -1:
                # Set cursor position
                self._window.move(y0, x0)
            # Print
            try:
                self._window.addstr(message, attributes)
            except curses.error:
                pass    # Allow to print last position
            # Refresh
            self._window.refresh()
        return None

    """
    Print a message string into a window. Choose y position, x automatically in the center. This affect to cursor.

    :return: returns nothing
    """
    @classmethod
    def print_message_center(self, message, y0, attributes = curses.A_NORMAL):
        if self._window != None:
            y_max, x_max = self._window.getmaxyx()
            lenght = len( message )
            indent = x_max - lenght
            indent = (int)(indent / 2)
            y0_int = (int)(y0)

            self.set_cursor(self._window, indent, y0_int)
            self._window.addstr(message, attributes)
        return None

    """
    Print a message with delay between character. It cannot be skipped.

    :return: returns nothing
    """
    @classmethod
    def print_message_slow(self, message, x0 = -1, y0 = -1, inter_delay = 100, attributes = curses.A_NORMAL):
        if self._window != None:
            if x0 > -1 and y0 > -1:
                # Set cursor position
                self._window.move(y0, x0)
            for char in message:
                # Print
                try:
                    self._window.addch(char, attributes)
                    self._window.refresh()
                    curses.napms(inter_delay)
                except curses.error:
                    pass    # Allow to print last position
            # Refresh
            self._window.refresh()
        return None

    """
    Print background with color.

    :return: returns nothing
    """
    @classmethod
    def change_color(self, color_character, color_background):
        if self._window != None:
            curses.init_pair(7, color_character, color_background)
            self._window.bkgd(curses.color_pair(7)) # Warning, color pair apply to all elements in curses, probably need a variable inside and change global this value!
            self._window.refresh()
        return None

    """
    Wait for key. TODO remove?

    :return: returns None
    """
    @classmethod
    def waitforkey(self, print_text = True, x0 = -1, y0 = -1):
        #if x0 > -1 and y0 > -1:
        #    self.set_cursor(window, x0, y0)
        #if print_text:
        #    self.print_message(window, "Press any key to continue.")
        return self._window.getkey()

    """
    If input true, start taking keyboard events.

    :return: returns None
    """
    @classmethod
    def set_input_mode(self, input):
        self._window.keypad(input)
        return None

    """
    Wait for a character. Need set input mode true

    :return: returns None
    """
    @classmethod
    def get_character(self):
        # Set always NO DELAY?
        #if x0 > -1 and y0 > -1:
        #    self.set_cursor(window, x0, y0)
        #if print_text:
        #    self.print_message(window, "Press any key to continue.")
        return self._window.getch()

    @classmethod
    def draw(self):
        # Override me
        return None
