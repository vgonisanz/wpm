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
        self._player_position_x = 1
        self._player_position_y = 1

        # Assign
        super(Maze, self).__init__(width, height, x0, y0) # Initialize variables in Element, Override height
        self.background.logger.info("Creating maze")

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

        # Add arrow controls
        event_up = EventObject(curses.KEY_UP, "Press <UP> to go up", self.callback_up)
        event_down = EventObject(curses.KEY_DOWN, "Press <DOWN> to go down", self.callback_down)
        event_left = EventObject(curses.KEY_LEFT, "Press <LEFT> to go left", self.callback_left)
        event_right = EventObject(curses.KEY_RIGHT, "Press <RIGHT> to go right", self.callback_right)
        self.add_event(event_up)
        self.add_event(event_down)
        self.add_event(event_left)
        self.add_event(event_right)

        # Create help
        help_message =  "Push r to generate another maze\n" + \
                        "Push keys to move after write question\n" + \
                        "Push q to quit\n"
        self.create_help(help_message)
        return None

    def set_player_position(self, x0, y0):
        self._player_position_x = x0
        self._player_position_y = y0
        self._maze_table.draw_player(self._player_position_x, self._player_position_y)
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
        self.set_player_position(1, 1)
        super(Maze, self).run()    # Widget autoiterate events
        return None

    def callback_down(self):
        """Move y + 1 if no wall
        return: None
        """
        previous_y = self._player_position_y + 1
        character = self._maze_table.get_character_at(self._player_position_x, previous_y)
        if character == ord(' '):
            self._maze_table.undraw_player(self._player_position_x, self._player_position_y)
            self._player_position_y = previous_y
            self._maze_table.draw_player(self._player_position_x, self._player_position_y)
        return None

    def callback_up(self):
        """Move y - 1 if no wall
        return: None
        """
        previous_y = self._player_position_y - 1
        character = self._maze_table.get_character_at(self._player_position_x, previous_y)
        if character == ord(' '):
            self._maze_table.undraw_player(self._player_position_x, self._player_position_y)
            self._player_position_y = previous_y
            self._maze_table.draw_player(self._player_position_x, self._player_position_y)
        return None

    def callback_left(self):
        """Move x - 1 if no wall
        return: None
        """
        previous_x = self._player_position_x - 1
        character = self._maze_table.get_character_at(previous_x, self._player_position_y)
        if character == ord(' '):
            self._maze_table.undraw_player(self._player_position_x, self._player_position_y)
            self._player_position_x = previous_x
            self._maze_table.draw_player(self._player_position_x, self._player_position_y)
        return None

    def callback_right(self):
        """Move x + 1 if no wall
        return: None
        """
        next_x = self._player_position_x + 1
        character = self._maze_table.get_character_at(next_x, self._player_position_y)
        if character == ord(' '):
            self._maze_table.undraw_player(self._player_position_x, self._player_position_y)
            self._player_position_x = next_x
            self._maze_table.draw_player(self._player_position_x, self._player_position_y)
        return None
