import curses   # TODO remove for my colors or color pairs.
from widget import Widget
from element import Element
from widget import EventObject


class Popup(Widget):
    _title = " Popup "
    _message = ""

    _print_title = False


    def __init__(self, width, height, x0, y0, print_title = False):
        self._print_title = print_title
        super(Popup, self).__init__(width, height, x0, y0) # Initialize variables in Element, Override height

        #Todo add a window inside border?

        # Create event quit with q
        event_quit = EventObject(ord('q'), self.callback_quit)
        self.add_event(event_quit)

        return None

    def callback_quit(self):
        self.end_condition()
        return None

    """
    Re-draw element at current position

    return: None
    """

    def set_message(self, message):
        self._message = message
        return None

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
        self._background.print_message_center(self._message, 3, curses.A_NORMAL)
        return None

    """
    Run popup logic and autodraw

    return: None
    """

    def run(self):
        self.draw()
        super(Popup, self).run()    # Widget autoiterate events
        return None
