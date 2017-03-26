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
    main_window = wpm.get_current_widget()

    # Create test element
    element_width = 10
    element_x0 = 1
    element_y0 = 2

    element = Element(10, 2, 1, 5)
    element.change_color(curses.COLOR_RED, curses.COLOR_YELLOW)

    wpm.msleep(2000)
    background.waitforkey(True, 1, 2)
    return None

if __name__ == "__main__":
    wrapper(main)
    print("Thanks for use %s" % os.path.basename(__file__))
