# -*- coding: utf-8 -*-
import curses   # TODO remove for my colors or color pairs.
from widget import Widget
from textbox import TextBox
from widget import EventObject

class EditableTextBox(Widget):
    """Widget to store text and edit it. Complementary to TextBox element.
    """
    def __init__(self, width, height, x0, y0):
        # Initialize all variables
        self._last_text = ""
        self._text_box = None

        super(EditableTextBox, self).__init__(width, height, x0, y0) # Initialize variables in Element, Override height

        # Add dumb textbox inside
        self._text_box = TextBox(width, height, x0, y0)
        return None

    def get_text(self):
        """Get text written after run
        return: None
        """
        return self._last_text

    def draw(self):
        """Re-draw element at current position
        return: None
        """
        # Clean mayor frame to use child
        self.foreground.clear()
        self._text_box.draw()
        return None

    def run(self):
        """Run question logic and autodraw
        return: None
        """
        self.draw()

        # Active cursor with echo in start position *TODO* Check best site to do this.
        curses.echo()
        curses.curs_set(2)
        self._text_box.set_cursor_position(0, 0)

        # Wait until user write and push enter
        data_from_user = self._text_box.window.getstr()
        self._last_text = data_from_user.decode("utf-8")

        # Restore cursor *TODO* Check best site to do this.
        curses.noecho()
        curses.curs_set(0)
        return None
