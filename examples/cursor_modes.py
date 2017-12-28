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
screen = None

def initialize():
    global wpm
    global screen

    wpm = Wpm(True)
    wpm.logger.info("Starting %s" % os.path.basename(__file__))
    screen = wpm.get_screen()   # Get main window to print
    return None

def set_cursor_invisible():
    screen.clear()
    screen.print_message("Cursor invisible:\n --> ", position_x0, position_y0)
    wpm.set_cursor_mode(0)
    screen.waitforkey()
    return None

def set_cursor_visible():
    screen.clear()
    screen.print_message("Cursor visible:\n --> ", position_x0, position_y0)
    wpm.set_cursor_mode(1)
    screen.waitforkey()
    return None

def set_cursor_veryvisible():
    screen.clear()
    screen.print_message("Cursor very visible:\n --> ", position_x0, position_y0)
    wpm.set_cursor_mode(2)
    screen.waitforkey()
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
