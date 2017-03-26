import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src/elements'))

import curses               # Todo remove chaning own variables
from curses import wrapper  # Use my own wrapper

from wpm import Wpm
from element import Element

# Configuration

# Variables

def main(stdscr):
    wpm = Wpm()
    background = wpm.get_background()

    # Create test element
    element_width = 20
    element_height = 10
    element_x0 = 1
    element_y0 = 2

    element = Element(element_width, element_height, element_x0, element_y0)
    element.change_color(curses.COLOR_RED, curses.COLOR_YELLOW)

    wpm.msleep(2000)
    background.waitforkey()
    return None

if __name__ == "__main__":
    wrapper(main)
    print("Thanks for use %s" % os.path.basename(__file__))
