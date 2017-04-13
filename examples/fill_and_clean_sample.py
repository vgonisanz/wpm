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
pattern = "#==|==#"

# Variables
wpm = None
background = None

def initialize():
    global wpm
    global background

    wpm = Wpm(True)
    wpm.logger.info("Starting %s" % os.path.basename(__file__))
    background = wpm.get_background()   # Get main window to print
    return None

def fill_with_pattern():
    background.fill_with_pattern(pattern)
    wpm.msleep(1)
    background.waitforkey()
    return None

def clear_line_from():
    background.print_message("Clear line from position: (%dx%d) " % (position_x0, position_y0), position_x0, position_y0)
    # clrtoeol(4, 5)
    wpm.msleep(1)
    background.waitforkey()
    return None

def clear_until_bottom():
    background.print_message("Clear to bottom from position: (%dx%d) " % (position_x0, position_y0), position_x0, position_y0)
    #cm.clrtobot(6, 7)
    wpm.msleep(1)
    background.waitforkey()
    return None

def main(stdscr):
    initialize()
    fill_with_pattern()
    clear_line_from() #TODO complete
    clear_until_bottom() #TODO complete
    return None

if __name__ == "__main__":
    wrapper(main)
    print("Thanks for use %s" % os.path.basename(__file__))
