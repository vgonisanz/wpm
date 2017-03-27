import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src/elements'))

import curses               # Todo remove chaning own variables
from curses import wrapper  # Use my own wrapper

from wpm import Wpm
from element import Element

# Configuration
position_x0 = 1
position_y0 = 2

# Variables
wpm = None
background = None

def initialize():
    global wpm
    global background

    wpm = Wpm()
    background = wpm.get_background()   # Get main window to print
    return None

def set_cursor_invisible():
    background.clear()
    background.print_message("Cursor invisible:\n --> ", position_x0, position_y0)
    wpm.set_cursor_mode(0)
    background.waitforkey()
    return None

def set_cursor_visible():
    background.clear()
    background.print_message("Cursor visible:\n --> ", position_x0, position_y0)
    wpm.set_cursor_mode(1)
    background.waitforkey()
    return None

def set_cursor_veryvisible():
    background.clear()
    background.print_message("Cursor very visible:\n --> ", position_x0, position_y0)
    wpm.set_cursor_mode(2)
    background.waitforkey()
    return None

def main(stdscr):
    initialize()
    set_cursor_invisible()
    set_cursor_visible()
    set_cursor_veryvisible()
    return None

if __name__ == "__main__":
    wrapper(main)
    print("Thanks for use %s" % os.path.basename(__file__))
