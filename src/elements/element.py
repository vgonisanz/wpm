import curses

class Element(object):

    window = None
    _width = None
    _height = None
    _x = None
    _y = None
    attributes = curses.A_NORMAL


    def __init__(self, width, height, x0, y0):
        self._width = width
        self._height = height
        self._x = x0
        self._y = y0
        self.window = curses.newwin(height, width, y0, x0)
        return None

    """
    Set cursor at position.

    :return: returns None
    """

    def set_cursor(self, x0, y0):
        if self.window != None:
            self.window.move(y0, x0)
        return None

    """
    Clear current window.

    :return: returns nothing
    """

    def clear(self):
        if self.window != None:
            self.window.clear()
            self.window.refresh()
        return None

    """
    Clear line y.

    :return: returns None
    """

    def clearln(self, y0):
        if self.window != None:
            self.window.move(y0, 0)
            self.window.clrtoeol()
        return None

    """
    Print a message string into its window. Choose a position. This affect to cursor.

    :return: returns nothing
    """

    def print_message(self, message, x0 = -1, y0 = -1, attributes = curses.A_NORMAL):
        if self.window != None:
            if x0 > -1 and y0 > -1:
                # Set cursor position
                self.window.move(y0, x0)
            # Print
            try:
                self.window.addstr(message, attributes)
            except curses.error:
                pass    # Allow to print last position
            # Refresh
            self.window.refresh()
        return None

    """
    Print a message string into a window. Choose y position, x automatically in the center. This affect to cursor.

    :return: returns nothing
    """

    def print_message_center(self, message, y0, attributes = curses.A_NORMAL):
        if self.window != None:
            y_max, x_max = self.window.getmaxyx()
            lenght = len( message )
            indent = x_max - lenght
            indent = (int)(indent / 2)
            y0_int = (int)(y0)

            self.set_cursor(indent, y0_int)
            self.window.addstr(message, attributes)
            return True
        return False

    """
    Print a message with delay between character. It cannot be skipped.

    :return: returns nothing
    """

    def print_message_slow(self, message, x0 = -1, y0 = -1, inter_delay = 100, attributes = curses.A_NORMAL):
        if self.window != None:
            if x0 > -1 and y0 > -1:
                # Set cursor position
                self.window.move(y0, x0)
            for char in message:
                # Print
                try:
                    self.window.addch(char, attributes)
                    self.window.refresh()
                    curses.napms(inter_delay)
                except curses.error:
                    pass    # Allow to print last position
            # Refresh
            self.window.refresh()
        return None

    """
    Print background with a pattern from (0, 0).

    :return: returns nothing
    """

    def fill_with_pattern(self, pattern):
        if self.window != None:
            y_max, x_max = self.window.getmaxyx()
            lenght = len( pattern )
            times = (int)(x_max * y_max / lenght)
            self.window.move(0, 0)
            for i in range(0, times):
                self.print_message(pattern)
        return None

    """
    Print background with color.

    :return: returns nothing
    """

    def change_color(self, color_character, color_background):
        if self.window != None:
            curses.init_pair(7, color_character, color_background)
            self.window.bkgd(curses.color_pair(7)) # Warning, color pair apply to all elements in curses, probably need a variable inside and change global this value!
            self.window.refresh()
        return None

    """
    Wait for key. TODO remove?

    :return: returns None
    """

    def waitforkey(self, print_text = True, x0 = -1, y0 = -1):
        #if x0 > -1 and y0 > -1:
        #    self.set_cursor(window, x0, y0)
        #if print_text:
        #    self.print_message(window, "Press any key to continue.")
        return self.window.getkey()

    """
    If input true, start taking keyboard events.

    :return: returns None
    """

    def set_input_mode(self, input):
        self.window.keypad(input)
        return None

    """
    Wait for a character. Need set input mode true

    :return: returns None
    """

    def get_character(self):
        # Set always NO DELAY?
        #if x0 > -1 and y0 > -1:
        #    self.set_cursor(window, x0, y0)
        #if print_text:
        #    self.print_message(window, "Press any key to continue.")
        return self.window.getch()


    def draw(self):
        # Override me
        return None
