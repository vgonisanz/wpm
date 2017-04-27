# -*- coding: utf-8 -*-
# Based on Maze Generator using unicode line drawing chars by Vidar 'koala_man' Holen
# www.vidarholen.net    -   other online demo http://www.vidarholen.net/~vidar/generatemaze.py

import curses   # TODO remove for my colors or color pairs.
from hwidget import HWidget
from widget import EventObject
from widget import ChildElement
from maze_table import MazeTable

from sys import *

class Maze(HWidget):
    """Widget with create a maze
    """
    def __init__(self, width, height, x0, y0):
        # Initialize all variables
        self._maze_table = None

        # Assign
        super(Maze, self).__init__(width, height, x0, y0) # Initialize variables in Element, Override height

        map_x_offset = 3    # Number of extra horizontal spaces
        map_y_offset = 1    # Number of extra vertical spaces

        self._maze_table = MazeTable(width, height, x0, y0, map_x_offset, map_y_offset)
        self._maze_table.generate_random_maze()
        self.create_child("mazetable", self._maze_table)    # Add it as child to auto-restore if needed

        # Create event quit with q
        event_quit = EventObject(ord('q'), "Press q to quit", self.callback_quit)
        self.add_event(event_quit)

        # Create event quit with r
        event_generate = EventObject(ord('r'), "Press r to generate a new maze", self.callback_generate_random_maze)
        self.add_event(event_generate)

        # Create help
        help_message =  "Push r to generate another maze\n" + \
                        "Push keys to move after write question\n" + \
                        "Push q to quit\n"
        self.create_help(help_message)
        return None

    def callback_quit(self):
        """Callback to set true end condition and left run bucle.
        :return: None
        """
        self.end_condition()
        return None

    def callback_generate_random_maze(self):
        """Callback to generate a new maze table
        :return: None
        """
        self._maze_table.generate_random_maze()
        self._maze_table.draw()
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
            self.draw() # *TODO* bug, draw must not be necessary, show help from hwidget must work but dont.
            result = True
        return result

    def draw(self):
        """Re-draw element at current position
        return: None
        """
        # Border
        self.background.clear()
        self.foreground.clear()    # todo remove?
        #self.foreground.window.border()
        #self.background.window.refresh()
        #self.foreground.window.refresh()

        # Print children
        #self._draw_children()   # Re-draw children if needed. Textbox by default.

        # Print maze
        #self._maze_table.print_border_type() # remove
        self._maze_table.draw()
        return None

    def run(self):
        """Run question logic and autodraw
        return: None
        """
        self.background.logger.info("Run maze")
        self.draw()
        super(Maze, self).run()    # Widget autoiterate events
        return None
