#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src/elements'))

import curses               # Todo remove chaning own variables
from curses import wrapper  # Use my own wrapper

from wpm import Wpm
from element import Element
from frame import Frame

# Configuration
mario_width = 3
mario_colors = [   2, 1, 2,
                    2, 1, 2,
                    2, 2, 2,
                    1, 2, 1,
                    1, 2, 1]

mario = [       32, 32, 32,
                 32, " ", 32,
                 32, 32, 32,
                 32, 32, 32,
                 32, 32, 32]


# Variables
wpm = None
screen = None
screen_width = 0
screen_height = 0

mario_frame_1 = None
mario_frame_2 = None
mario_sprite = None

def initialize():
    global wpm
    global screen
    global screen_width
    global screen_height

    wpm = Wpm(True)
    wpm.logger.info("Starting %s" % os.path.basename(__file__))
    screen_width, screen_height = wpm.get_window_size()
    screen = wpm.get_screen()
    return None

def prepare_colors():
    # A terminal can change colors ids! use palettes.
    # Color pair ID, character, screen
    if curses.COLORS == 8:
        curses.init_pair(1, 0, 0)
        curses.init_pair(2, 2, 2) # Green shall be 10
        curses.init_pair(3, 3, 3) # Brown shall be 14
        curses.init_pair(4, -1, -1) # -1 = default color
        curses.init_pair(5, 3, 0) # red over white expected
    if curses.COLORS == 256:
        curses.init_pair(1, 0, 0)
        curses.init_pair(2, 2, 2) # Red Expected
        curses.init_pair(3, 180, 180) # Flesh expected
        curses.init_pair(4, 95, 95) # Brown expected
        curses.init_pair(5, 3, 2) # white over red expected
    return None

def print_mario():
    global mario_frame

    # This frame use all data provided in configuration variables.
    mario_frame = Frame(mario_width, mario_colors, mario)

    # Add 1 offset to mario height
    offset_y = 1
    number_of_mario = int(screen_height / (mario_frame.height + offset_y) )
    screen.print_frame(mario_frame, 0, offset_y)
    return None

def main(stdscr):
    initialize()
    prepare_colors()

    print_mario()
    screen.window.getch()
    return None

if __name__ == "__main__":
    wrapper(main)
    print("Thanks for use %s" % os.path.basename(__file__))
