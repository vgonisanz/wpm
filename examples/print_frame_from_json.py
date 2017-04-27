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

import json

# Configuration
json_filename = 'input/mario_normal.json'
x0 = 5
y0 = 5
mario_pixel_width = 2

# Variables
wpm = None
screen = None
screen_width = 0
screen_height = 0

mario_frame = None

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
        curses.init_pair(1, -1, -1)  # Background: -1 is default.
        curses.init_pair(2, 3, 3) # Hair: Brown shall be 14 orange shall be 219
        curses.init_pair(3, 4, 4) # Skin: Pink
        curses.init_pair(4, 2, 2) # Clothes: Red shall be 2
        #curses.init_pair(5, 95, 95) # Test: ...
    if curses.COLORS == 256:
        curses.init_pair(1, -1, -1)  # Background: -1 is default.
        curses.init_pair(2, 95, 95) # Hair: Brown shall be 14 orange shall be 219
        curses.init_pair(3, 218, 218) # Skin: Pink
        curses.init_pair(4, 2, 2) # Clothes: Red shall be 2
        #curses.init_pair(5, 95, 95) # Test: ...
    return None

def load_json_frame(input_name):
    with open(input_name, encoding='utf-8') as data_file:
        string_data = json.load(data_file)
        json_data = json.loads(string_data)
    return json_data

def print_mario():
    global mario_frame

    # This frame use all data provided in configuration variables.
    json_data = load_json_frame(json_filename)
    metadata = json_data['metadata']
    image_width = metadata['size'][0]
    pixel_list = json_data['pixel_list']

    # Convert pixels to int
    for i in range(len(pixel_list)):
        pixel_list[i] = int(pixel_list[i])

    mario_frame = Frame(image_width, pixel_list)

    # Draw it
    screen.print_frame(mario_frame, mario_pixel_width, x0, y0)
    screen.window.getch()
    return None

def main(stdscr):
    initialize()
    prepare_colors()
    print_mario()
    return None

if __name__ == "__main__":
    wrapper(main)
    print("Thanks for use %s" % os.path.basename(__file__))
