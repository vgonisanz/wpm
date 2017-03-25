import curses               # Todo remove chaning own variables
from curses import wrapper  # Use my own wrapper

import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
from wpm import Wpm

from element import Element

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
    wpm.waitforkey(main_window, True, 1, 2)
    return None

if __name__ == "__main__":
    wrapper(main)
    print("Thanks for use element sample")
