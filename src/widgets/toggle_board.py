import curses   # TODO remove for my colors or color pairs.
from widget import Widget
from toggle_table import ToggleTable
from widget import EventObject
from widget import ChildElement


class ToggleBoard(Widget):
    _title = " ToggleBoard "
    _print_title = False
    _toggle_table = None
    xpos = 0
    ypos = 0


    def __init__(self, width, height, x0, y0, print_title = False):
        self._print_title = print_title
        super(ToggleBoard, self).__init__(width, height, x0, y0) # Initialize variables in Element, Override height

        # Initialize cursor center
        self.xpos = int(width/2)
        self.ypos = int(height/2)

        # Add toggletable inside
        self._toggle_table = ToggleTable(width - 2 , height - 2, x0 + 1, y0 + 1)
        #toggletable.window.border()    # test draw
        toggletable_child = ChildElement("toggletable", self._toggle_table)
        self.add_child(toggletable_child)

        # Create event quit with q
        event_quit = EventObject(ord('q'), self.callback_quit)
        self.add_event(event_quit)

        # Create event clear with c
        event_clear = EventObject(ord('c'), self.callback_clear)
        self.add_event(event_clear)

        # Create event random with r
        event_random = EventObject(ord('r'), self.callback_randomize)
        self.add_event(event_random)

        # Create event set current value
        event_set = EventObject(ord('s'), self.callback_set)
        self.add_event(event_set)

        # Create event toggle current value
        event_toggle = EventObject(ord('t'), self.callback_toggle)
        self.add_event(event_toggle)

        # Add controls
        event_up = EventObject(curses.KEY_UP, self.callback_up)
        event_down = EventObject(curses.KEY_DOWN, self.callback_down)
        event_left = EventObject(curses.KEY_LEFT, self.callback_left)
        event_right = EventObject(curses.KEY_RIGHT, self.callback_right)
        self.add_event(event_up)
        self.add_event(event_down)
        self.add_event(event_left)
        self.add_event(event_right)
        return None

    def callback_quit(self):
        self.end_condition()
        return None

    def callback_up(self):
        if self.ypos > 1:
            self.ypos -= 1
            self.background.set_cursor_position(self.xpos, self.ypos)
        return None

    def callback_down(self):
        if self.ypos < self._toggle_table._height:
            self.ypos += 1
            self.background.set_cursor_position(self.xpos, self.ypos)
        return None

    def callback_left(self):
        if self.xpos > 1:
            self.xpos -= 1
            self.background.set_cursor_position(self.xpos, self.ypos)
        return None

    def callback_right(self):
        if self.xpos < self._toggle_table._width:
            self.xpos += 1
            self.background.set_cursor_position(self.xpos, self.ypos)
        return None

    def callback_clear(self):
        self._toggle_table.erase()
        self._toggle_table.draw()
        self._toggle_table.clear()
        return None

    def callback_randomize(self):
        self._toggle_table.generate_random_table()
        self._toggle_table.draw()
        return None

    def callback_set(self):
        self._toggle_table.set(self.xpos, self.ypos)
        #self._toggle_table.draw()
        return None

    def callback_toggle(self):
        self._toggle_table.toggle(self.xpos, self.ypos)
        #self._toggle_table.draw()
        return None

    """
    Re-draw element at current position

    return: None
    """

    def draw(self):

        # Border
        self.background.clear()    # todo remove?
        self.background.window.border()
        self.background.window.refresh()
        #

        # Title
        if self._print_title:
            self.background.print_message_center(self._title, 0, curses.A_REVERSE)
        # Print message
        self._draw_children()   # Re-draw children if needed. toggletable by default.

        # Restore cursor
        self.background.set_cursor_position(self.xpos, self.ypos)
        return None

    """
    Run ToggleBoard logic and autodraw

    return: None
    """

    def run(self):
        self.draw()
        super(ToggleBoard, self).run()    # Widget autoiterate events
        return None
