import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src/elements'))

import curses               # Todo remove chaning own variables
from curses import wrapper  # Use my own wrapper

from wpm import Wpm
from element import Element

# Configuration
border_width = 20
border_height = 10
border_x0 = 1
border_y0 = 2

# Variables
element = None
element_background = None

def initialize():
    global wpm
    global background

    wpm = Wpm()
    #background = wpm.get_background()
    return None

def create_element():
    global element

    element = Element(border_width, border_height, border_x0, border_y0)
    return None

def set_border(number):
    element.print_border(number)
    element.waitforkey()
    return None

def main(stdscr):
    initialize()
    create_element()
    set_border(0)
    set_border(1)
    set_border(2)
    set_border(3)


    return None

if __name__ == "__main__":
    wrapper(main)
    print("Thanks for use %s" % os.path.basename(__file__))
