import curses   # TODO remove for my colors or color pairs.
from element import Element

class TextBox(Element):
    _text = ""
    _cursor_x = 0
    _cursor_y = 0

    def __init__(self, width, height, x0, y0, text = ""):
        super(TextBox, self).__init__(width, height, x0, y0)
        self._text = text
        return None

    def set_cursor(self, x, y):
        self._cursor_x = x
        self._cursor_y = y
        return None

    def set_cursor_center(self):
        y_max, x_max = self.window.getmaxyx()
        lenght = len( self._text )
        indent_x = (int)(x_max/2 - lenght/2)
        indent_y = (int)(y_max/2) - 1

        self.set_cursor(indent_x, indent_y)
        return None

    def set_text(self, text):
        self._text = text
        return None

    def get_text(self):
        return self._text

    """
    Draw text if provided

    return: None
    """

    def draw(self):
        self.print_message(self._text, self._cursor_x, self._cursor_y, curses.A_NORMAL)
        return None
