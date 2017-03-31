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

def function1():
    # ...
    wpm.msleep(1)
    background.waitforkey()
    return None

def main(stdscr):
    initialize()

    # Create element or widget here
    # ...
    function1()

    return None

if __name__ == "__main__":
    wrapper(main)
    print("Thanks for use %s" % os.path.basename(__file__))
