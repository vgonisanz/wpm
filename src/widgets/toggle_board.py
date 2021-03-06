# -*- coding: utf-8 -*-
import curses   # TODO remove for my colors or color pairs.
from hwidget import HWidget
from toggle_table import ToggleTable
from eventobject import EventObject


class ToggleBoard(HWidget):
    def __init__(self, width, height, x0, y0, print_title = False):
        # Initialize all variables
        self._title = " ToggleBoard "
        self._print_title = False
        self.xpos = 0
        self.ypos = 0

        # Assign
        self._print_title = print_title
        super(ToggleBoard, self).__init__(width, height, x0, y0) # No create foreground
        self.background.logger.info("Creating toggle board")

        # Add toggletable as foreground, is not a child.
        toggle_width = width - 2
        toggle_height = height - 2
        toggle_x0 = x0 + 1
        toggle_y0 = y0 + 1

        self._toggle_table = ToggleTable(toggle_width, toggle_height, toggle_x0, toggle_y0)
        self.create_child("toggletable", self._toggle_table)    # Add it as child to auto-restore if needed

        # Initialize cursor center
        self.xpos = int(toggle_width/2)
        self.ypos = int(toggle_height/2)

        # Create event quit with q
        event_quit = EventObject(ord('q'), "Press q to quit", self.callback_quit)
        self.add_event(event_quit)

        # Create event clear with c
        event_clear = EventObject(ord('c'), "Press c to clear table", self.callback_clear)
        self.add_event(event_clear)

        # Create event random with r
        event_random = EventObject(ord('r'), "Press r to randomize", self.callback_randomize)
        self.add_event(event_random)

        # Create event set current value
        event_set = EventObject(ord('s'), "Press s to set cursor position", self.callback_set)
        self.add_event(event_set)

        # Create event toggle current value
        event_toggle = EventObject(ord('t'), "Press t to toggle cursor position", self.callback_toggle)
        self.add_event(event_toggle)

        # Add controls
        event_up = EventObject(curses.KEY_UP, "Press UP to move", self.callback_up)
        event_down = EventObject(curses.KEY_DOWN, "Press DOWN to move", self.callback_down)
        event_left = EventObject(curses.KEY_LEFT, "Press LEFT to move", self.callback_left)
        event_right = EventObject(curses.KEY_RIGHT, "Press RIGHT to move", self.callback_right)
        self.add_event(event_up)
        self.add_event(event_down)
        self.add_event(event_left)
        self.add_event(event_right)

        help_message = "Use arrows to move\n" + \
                        "Use c to clear table\n" + \
                        "Use r to generate random board\n" + \
                        "Use s to set cursor position\n" + \
                        "Use t to toggle cursor position\n" + \
                        "Use q to quit."
        self.create_help(help_message)
        return None

    def callback_quit(self):
        """Callback to set true end condition and left run bucle.
        :return: None
        """
        self.end_condition()
        return None

    def callback_up(self):
        """Callback to Go upper in element if in range
        :return: None
        """
        if self.ypos > 0:
            self.ypos -= 1
            self._toggle_table.set_cursor_position(self.xpos, self.ypos)
        return None

    def callback_down(self):
        """Callback to Go lower in table element if in range
        :return: None
        """
        if self.ypos < self._toggle_table._height - 1:
            self.ypos += 1
            self._toggle_table.set_cursor_position(self.xpos, self.ypos)
        return None

    def callback_left(self):
        """Callback to Go left in table element if in range
        :return: None
        """
        if self.xpos > 0:
            self.xpos -= 1
            self._toggle_table.set_cursor_position(self.xpos, self.ypos)
        return None

    def callback_right(self):
        """Callback to Go right in table element if in range
        :return: None
        """
        if self.xpos < self._toggle_table._width - 1:
            self.xpos += 1
            self._toggle_table.set_cursor_position(self.xpos, self.ypos)
        return None

    def callback_clear(self):
        """Callback to clear all characters in the table element
        :return: None
        """
        #curses.curs_set(0)  # Hide cursor
        self._toggle_table.erase()
        self._toggle_table.clear()
        return None

    def callback_randomize(self):
        """Callback to assign or not randomily characters in the table element
        :return: None
        """
        xpos_0 = self.xpos
        ypos_0 = self.ypos
        #curses.curs_set(0)  # Hide cursor
        self._toggle_table.generate_random_table()
        self._toggle_table.draw()
        #curses.curs_set(2)  # Show cursor
        # Restore cursor
        self.background.set_cursor_position(xpos_0, ypos_0)
        return None

    def callback_set(self):
        """Callback to set a character in the current cursor position
        :return: None
        """
        self._toggle_table.set(self.xpos, self.ypos)
        self._toggle_table.set_cursor_position(self.xpos, self.ypos)   # Restore cursor
        return None

    def callback_toggle(self):
        """Callback to toggle a character in the current cursor position
        :return: None
        """
        self._toggle_table.toggle(self.xpos, self.ypos)
        self._toggle_table.set_cursor_position(self.xpos, self.ypos)   # Restore cursor
        return None

    def draw(self):
        """Re-draw element at current position
        return: None
        """
        # Update background
        self.background.clear()
        self.background.window.border()
        if self._print_title:
            self.background.print_message_center(self._title, 0, curses.A_REVERSE)
        self.background.window.refresh()

        # Update foreground
        self._toggle_table.clear()
        self._toggle_table.window.refresh()
        return None

    def run(self):
        """Run ToggleBoard logic and autodraw
        return: None
        """
        self.background.logger.info("Run toggle board")
        curses.curs_set(0)  # Hide cursor
        self.draw()
        curses.curs_set(2)  # Show cursor
        self._toggle_table.set_cursor_position(self.xpos, self.ypos)   # Restore cursor
        super(ToggleBoard, self).run()    # Widget autoiterate events
        curses.curs_set(0)  # Hide cursor
        return None
