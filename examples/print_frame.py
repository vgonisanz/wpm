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

cactus_frame = None
palmtree_frame = None
ascii_frame = None
unicode_frame = None
car_frame = None

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
        curses.init_pair(2, 10, 10) # Green expected
        curses.init_pair(3, 209, 209) # Brown expected
        curses.init_pair(4, -1, -1) # -1 = default color
        curses.init_pair(5, 3, 2) # white over red expected
    return None

def print_cactus():
    global cactus_frame

    # This frame use all data provided in configuration variables.
    cactus_frame = Frame(cactus_width, cactus_colors, cactus)

    # Add 1 offset to cactus height
    offset_y = 1
    number_of_cactus = int(screen_height / (cactus_frame.height + offset_y) )
    for i in range(0, number_of_cactus):
        y0 = i * (cactus_frame.height + offset_y)
        screen.print_frame(cactus_frame, 1, 0, y0)
    return None

def print_palmtrees():
    global palmtree_frame

    # This frame create in constructor character array using as character ASCII 31 = ^_ as base.
    # You cannot see it because it have the same color as the screen
    palmtree_frame = Frame(palmtree_width, palmtree_colors, [], 32)

    # Add 1 offset to palmtree height
    offset_x = cactus_frame.width + 1
    offset_y = 1
    number_of_palmtree = int(screen_height / (palmtree_frame.height + offset_y) )

    for i in range(0, number_of_palmtree):
        y0 = i * (palmtree_frame.height + offset_y)
        screen.print_frame(palmtree_frame, 2, offset_x, y0)
    # Print sides

    return None

def print_ascii():
    global ascii_frame

    xpos = cactus_width + palmtree_width * 2 + ascii_offset
    ascii_frame = Frame(ascii_width, ascii_colors, ascii_characters)
    screen.print_frame(ascii_frame, 1, xpos, 0)
    return None

def print_unicode():
    global unicode_frame

    xpos = cactus_width + palmtree_width * 2 + ascii_offset
    ypos = ascii_frame.height + unicode_offset
    unicode_frame = Frame(unicode_width, unicode_colors, unicode_characters)
    screen.print_frame(unicode_frame, 1, xpos, ypos)
    return None

def print_car():
    global car_frame

    xpos = cactus_width + palmtree_width * 2 + ascii_offset + unicode_offset
    ypos = ascii_frame.height + ascii_frame.height + car_offset
    car_frame = Frame(car_width, car_colors, car_characters)
    screen.print_frame(car_frame, 1, xpos, ypos)
    return None

def main(stdscr):
    initialize()
    prepare_colors()

    print_cactus()
    print_palmtrees()
    print_ascii()
    print_unicode()
    print_car()

    screen.window.getch()
    return None

if __name__ == "__main__":
    wrapper(main)
    print("Thanks for use %s" % os.path.basename(__file__))
