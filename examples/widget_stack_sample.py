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
    # Initialize curses manager
    #cm = CursesManager()
    #cm.set_current_window(stdscr)
    #cm.clear()
    #cm.create_screen_info_popup()
    return None

if __name__ == "__main__":
    wrapper(main)
    print("Thanks for use %s" % os.path.basename(__file__))
