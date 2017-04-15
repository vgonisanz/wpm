import curses   # TODO remove for my colors or color pairs.
from widget import Widget
from textbox import TextBox
from widget import EventObject
from widget import ChildElement


class Popup(Widget):

    def __init__(self, width, height, x0, y0, quit_key = ord('q'), print_title = False):
        # Initialize all variables
        self._title = " Popup "
        self._print_title = False

        # Assign
        self._print_title = print_title
        super(Popup, self).__init__(width, height, x0, y0) # Initialize variables in Element, Override height

        # Add textbox inside
        textbox = TextBox(width - 2 , height - 2, x0 + 1, y0 + 1)
        #textbox.window.border()    # test draw
        textbox_child = ChildElement("textbox", textbox)
        self.add_child(textbox_child)

        # Create event quit with q
        event_quit = EventObject(quit_key, self.callback_quit)
        self.add_event(event_quit)

        return None

    def callback_quit(self):
        self.end_condition()
        return None

    """
    Set popup title

    return: None
    """

    def set_title(self, title):
        self._title = title
        return None

    """
    Set a message into textbox

    return: None
    """

    def set_message(self, message, centered = False):
        child = self.get_child("textbox")
        child.set_text(message)
        if centered:
            child.set_cursor_center(True)
        return None

    """
    Re-draw element at current position

    return: None
    """

    def draw(self):

        # Update background
        self.background.clear()    # todo remove?
        self.background.window.border()
        if self._print_title:
            self.background.print_message_center(self._title, 0, curses.A_REVERSE)
        self.background.window.refresh()

        # Update foreground
        self.foreground.window.refresh()
        self._draw_children()   # Re-draw children if needed. Textbox by default.
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
            #child.celement.clear()
            child.celement.draw()
            child.celement.window.refresh()
        return None
