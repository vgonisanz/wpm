# -*- coding: utf-8 -*-
import curses   # TODO remove for my colors or color pairs.
from widget import Widget
from eventobject import EventObject
from popup import Popup

class HWidget(Widget):
    """Widget with help included
    """
    def __init__(self, width, height, x0, y0):
        # Initialize
        self._help_pop_up = None

        # Call father Widget to complete its functionality.
        super(HWidget, self).__init__(width, height, x0, y0) # Initialize variables in Element, Override height
        return None

    def run(self):
        """Run question logic and autodraw
        return: None
        """
        super(HWidget, self).run()    # Widget autoiterate events
        return None

    def create_help(self, text = "Help"):
        """Create help popup
        :input action_object
        :return: returns nothing
        """
        ratio = 0.8
        antiratio = 1 - ratio
        help_width = int(ratio * self.background._width)
        help_height = int(ratio * self.background._height)
        help_x0 = int(antiratio/2 * self.background._width) + self.background._x
        help_y0 = int(antiratio/2 * self.background._height) + self.background._y

        self._help_pop_up = Popup(help_width, help_height, help_x0, help_y0, curses.KEY_F1)
        self._help_pop_up.set_title("Help")
        self._help_pop_up.set_message(text)

        event_help = EventObject(curses.KEY_F1, "Press F1 to show help", self.show_help)
        self.add_event(event_help)
        return None

    def show_help(self):
        """Show help.
        :return: True if success
        """
        result = False
        if self._help_pop_up:
            self.store_widget()
            self._help_pop_up.run()
            self.restore_widget()
            result = True
        return result
