#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src/elements'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src/widgets'))

import curses               # Todo remove chaning own variables
from curses import wrapper  # Use my own wrapper

from wpm import Wpm
from element import Element
from maze import Maze

# Configuration
position_x0 = 0
position_y0 = 0

maze_width = 40
maze_height = 40

# Variables
wpm = None
screen = None
maze = None

def initialize():
    global wpm
    global screen

    wpm = Wpm(True)
    wpm.logger.info("Starting %s" % os.path.basename(__file__))
    screen = wpm.get_screen()   # Get main window to print
    return None

def generate_maze():
    global maze

    width = maze_width
    height = maze_height
    maze = Maze(maze_width, maze_height, position_x0, position_y0)
    maze.run()
    return None

def main(stdscr):
    initialize()

    generate_maze()
    return None

if __name__ == "__main__":
    wrapper(main)
    print("Thanks for use %s" % os.path.basename(__file__))
