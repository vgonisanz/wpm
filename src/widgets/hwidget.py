import curses   # TODO remove for my colors or color pairs.
from widget import Widget
from widget import EventObject
from popup import Popup

"""
Widget with help included
"""
class HWidget(Widget):
    def __init__(self, width, height, x0, y0):
        # Initialize
        self._help_pop_up = None

        super(HWidget, self).__init__(width, height, x0, y0) # Initialize variables in Element, Override height
        return None

    """
    Run question logic and autodraw

    return: None
    """

    def run(self):
        super(HWidget, self).run()    # Widget autoiterate events
        return None

    """
    Create help popup
    :input action_object
    :return: returns nothing
    """
    def create_help(self, text):
        help_width = int(self.background._width*8/10)
        help_height = int(self.background._height*8/10)
        help_x0 = 1
        help_y0 = 1

        self._help_pop_up = Popup(help_width, help_height, help_x0, help_y0, curses.KEY_F1)
        self._help_pop_up.set_title("Help")
        self._help_pop_up.set_message(text)

        event_help = EventObject(curses.KEY_F1, self.show_help)
        self.add_event(event_help)
        return None

    """
    Show help.

    :return: returns nothing
    """

    def show_help(self):
        self._help_pop_up.run()
        # Hide again
        self._help_pop_up.background.window.clear()
        self._help_pop_up.background.window.refresh()
        # Redraw
        self.draw()
        return None
