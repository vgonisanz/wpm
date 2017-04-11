import curses   # TODO remove for my colors or color pairs.
from widget import Widget
from textbox import TextBox
from widget import EventObject
from widget import ChildElement

class EditableTextBox(Widget):
    _last_text = ""
    _text_box = None

    def __init__(self, width, height, x0, y0):
        super(EditableTextBox, self).__init__(width, height, x0, y0) # Initialize variables in Element, Override height

        # Add dumb textbox inside
        self._text_box = TextBox(width, height, x0, y0)
        return None

    """
    Get text written after run

    return: None
    """

    def get_text(self):
        return self._last_text

    """
    Re-draw element at current position

    return: None
    """

    def draw(self):
        # Clean mayor frame to use child
        self.background.clear()
        self._text_box.draw()
        return None

    """
    Run question logic and autodraw

    return: None
    """

    def run(self):
        self.draw()
        
        # Active cursor with echo in start position
        curses.echo()
        curses.curs_set(2)
        self._text_box.set_cursor_position(0, 0)

        # Wait until user write and push enter
        answer = self._text_box.window.getstr()
        self._last_text = answer.decode("utf-8")

        # Restore cursor
        curses.noecho()
        curses.curs_set(0)
        return None
