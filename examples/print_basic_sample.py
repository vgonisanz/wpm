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

    # Initial message
    background.print_message("In this sample we are going to print messages.")
    background.waitforkey(True)
    background.clear()

    # Change color character and background
    background.print_message("But first, we change background color.")
    background.change_color(curses.COLOR_BLACK, curses.COLOR_WHITE)
    background.waitforkey(True)
    background.clear()

    return None

if __name__ == "__main__":
    wrapper(main)
    print("Thanks for use %s" % os.path.basename(__file__))
