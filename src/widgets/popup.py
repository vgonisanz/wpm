import curses   # TODO remove for my colors or color pairs.
from widget import Widget
from textbox import TextBox
from widget import EventObject
from widget import ChildElement


class Popup(Widget):
    _title = " Popup "
    _print_title = False


    def __init__(self, width, height, x0, y0, print_title = False):
        self._print_title = print_title
        super(Popup, self).__init__(width, height, x0, y0) # Initialize variables in Element, Override height

        # Add textbox inside
        textbox = TextBox(width - 1, height - 1, x0 + 1, y0 + 1)
        textbox_child = ChildElement("textbox", textbox)
        self.add_child(textbox_child)

        # Create event quit with q
        event_quit = EventObject(ord('q'), self.callback_quit)
        self.add_event(event_quit)

        return None

    def callback_quit(self):
        self.end_condition()
        return None

    """
    Set a message into textbox

    return: None
    """

    def set_message(self, message):
        child = self.get_child("textbox")
        child.celement.set_text(message)
        return None

    """
    Re-draw element at current position

    return: None
    """

    def get_child(self, child_id):
        child = None
        for member in self._children:
            if member.cid == child_id:
                return member
        return child

    """
    Re-draw element at current position

    return: None
    """

    def draw(self):
        # Border
        self._background.window.border()
        # Title
        if self._print_title:
            self._background.print_message_center(self._title, 0, curses.A_REVERSE)
        # Print message
        child = self.get_child("textbox")
        result = child.celement.print_message_center("HOOLA", 3, curses.A_NORMAL)
        #self._background.print_message_center(str(result), 3, curses.A_NORMAL)
        #child.celement.window.refresh()
        #self._draw_children()   # Re-draw children if needed. Textbox by default.
        self._background.print_message_center(child.celement.get_text(), 3, curses.A_NORMAL)
        return None

    """
    Run popup logic and autodraw

    return: None
    """

    def run(self):
        self.draw()
        super(Popup, self).run()    # Widget autoiterate events
        return None

    """
    This private method iterate children and draw them.

    :return: returns nothing
    """

    def _draw_children(self):
        for child in self._children:
            child.celement.draw()
        return None
