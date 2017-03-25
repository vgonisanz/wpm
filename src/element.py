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

    @classmethod
    def draw(self):
        # Override me
        return None
