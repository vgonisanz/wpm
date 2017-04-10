#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src/elements'))

import curses               # Todo remove chaning own variables
from curses import wrapper  # Use my own wrapper

from wpm import Wpm
from element import Element
from sprite import Sprite

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
background = None
screen_width = 0
screen_height = 0

cactus_sprite = None
palmtree_sprite = None
ascii_sprite = None
unicode_sprite = None

def initialize():
    global wpm
    global background
    global screen_width
    global screen_height

    wpm = Wpm()
    screen_width, screen_height = wpm.get_window_size()
    background = wpm.get_background()
    return None

def prepare_colors():
    # A terminal can change colors ids! use palettes.
    # Color pair ID, character, background
    if curses.COLORS == 8:
        curses.init_pair(1, 0, 0)
        curses.init_pair(2, 10, 10) # Green shall be 10
        curses.init_pair(3, 14, 14) # Brown shall be 14
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
    global cactus_sprite

    # This sprite use all data provided in configuration variables.
    cactus_sprite = Sprite(cactus_width, cactus_colors, cactus)

    # Add 1 offset to cactus height
    offset_y = 1
    number_of_cactus = int(screen_height / (cactus_sprite.height + offset_y) )
    for i in range(0, number_of_cactus):
        y0 = i * (cactus_sprite.height + offset_y)
        background.print_sprite(cactus_sprite, 0, y0)
    return None

def print_palmtrees():
    global palmtree_sprite

    # This sprite create in constructor character array using as character ASCII 31 = ^_ as base.
    # You cannot see it because it have the same color as the background
    palmtree_sprite = Sprite(palmtree_width, palmtree_colors, [], 31)

    # Add 1 offset to palmtree height
    offset_x = cactus_sprite.width + 1
    offset_y = 1
    number_of_palmtree = int(screen_height / (palmtree_sprite.height + offset_y) )

    for i in range(0, number_of_palmtree):
        y0 = i * (palmtree_sprite.height + offset_y)
        background.print_sprite(palmtree_sprite, offset_x, y0)
    # Print sides

    return None

def print_ascii():
    global ascii_sprite

    xpos = cactus_width + palmtree_width * 2 + ascii_offset
    ascii_sprite = Sprite(ascii_width, ascii_colors, ascii_characters)
    background.print_sprite(ascii_sprite, xpos, 0)
    return None

def print_unicode():
    global unicode_sprite

    xpos = cactus_width + palmtree_width * 2 + ascii_offset
    ypos = ascii_sprite.height + unicode_offset
    unicode_sprite = Sprite(unicode_width, unicode_colors, unicode_characters)
    background.print_sprite(unicode_sprite, xpos, ypos)
    return None

def print_car():
    global car_sprite

    xpos = cactus_width + palmtree_width * 2 + ascii_offset + unicode_offset
    ypos = ascii_sprite.height + ascii_sprite.height + car_offset
    car_sprite = Sprite(car_width, car_colors, car_characters)
    background.print_sprite(car_sprite, xpos, ypos)
    return None

def main(stdscr):
    initialize()
    prepare_colors()

    print_cactus()
    print_palmtrees()
    print_ascii()
    print_unicode()
    print_car()

    background.window.getch()
    return None

if __name__ == "__main__":
    wrapper(main)
    print("Thanks for use %s" % os.path.basename(__file__))
