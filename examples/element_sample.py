import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src/elements'))

import curses               # Todo remove chaning own variables
from curses import wrapper  # Use my own wrapper

from wpm import Wpm
from element import Element

# Configuration
element_width = 20
element_height = 10
element_x0 = 1
element_y0 = 2

# Variables
wpm = None
background = None
element = None

def initialize():
    global wpm
    global background

    wpm = Wpm(True)
    wpm.logger.info("Starting %s" % os.path.basename(__file__))
    background = wpm.get_background()
    return None

def create_element():
    global element

    # Create test element
    element = Element(element_width, element_height, element_x0, element_y0)
    element.change_color(curses.COLOR_RED, curses.COLOR_YELLOW)

    wpm.msleep(2000)
    background.waitforkey()
    return None

def main(stdscr):
    initialize()
    create_element()
    return None

if __name__ == "__main__":
    wrapper(main)
    print("Thanks for use %s" % os.path.basename(__file__))
