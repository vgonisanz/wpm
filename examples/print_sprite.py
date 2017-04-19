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
palmtree_width = 8
palmtree_colors = [ 1, 1, 1, 1, 1, 2, 2, 2,
                    1, 2, 2, 2, 1, 1, 2, 2,
                    2, 1, 1, 2, 2, 2, 1, 1,
                    1, 1, 2, 2, 2, 1, 2, 1,
                    1, 2, 2, 3, 3, 1, 1, 2,
                    2, 1, 1, 3, 3, 1, 1, 2,
                    1, 1, 1, 3, 3, 1, 1, 1,
                    1, 1, 1, 3, 3, 1, 1, 1]

cactus_width = 3
cactus_colors = [   2, 1, 2,
                    2, 1, 2,
                    2, 2, 2,
                    1, 2, 1,
                    1, 2, 1]

cactus = [       32, 32, 32,
                 32, " ", 32,
                 32, 32, 32,
                 32, 32, 32,
                 32, 32, 32]

ascii_width = 3
ascii_colors = [        4, 4, 4,
                        4, 4, 4,
                        4, 4, 4 ]
ascii_characters = [    "a", "b", "c",
                        65, 66, 67,         # ASCII values: A, B, C
                        134, 135, 136    ]  # Extended ASCII:  doesn't works.
ascii_offset = 2

unicode_width = 3
unicode_colors = [      4, 4, 4,
                        4, 4, 4,
                        4, 4, 4 ]
unicode_characters = [      "\u00B6", "Ū", "Ž",         # Unicode values, you can print directly or with ID
                            "Ā", "\u0488", "Ž",
                            "Ā", "Ū", "\u16E5",    ]    # Some characters can override other characters!
unicode_offset = 1

car_width = 3
car_colors = [          1, 1, 1,
                        1, 1, 1,
                        1, 1, 1,
                        1, 1, 1,
                        1, 1, 1 ]
                        # Unicode box drawing
car_characters = [          " ", "\u2533", " ",
                            "\u2523", "\u2588", "\u252B",
                            " ", "\u2588", " ",
                            "\u255F", "\u2588", "\u2562",
                            "\u250C", "\u2538", "\u2510"]
car_offset = 1

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
    global cactus_frame

    # This frame use all data provided in configuration variables.
    cactus_frame = Frame(cactus_width, cactus_colors, cactus)

    # Add 1 offset to cactus height
    offset_y = 1
    number_of_cactus = int(screen_height / (cactus_frame.height + offset_y) )
    for i in range(0, number_of_cactus):
        y0 = i * (cactus_frame.height + offset_y)
        screen.print_frame(cactus_frame, 0, y0)
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
